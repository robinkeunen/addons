# -*- coding: utf-8 -*-

from openerp import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    analytic_account_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account',
        company_dependent=True,
        domain=[('account_type', '!=', 'closed')])