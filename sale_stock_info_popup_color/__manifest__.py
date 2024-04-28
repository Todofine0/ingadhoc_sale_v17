{
    'name': 'Sale Stock Info Pop-up Color',
    'version': "17.0.1.2.0",
    'category': 'Sales',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'sale_stock',
    ],
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'sale_stock_info_popup_color/static/src/**/*',
            ('remove', 'sale_stock_info_popup_color/static/src/legacy/**/*'),
        ],
        "web.assets_backend_legacy_lazy": [
            'sale_stock_info_popup_color/static/src/legacy/**/*',
        ]
    },
    'demo': [
    ],
    'installable': False,
    'auto_install': False,
    'application': False,
}
