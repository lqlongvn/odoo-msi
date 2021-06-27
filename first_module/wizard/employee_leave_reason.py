from odoo import fields, models, api

class EmployeeLeaveReason(models.TransientModel):
    _name = 'employee.leave.reason'

    reason = fields.Selection(
        selection=[('1', 'Nghi Thai San'), ('2', 'Nghi Phep'), ('3', 'Nghi Viec')], string='Reason')

    def update_leave_reason(self):
        employee_id = self.env.context.get('active_id', False)
        employee_record = self.env['employee'].browse(employee_id)
        employee_record.write({'state': self.reason})
        return True

