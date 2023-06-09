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
    'assets': {
        'web.assets_backend': [
            '/mm_video/static/src/js/scripts.js',
        ],
        'web.assets_common': [
            
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/video.xml',
        'views/project_edit.xml',
        'views/partner_form.xml',
    ],
    
    'application': True,
}