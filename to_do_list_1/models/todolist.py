from odoo import fields, models, api

class ToDoList(models.Model):
    _name = 'todolist'

    ngay_batdau = fields.Date(string='Ngày bắt đầu công việc')
    name = fields.Text(string='Nội dung công việc phải làm')
    ketqua = fields.Char(string='Kết quả thực hiện')
    state = fields.Selection(
        selection=[('0', 'Đang thực hiện'), ('1', 'Hoàn thành'), ('2', 'Tạm dừng'), ('3', 'Đã hủy')], string='Trạng thái')

    linhvuc = fields.Selection(
        selection=[('0', 'Tiếng Trung'), ('1', 'Tiếng Nhật'),
                   ('2', 'Tiếng Anh'), ('3', 'Tiếng Hàn'),
                   ('4', 'Chuyên môn ở CQ'), ('5', 'Lập trình')], string='Lĩnh vực')
