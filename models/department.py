from odoo import models,fields

class HmsDepartment(models.Model):
    _name = 'hms.department'
    name = fields.Char(string="name", required=True)
    capcity=fields.Integer()
    is_open=fields.Boolean()
    patient_ids=fields.One2many('hms.patient','department_id')
