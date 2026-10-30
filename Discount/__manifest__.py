{
    'name': 'Product Master MRP Discount Calculator',
    'version': '16.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Calculates discounted sales price based on MRP and discount percentage.',
    'author': 'Felix Kumar',
    'website': 'https://yourwebsite.com',
    
    # --- PRICING & SELLING CONFIGURATION ---
    'price': 19.00,                 # Set your price in EUR/USD (e.g., 19.00)
    'currency': 'EUR',              # Currency: 'EUR' or 'USD'
    'license': 'OPL-1',             # Required license for paid Odoo modules
    
    'depends': ['product', 'sale'],
    'data': [
        'views/product_template_views.xml',
    ],
    'images': ['static/description/banner.png'], # Recommended thumbnail for store page
    'installable': True,
    'application': True,
}
