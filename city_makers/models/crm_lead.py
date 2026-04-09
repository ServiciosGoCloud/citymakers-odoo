from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Campos que movimos del contacto al CRM
    x_vortex_complejidad = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta')
    ], string='Nivel de Complejidad')

    x_vortex_estado_comercial = fields.Selection([
        ('no_contactado', 'No contactado'),
        ('email_1', 'Email 1 enviado'),
        ('en_seguimiento', 'En seguimiento'),
        ('interesado', 'Interesado'),
        ('descartado', 'Descartado')
    ], string='Estado Comercial')

    # Campos "Espejo" del Contacto (Lectura únicamente)
    # partner_id es el campo nativo de Odoo para el Cliente/Contacto en CRM
    x_vortex_partner_sector = fields.Char(related='partner_id.x_vortex_sector', string='Sector (Contacto)', readonly=True)
    x_vortex_partner_linkedin = fields.Char(related='partner_id.x_vortex_linkedin_corp', string='LinkedIn Corp (Contacto)', readonly=True)
    x_vortex_partner_tamano = fields.Selection(related='partner_id.x_vortex_tamano', string='Tamaño (Contacto)', readonly=True)