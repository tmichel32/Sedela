# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'opportunity.wizard'

    # Recherche du stage qui est gagné
    @api.multi
    def stageGagner(self):
        obj = self.env['crm.case.stage']
        vals = obj.search([('probability','=','100')])
        if vals:
            return vals[0].id

    @api.multi
    def rearranger(self):
        opportunity = self.env['crm.lead']
        vals = opportunity.search([('ref','!=',False),('stage_id','!=',self.stageGagner())])
        if vals:
            for v in vals:
                v.update({'stage_id':self.stageGagner()})
        # vals = opportunity.search([('ref','!=',False)])
        # if vals:
        #     for v in vals:
        #         v.update({'planned_revenue':v.ref.amount_untaxed})
