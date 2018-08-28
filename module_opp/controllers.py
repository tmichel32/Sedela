# -*- coding: utf-8 -*-
from openerp import http

# class ModuleOpp(http.Controller):
#     @http.route('/module_opp/module_opp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_opp/module_opp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_opp.listing', {
#             'root': '/module_opp/module_opp',
#             'objects': http.request.env['module_opp.module_opp'].search([]),
#         })

#     @http.route('/module_opp/module_opp/objects/<model("module_opp.module_opp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_opp.object', {
#             'object': obj
#         })