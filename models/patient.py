from odoo import models,fields,api
from odoo.exceptions import UserError
import re
from datetime import  datetime
class HmsPatient(models.Model):
    _name = "hms.patient"
    _rec_name = 'first_name'
    first_name=fields.Char(string="First Name",required=True)
    last_name=fields.Char(string="Last Name",required=True)
    email = fields.Char()
    birth_date=fields.Date()
    age= fields.Integer(compute="get_age",store=True)
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
    state = fields.Selection([
        ('undetermined','Undetermined'),('good','Good'),('fair','Fair'),('serious','Serious')
    ],default='undetermined')


    _sql_constraints = [
        ("Invalid email","unique(email)","This email is already exits")
    ]

    @api.constrains("email")
    def check_email(self):
        if self.email:
            my_pattern = r'^[a-zA-Z0-9\.]+@[a-z0-9]+\.(com|org|net)$'
            is_match = re.match(my_pattern,self.email)
            if not is_match:
                raise UserError(f'This email {self.email} is Invalid')

    # Action of buttons of state
    def set_good(self):
        for record in self:
            record.state = 'good'

    def set_fair(self):
        for record in self:
            record.state = 'fair'
    def set_serious(self):
        for record in self:
            record.state = 'serious'

    def back_to_undetermined(self):
        for record in self:
            record.state = 'undetermined'


    # compute age
    @api.onchange("birth_date")
    def get_age(self):
        for record in self:
            if record.birth_date:
                # print(str(record.birth_date))
                # convert date type to datetime
                birth_date_time = datetime.strptime(str(record.birth_date), "%Y-%m-%d")
                # print(birth_date_time)
                # calc differance between two dates
                record.age =abs((birth_date_time - datetime.now()).days) // 365


    @api.constrains('state')
    def write_new_log(self):
        for record in self:
            record.env['history.patient.line'].create({'patient_id':record.id,
                                                 'description':f'Add new state {record.state}'})

    @api.onchange('age')
    def _onchange_age(self):
        for record in self:
            if record.age==0:
                return
            elif record.age < 30:
                record.p_c_r=True
                return {
                    'warning': {
                        'title': "PCR Checked",
                        'message': "PCR automatically checked",
                    }
                }
            elif record.age >= 30:
                record.p_c_r=False
                return




class HistoryPatientLine(models.Model):
    _name = 'history.patient.line'
    description=fields.Char()
    patient_id=fields.Many2one("hms.patient",readonly=True,invisible=True)



class CrmInheritPartner(models.Model):
    _inherit = 'res.partner'
    related_user_id = fields.Many2one('hms.patient')

    @api.constrains("email")
    def check_email(self):
        for record in self:
            email_patient = record.env['hms.patient'].search([('email','=',record.email)])
            if email_patient:
                raise UserError(f'This email {record.email} is exits in patients ')

    # @api.multi is deprcated in odoo 13 so when use nlink use with for each element
    def unlink(self):
        for record in self:
            if record.related_user_id:
                raise UserError(f'Be ware this customer related with patient name {record.related_user_id.first_name}')
        return super(CrmInheritPartner, self).unlink()