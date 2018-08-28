# -*- coding: utf-8 -*-

from openerp import models, fields, api


class affichageDevis(models.Model):
    _inherit = "sale.order"

    def action_button_confirm(self, cr, uid, ids, context=None):
        if not context:
            context = {}
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        self.signal_workflow(cr, uid, ids, 'order_confirm')
        if context.get('send_email'):
            self.force_quotation_send(cr, uid, ids, context=context)
        # self.updateQuotation()
        # def updateQuotation(self):
        so = self.pool.get('sale.order').browse(cr,uid,ids)
        amount = so.amount_untaxed
        opportunity = self.pool.get('crm.lead')
        var = "sale.order,"+str(ids[0])
        up = opportunity.search(cr,uid,[("ref","=",var)])
        if up:
            obj = opportunity.browse(cr,uid,up)
            obj.update({'planned_revenue':amount})
        return True

    # @api.multi





# print "RAKOTO"
