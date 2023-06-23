{
    'name': 'Metafoor Media Video',
    'version': '0.0.1',
    'summary': 'Metafoor Media Customizations',
    'sequence': 5,
    'description': 'Several customizations on Odoo to improve the Business Case off Metafoor Media.',

    'author': 'Harry Nijkamp',
    'company': 'Metafoor Media BV',
    'website': 'www.metafoormedia.nl',
    'category': 'Customization',
    'depends': ['base', 'mail'],
    
    'icon': 'static/description/icon.png',

    'data': [
        'views/views.xml',
        'views/res_partner_tree.xml',
        'views/res_partner_view.xml'
    ],
    
    'application': True,
}