
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
    'wizard/ChangeAppointment.xml',
    'views/menu.xml',
    'views/Patient.xml',
    'views/Doctor.xml',
    'views/Speciality.xml',
    'views/City.xml',
    'views/Appointment.xml',
    'views/Pharma.xml',
    'views/Prescription.xml',
    'views/Labtest.xml',
    'views/Bill.xml'],
    'installable':True,
    'auto_install':False,
    'images':['static/description/icon.png'],
    'application':True,
    'license': 'LGPL-3',
}