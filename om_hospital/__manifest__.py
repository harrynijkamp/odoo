{
    'name': 'Hospital Management Server',
    'version': '1.0.0',
    'summary': 'Hospital Management Software',
    'sequence': 5,
    'description': '',

    'author': 'Harry Nijkamp',
    'company': 'Metafoor Media BV',
    'website': 'www.metafoormedia.nl',
    'category': 'Customization',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/sales_order.xml',
    ],
    'application': True,
}