from odoo import models,fields

class HmsPatient(models.Model):
    _name = "hms.patient"
    first_name=fields.Char(string="First Name",required=True)
    last_name=fields.Char(string="Last Name",required=True)
    birth_date=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float(string="CR Ratio")
    blood_type=fields.Selection([("A","Group A"),("B","Group B")
                                    ,("O","Group O"),("AB","Group B")])
    p_c_r=fields.Boolean()
    image=fields.Binary(string="Upload Image")
    address=fields.Text()
    age=fields.Integer()
    department_id=fields.Many2one('hms.department')
    doctor_id=fields.Many2one('hms.doctors')
    dep_capcity=fields.Integer(related='department_id.capcity',string="department capcity")

