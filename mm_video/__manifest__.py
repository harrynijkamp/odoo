{
    'name': 'Metafoor Media Video',
    'version': '0.0.1',
    'summary': 'Metafoor Media Custom Video Module',
    'sequence': 5,
    'description': '',

    'author': 'Harry Nijkamp',
    'company': 'Metafoor Media BV',
    'website': 'www.metafoormedia.nl',
    'category': 'Customization',
    'depends': ['base', 'project', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/video.xml',
        
    ],
    'application': True,
}