{
    'name': 'Purchase Order Line View',
    'version': '17.0',
    'summary': """
    Access purchase order lines and RFQs through various intuitive views.
    """,
    'description': """
✔ View Purchase Orders and RFQ Order Lines in a centralized interface.
✔ Includes Tree, Kanban, Calendar, Pivot, and Graph views.
✔ Effortlessly navigate between different perspectives for better visualization and analysis.

""",
    'category': 'Purchases',
    'sequence': 1,
    'author': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com/',
    'license': 'LGPL-3',
    'price': 24.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_line_view.xml',
        'views/rfq_line_view.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
