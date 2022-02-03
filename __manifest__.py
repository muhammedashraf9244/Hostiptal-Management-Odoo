{
    'name': "Hms",
    'summary': "Hms is a module for record patients ",
    'description': '''Hms is a module for record patients''',
    'author': "MuhammedAshraf",
    'company': "ITI",
    'website': "https://github.com/muhammedashraf9244/Hostiptal-Management-Odoo",
    'version': "13.0",
    'data': [
        'security/hms_security.xml',
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctors_view.xml',
        'views/department_view.xml',
        'views/crm_inherit_view.xml',
        'reports/patient_template.xml',
        'reports/report_view.xml',
    ],
    'depends': ['base', 'crm'],

}
