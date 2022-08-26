
{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'This is Hospital Management System',
    'description': """
    This is Hospital Management System.
    """,
    'sequence':-500,
    'depends': ['base'],
    'data': ['security/ir.model.access.csv',
    'views/menu.xml',
    'views/Patient.xml',
    'views/Doctor.xml',
    'views/Speciality.xml',
    'views/City.xml',
    'views/Appointment.xml',],
    'installable':True,
    'auto_install':False,
    'images':['static/description/icon.png'],
    'application':True,
    'license': 'LGPL-3',
}