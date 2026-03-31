{
    'name': 'City Makers Odoo CRM & Contacts',
    'version': '1.1',
    'depends': ['base', 'contacts', 'crm'], # Agregamos 'crm'
    'data': [
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml', # Archivo nuevo
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}