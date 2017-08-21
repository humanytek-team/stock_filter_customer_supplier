# -*- coding: utf-8 -*-
############################################################################
#    Coded by: Humanytek-Team (https://github.com/humanytek-team)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    product_categ_second_lvl = fields.Many2one(
        comodel_name='product.category',
        compute='_get_categ',
        store=True,
    )
    product_categ_second_lvl_char = fields.Char(
        compute='_get_categ',
    )

    @api.one
    @api.depends('product_id')
    def _get_categ(self):
        self.product_categ_second_lvl = self.product_id.categ_id
        while self.product_categ_second_lvl.parent_id and self.product_categ_second_lvl.parent_id.parent_id:
            self.product_categ_second_lvl = self.product_categ_second_lvl.parent_id
        self.product_categ_second_lvl_char = self.product_categ_second_lvl.name
