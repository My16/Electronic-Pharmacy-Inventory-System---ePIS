# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# ─────────────────────────────────────────────────────────────────────────────
# USER PROFILE
# ─────────────────────────────────────────────────────────────────────────────
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('user',  'User'),
        ('staff', 'Staff'),
        ('admin', 'Administrator'),
    ]
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    middle_name = models.CharField(max_length=100, blank=True, default='')
    role        = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    avatar      = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} — {self.get_role_display()}"

    def get_full_name_with_middle(self):
        parts = [self.user.first_name, self.middle_name, self.user.last_name]
        return ' '.join(p for p in parts if p).strip() or self.user.username


@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)


# ─────────────────────────────────────────────────────────────────────────────
# SUPPLIER
# ─────────────────────────────────────────────────────────────────────────────
class Supplier(models.Model):
    name         = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=150, blank=True)
    phone        = models.CharField(max_length=50, blank=True)
    email        = models.EmailField(blank=True)
    address      = models.TextField(blank=True)
    notes        = models.TextField(blank=True)
    is_active    = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# ─────────────────────────────────────────────────────────────────────────────
# MEDICINE CATEGORY
# ─────────────────────────────────────────────────────────────────────────────
class MedicineCategory(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Medicine Categories'
        ordering = ['name']


# ─────────────────────────────────────────────────────────────────────────────
# MEDICINE
# ─────────────────────────────────────────────────────────────────────────────
class Medicine(models.Model):

    DOSAGE_FORM_CHOICES = [
        ('tablet',      'Tablet'),
        ('capsule',     'Capsule'),
        ('syrup',       'Syrup'),
        ('suspension',  'Suspension'),
        ('injection',   'Injection'),
        ('cream',       'Cream'),
        ('ointment',    'Ointment'),
        ('drops',       'Drops'),
        ('inhaler',     'Inhaler'),
        ('patch',       'Patch'),
        ('suppository', 'Suppository'),
        ('powder',      'Powder'),
        ('other',       'Other'),
    ]

    medicine_name    = models.CharField(max_length=200)
    generic_name     = models.CharField(max_length=200)
    brand_name       = models.CharField(max_length=200, blank=True)
    category         = models.ForeignKey(
                           MedicineCategory, on_delete=models.SET_NULL,
                           null=True, blank=True, related_name='medicines')
    dosage_form      = models.CharField(max_length=20, choices=DOSAGE_FORM_CHOICES, default='tablet')
    strength         = models.CharField(max_length=100)
    manufacturer     = models.CharField(max_length=200, blank=True)
    supplier         = models.ForeignKey(
                           Supplier, on_delete=models.SET_NULL,
                           null=True, blank=True, related_name='medicines')
    barcode          = models.CharField(max_length=100, blank=True, unique=True, null=True)
    batch_number     = models.CharField(max_length=100, blank=True)
    expiry_date      = models.DateField(null=True, blank=True)
    purchase_price   = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    selling_price    = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock_quantity   = models.PositiveIntegerField(default=0)
    reorder_level    = models.PositiveIntegerField(default=10)
    storage_location = models.CharField(max_length=150, blank=True)
    is_active        = models.BooleanField(default=True)
    created_by       = models.ForeignKey(
                           User, on_delete=models.SET_NULL,
                           null=True, blank=True, related_name='medicines_created')
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine_name} {self.strength}"

    @property
    def is_out_of_stock(self):
        return self.stock_quantity == 0

    @property
    def is_low_stock(self):
        return 0 < self.stock_quantity <= self.reorder_level

    @property
    def is_expiring_soon(self):
        if not self.expiry_date:
            return False
        return self.expiry_date <= (timezone.now().date() + timezone.timedelta(days=90))

    @property
    def is_expired(self):
        if not self.expiry_date:
            return False
        return self.expiry_date < timezone.now().date()

    @property
    def stock_status(self):
        if self.is_out_of_stock:
            return 'out_of_stock'
        if self.is_low_stock:
            return 'low_stock'
        return 'in_stock'

    class Meta:
        ordering = ['medicine_name']
        verbose_name_plural = 'Medicines'


# ─────────────────────────────────────────────────────────────────────────────
# STOCK MOVEMENT
# ─────────────────────────────────────────────────────────────────────────────
class StockMovement(models.Model):

    MOVEMENT_TYPES = [
        ('in',       'Stock In'),
        ('out',      'Stock Out'),
        ('adjust',   'Adjustment'),
        ('return',   'Return'),
        ('expired',  'Expired Removal'),
        ('damaged',  'Damaged / Disposal'),
        ('audit',    'Audit Adjustment'),
    ]

    medicine        = models.ForeignKey(
                          Medicine, on_delete=models.CASCADE, related_name='movements')
    movement_type   = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity        = models.IntegerField()
    quantity_before = models.PositiveIntegerField()
    quantity_after  = models.PositiveIntegerField()
    supplier        = models.ForeignKey(
                          Supplier, on_delete=models.SET_NULL,
                          null=True, blank=True)
    batch_number    = models.CharField(max_length=100, blank=True)
    expiry_date     = models.DateField(null=True, blank=True)
    purchase_price  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dispensed_to    = models.CharField(max_length=200, blank=True)
    prescription_no = models.CharField(max_length=100, blank=True)
    notes           = models.TextField(blank=True)
    reference_no    = models.CharField(max_length=100, blank=True)
    performed_by    = models.ForeignKey(
                          User, on_delete=models.SET_NULL,
                          null=True, blank=True, related_name='stock_movements')
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.get_movement_type_display()} — "
                f"{self.medicine.medicine_name} ({self.quantity:+d})")

    @property
    def is_stock_in(self):
        return self.movement_type in ('in', 'return')

    @property
    def is_stock_out(self):
        return self.movement_type in ('out', 'expired', 'damaged')

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'


# ─────────────────────────────────────────────────────────────────────────────
# DISPENSING  (transaction header)
# ─────────────────────────────────────────────────────────────────────────────
class Dispensing(models.Model):
    """
    One record per dispensing transaction (the receipt).
    Each transaction can have multiple DispensingItem rows.
    Stock is deducted via StockMovement('out') — no conflict with stock management.
    """
    customer_name   = models.CharField(max_length=200, blank=True)
    prescription_no = models.CharField(max_length=100, blank=True)
    notes           = models.TextField(blank=True)
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_amount    = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pharmacist      = models.ForeignKey(
                          User, on_delete=models.SET_NULL,
                          null=True, blank=True, related_name='dispensings')
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dispensing #{self.pk} — ₱{self.total_amount} ({self.created_at.date()})"

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'Dispensing Transaction'
        verbose_name_plural = 'Dispensing Transactions'


# ─────────────────────────────────────────────────────────────────────────────
# DISPENSING ITEM  (one per medicine line in a transaction)
# ─────────────────────────────────────────────────────────────────────────────
class DispensingItem(models.Model):
    """
    Individual line item inside a Dispensing transaction.
    unit_price is snapshotted at time of sale so price changes don't affect history.
    """
    dispensing  = models.ForeignKey(
                      Dispensing, on_delete=models.CASCADE, related_name='items')
    medicine    = models.ForeignKey(
                      Medicine, on_delete=models.PROTECT, related_name='dispensing_items')
    quantity    = models.PositiveIntegerField()
    unit_price  = models.DecimalField(max_digits=10, decimal_places=2)   # snapshot
    subtotal    = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return (f"{self.medicine.medicine_name} x{self.quantity} "
                f"@ ₱{self.unit_price}")

    class Meta:
        verbose_name        = 'Dispensing Item'
        verbose_name_plural = 'Dispensing Items'