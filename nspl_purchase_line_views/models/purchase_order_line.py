from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_image = fields.Binary(
        related="product_id.image_1920",
        string="Image")

    @api.onchange('order_id')
    def onchange_order_id(self):
        if self.order_id.state in ['cancel', 'done', 'purchase']:
            raise UserError(_("You cannot select purchase order in "
                              "cancel or locked or purchase order state"))
