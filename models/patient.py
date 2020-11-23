from odoo import models,fields,api
class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = 'first_name'
    first_name=fields.Char(string="First Name",required=True)
    last_name=fields.Char(string="Last Name",required=True)
    birth_date=fields.Date()
    history=fields.Html()
    cr_ratio=fields.Float(string="CR Ratio",required=True)
    blood_type=fields.Selection([("A","Group A"),("B","Group B")
                                    ,("O","Group O"),("AB","Group B")])
    p_c_r=fields.Boolean()
    image=fields.Binary(string="Upload Image")
    address=fields.Text()
    age=fields.Integer()
    department_id=fields.Many2one('hms.department' )
    doctor_id=fields.Many2many('hms.doctors')
    dep_capcity=fields.Integer(related='department_id.capcity',string="department capcity")
    history_id=fields.One2many("history.patient.line","patient_id")
    status=["Undetermined","Good","Fair", "Serious"]

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.p_c_r=True
            return {
                'warning': {
                    'title': "PCR Checked",
                    'message': "PCR automatically checked",
                }
            }




class HistoryPatientLine(models.Model):
    _name = 'history.patient.line'
    description=fields.Char()
    patient_id=fields.Many2one("hms.patient",readonly=True,invisible=True)



