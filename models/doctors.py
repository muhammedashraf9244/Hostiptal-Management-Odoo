from odoo import models,fields

class HmsDoctors(models.Model):
    _name = 'hms.doctors'
    _rec_name = 'first_name'
    first_name = fields.Char(string="first name", required=True)
    last_name = fields.Char(string="last name", required=True)
    image=fields.Binary(string="Upload Image")
    patient_ids=fields.One2many('hms.patient','doctor_id')
