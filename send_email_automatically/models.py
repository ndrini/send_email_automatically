# -*- coding: utf-8 -*-
from openerp import models, fields, api

class res_partner(models.Model):
    _inherit = 'account.analytic.account'

    @api.multi
    def send_email_with_contract(self):
        '''
        This function opens a window to compose an email, with the template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False

        # In Odoo 9 'mail.template'
        # template_id = self.env['email.template'].search([('name', '=', 'Contract send by e-mail template')], limit=1)

        template_id = self.env['email.template'].search([('name', '=', 'Invoice - Send by Email')], limit=1)

        


        ctx = dict()
        ctx.update({
            'default_model': 'res.partner',
            'default_res_id': False,
            'default_use_template': True,
            'default_template_id': template_id.id or False,
            'default_composition_mode': 'comment',
            'skip_notification': True,
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
            }