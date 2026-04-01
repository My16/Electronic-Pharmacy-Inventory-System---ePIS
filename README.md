"# Electronic Pharmacy Inventory System (ePIS)

[![Django](https://img.shields.io/badge/Django-5.2.5-darkgreen)]()
[![Python](https://img.shields.io/badge/Python-3.8+-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

A comprehensive **Django-based pharmacy inventory management system** designed to streamline pharmacy operations with medicine inventory tracking, stock management, supplier coordination, and detailed reporting.

---

## 🏥 Features

### 📊 Dashboard & Analytics
- **Real-time Overview**: Track total medicines, low stock alerts, expiring medications (within 90 days)
- **Sales Analytics**: Daily, weekly, and monthly revenue tracking
- **Key Metrics**: Monitor stock value, total sales, upcoming expirations
- **Visual Charts**: Data visualization for better insights

### 💊 Inventory Management
- **Add/Edit/Delete Medicines**: Comprehensive medicine database with multiple dosage forms
- **Stock Tracking**: Real-time stock levels and quantity management
- **Barcode Support**: Quick lookup using medicine barcodes
- **Batch Management**: Track medicine batches and expiry dates
- **Automated Alerts**: Low stock and expiration warnings

### 📦 Stock Management
- **Stock In**: Receive medicines from suppliers with batch tracking
- **Stock Out**: Dispense medicines with automatic inventory reduction
- **Stock Adjustments**: Manual adjustments for inventory corrections
- **Movement History**: Complete audit trail of all stock movements

### 💰 Dispensing & Sales
- **Point of Sale (POS)**: Create and manage medicine sales
- **Digital Receipts**: Generate receipts with transaction details
- **Multi-item Orders**: Support multiple medicines per transaction
- **Payment Tracking**: Record and manage payments

### 👥 Supplier Management
- **Supplier Database**: Maintain supplier contact and delivery information
- **Contact Details**: Phone, email, address management
- **Activity Tracking**: Purchase history and interactions
- **Status Management**: Active/inactive supplier toggling

### 👤 User Management
- **Role-Based Access Control**: Admin, Staff, and User roles
- **User Profiles**: Extended user information with avatars
- **Authentication**: Secure login and session management
- **Permission Management**: Fine-grained access control

### 📄 Reporting & Exports
- **Excel Exports**: Generate comprehensive inventory reports in Excel format
- **PDF Reports**: Create printable pharmacy reports and receipts
- **Custom Formatting**: Professional styling for documents
- **Multiple Report Types**: Inventory, sales, and movement reports

---

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (Default) / PostgreSQL compatible
- **Frontend**: HTML5, CSS3, JavaScript
- **Libraries & Tools**:
  - `django-widget-tweaks`: Enhanced form rendering
  - `openpyxl`: Excel file generation
  - `reportlab`: PDF generation
  - `qrcode`: QR code generation
  - `pandas`: Data analysis and export
  - `Pillow`: Image processing

---

## 📁 Project Structure

```
Pharmacy-System-Project/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── db.sqlite3                     # SQLite database
│
├── PharmacySystem/                # Main Django project settings
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # Main URL router
│   ├── asgi.py                   # ASGI configuration
│   └── wsgi.py                   # WSGI configuration
│
└── PharmaSys/                     # Django application
    ├── models.py                 # Database models
    ├── views.py                  # Business logic & views
    ├── forms.py                  # Django forms
    ├── urls.py                   # App URL routing
    ├── admin.py                  # Django admin setup
    ├── apps.py                   # App configuration
    │
    ├── migrations/               # Database migrations
    ├── static/                   # CSS, JavaScript, images
    │   ├── css/
    │   ├── js/
    │   └── forms/
    └── templates/                # HTML templates
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository** (or navigate to the project)
   ```bash
   cd Pharmacy-System-Project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a superuser** (admin account)
   ```bash
   python manage.py createsuperuser
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Application: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`

---

## 📖 Usage Guide

### Authentication
- Log in with your superuser credentials
- First-time users can register or be created by administrators
- Role assignment available in admin panel

### Dashboard
- View real-time pharmacy metrics upon login
- Monitor stock levels and upcoming expirations
- Review sales trends and revenue

### Managing Medicines
1. Navigate to **Inventory** → **Add Medicine**
2. Fill in medicine details (name, generic name, category, dosage form)
3. Set pricing and stock information
4. Save and manage from the inventory list

### Stock Operations
1. **Stock In**: Receive medicines from suppliers
   - Go to **Stock** → **Stock In**
   - Select supplier and add medicines
   
2. **Stock Out**: Dispense medicines
   - Go to **Stock** → **Stock Out**
   - Select medicines and update quantities

3. **Adjustments**: Correct inventory discrepancies
   - Go to **Stock** → **Adjust Stock**
   - Specify reason for adjustment

### Processing Sales
1. Navigate to **Dispensing** → **Create Sale**
2. Search and add medicines
3. Confirm quantities and prices
4. Complete transaction and generate receipt

### Managing Suppliers
1. Go to **Suppliers** section
2. Add new suppliers with contact details
3. Track supplier history and activity

### Generating Reports
- Use export features available on dashboard and inventory pages
- Generate Excel or PDF reports for analysis and record-keeping

---

## 🔐 User Roles

| Role | Permissions |
|------|------------|
| **Admin** | Full system access, user management, settings |
| **Staff** | Inventory, stock, dispensing, reporting |
| **User** | Limited access, view-only permissions |

---

## 📋 Database Models

### Key Models
- **UserProfile**: Extended user information with roles
- **Medicine**: Pharmacy medicines with dosage forms and pricing
- **MedicineCategory**: Classification of medicines
- **Supplier**: Medicine supplier information
- **StockMovement**: Track all inventory changes
- **Dispensing**: Sales transactions
- **DispensingItem**: Individual items in dispensing records

---

## 🎨 Main Features Breakdown

| Feature | Location | Access |
|---------|----------|--------|
| Dashboard | `/dashboard/` | All authenticated users |
| Inventory Management | `/inventory/` | Staff & Admin |
| Stock Management | `/stock/` | Staff & Admin |
| Dispensing/POS | `/dispensing/` | Staff & Admin |
| Supplier Management | `/suppliers/` | Admin |
| User Management | `/users/` | Admin |
| Reports & Exports | Dashboard & Pages | Staff & Admin |

---

## 🔧 Configuration

### Settings File
Located in `PharmacySystem/settings.py`:
- Database configuration
- Installed apps
- Middleware settings
- Static files and media configuration
- Email settings (if needed)

### Environment Variables (Optional)
Consider using `.env` file for sensitive information:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 📦 Dependencies Summary

Key dependencies included:
- **Django 5.2.5** - Web framework
- **psycopg2** - PostgreSQL adapter
- **openpyxl** - Excel generation
- **reportlab** - PDF creation
- **pandas** - Data analysis
- **qrcode** - QR code generation
- **pillow** - Image processing

See `requirements.txt` for complete list.

---

## 🐛 Troubleshooting

### Database Errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

---

## 📝 Notes

- Ensure proper backup of `db.sqlite3` before major changes
- Use PostgreSQL for production environments
- Regularly update dependencies
- Test reports before production use

---

## 📄 License

This project is provided as-is for educational and professional use.

---

## 🤝 Contributing

Contributions and improvements are welcome! Please:
1. Test your changes thoroughly
2. Maintain code quality
3. Document any new features
4. Submit detailed pull requests

---

## ⚠️ Disclaimer

This system is designed for pharmacy inventory management. Ensure compliance with local pharmaceutical regulations and data protection laws before deployment.

---

**Last Updated**: April 2026  
**Version**: 1.0.0" 
