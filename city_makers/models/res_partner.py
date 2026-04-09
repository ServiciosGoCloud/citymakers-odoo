from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_vortex_sector = fields.Char(string='Sector')
    x_vortex_linkedin_corp = fields.Char(string='LinkedIn Empresa')
    x_vortex_decisor = fields.Char(string='Nombre Decisor')
    x_vortex_linkedin_pers = fields.Char(string='LinkedIn Personal')
    x_vortex_comentarios = fields.Text(string='Comentarios de Contacto')
    x_vortex_tamano = fields.Selection([
        ('1-50', '1-50 empleados'),
        ('51-200', '51-200 empleados'),
        ('201-500', '201-500 empleados'),
        ('500+', 'Más de 500 empleados')
    ], string='Tamaño Estimado')
    x_vortex_tipo_empresa = fields.Selection([
        ('consolidada', 'Empresa Consolidada'),
        ('extranjera', 'Empresa Extranjera ya Establecida'),
        ('startup', 'Startup / Scaleup')
    ], string='Tipo de Empresa')
    x_vortex_clasificacion = fields.Selection([
        ('a', 'Clasificación A'),
        ('b', 'Clasificación B')
    ], string='Clasificación A/B')