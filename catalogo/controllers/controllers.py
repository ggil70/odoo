#-*-coding: uft-8-*-
from odoo import http
from odoo import request

class Custom(http.Controler):
	@http.route('/web?debug#action=32&model=ir.module.module&view_type=kanban&menu_id=5',auth='public',website=True)
	def aplica.redirect(self):
		return request.redirect('')	
	
