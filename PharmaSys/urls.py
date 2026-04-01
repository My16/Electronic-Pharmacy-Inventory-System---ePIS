# urls.py
from django.urls import path
from . import views

urlpatterns = [

    # ── Auth ──────────────────────────────────────────────────────────────────
    path('',        views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ── Dashboard ─────────────────────────────────────────────────────────────
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # ── Inventory ─────────────────────────────────────────────────────────────
    path('inventory/',                       views.inventory_view,          name='inventory'),
    path('inventory/add/',                   views.inventory_add_view,      name='inventory_add'),
    path('inventory/edit/<int:pk>/',         views.inventory_edit_view,     name='inventory_edit'),
    path('inventory/delete/<int:pk>/',       views.inventory_delete_view,   name='inventory_delete'),
    path('inventory/barcode/',               views.inventory_barcode_lookup,name='inventory_barcode'),
    path('inventory/stock-adjust/<int:pk>/', views.inventory_stock_adjust,  name='inventory_stock_adjust'),

    # ── Category Management (AJAX) ─────────────────────────────────────────────
    path('api/category-search/', views.category_search_ajax,  name='category_search_ajax'),
    path('api/category-create/', views.category_create_ajax,  name='category_create_ajax'),

    # ── Medicine search (AJAX) ────────────────────────────────────────────────
    path('api/medicine-search/', views.medicine_search_ajax, name='medicine_search_ajax'),

    # ── Stock Management ──────────────────────────────────────────────────────
    path('stock/',               views.stock_management_view, name='stock_management'),
    path('stock/in/',            views.stock_in_view,         name='stock_in'),
    path('stock/out/',           views.stock_out_view,        name='stock_out'),
    path('stock/adjust/',        views.stock_adjust_view,     name='stock_adjust'),
    path('stock/medicine-info/', views.stock_medicine_info,   name='stock_medicine_info'),

    # ── Dispensing / Sales ────────────────────────────────────────────────────
    path('dispensing/',                     views.dispensing_view,    name='dispensing'),
    path('dispensing/create/',              views.dispensing_create,  name='dispensing_create'),
    path('dispensing/receipt/<int:pk>/',    views.dispensing_receipt, name='dispensing_receipt'),

    # ── Suppliers ─────────────────────────────────────────────────────────────
    path('suppliers/',                    views.suppliers_view,        name='suppliers'),
    path('suppliers/add/',                views.supplier_add_view,     name='supplier_add'),
    path('suppliers/edit/<int:pk>/',      views.supplier_edit_view,    name='supplier_edit'),
    path('suppliers/delete/<int:pk>/',    views.supplier_delete_view,  name='supplier_delete'),
    path('suppliers/toggle/<int:pk>/',    views.supplier_toggle_view,  name='supplier_toggle'),
    path('suppliers/detail/<int:pk>/',    views.supplier_detail_view,  name='supplier_detail'),

    # ── User Management ───────────────────────────────────────────────────────
    path('users/',                   views.user_management_view,    name='user_management'),
    path('users/add/',               views.user_add_view,           name='user_add'),
    path('users/edit/<int:pk>/',     views.user_edit_view,          name='user_edit'),
    path('users/delete/<int:pk>/',   views.user_delete_view,        name='user_delete'),
    path('users/toggle/<int:pk>/',   views.user_toggle_active_view, name='user_toggle_active'),

    # ── Settings ──────────────────────────────────────────────────────────────
    path('settings/', views.settings_view, name='settings'),

    # ── Reports ───────────────────────────────────────────────────────────────
    path('reports/',              views.reports_view,        name='reports'),
    path('reports/export/excel/', views.report_export_excel, name='report_export_excel'),
    path('reports/export/pdf/',   views.report_export_pdf,   name='report_export_pdf'),
]