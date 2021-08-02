from odoo import fields, models, api

class ToDoList(models.Model):
    _name = 'todolist'

    name = fields.Char(string='Nội dung công việc phải làm')
    state = fields.Selection(
        selection=[('0', 'Đang thực hiện'), ('1', 'Hoàn thành'), ('2', 'Tạm dừng'), ('3', 'Đã hủy')], string='Trạng thái')

    linhvuc = fields.Selection(
        selection=[('0', 'Tiếng Trung'), ('1', 'Tiếng Nhật'),
                   ('2', 'Tiếng Anh'), ('3', 'Tiếng Hàn'),
                   ('4', 'Chuyên môn ở CQ'), ('5', 'Lập trình')], string='Lĩnh vực')
