{
        'name': "School Management",
        'summary': "School Management Software",
        'description': "Treating Schools",
        'author': "MyCompany",
        'website': "www.youcompany",
        'category': "Tools",
        'version': '16.0.1.0.0',
        'post_init_hook': "create_student",
        'depends': ['base', 'contacts'],
        'data': [
            'secturity/ir.model.access.csv',
            'views/school.xml',
        ],

        'assets': {
            'web.assets_backend': [
                'school_management/static/src/js/test.js'
            ],
        },
        'demo': [],
        'images': ['static/description/icon.png'],
        'installable': True,
        'application': True,
        'auto_install': False
}