
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
# Generated by the OpenERP plugin for Dia !
# from osv import fields,osv --- <8.0.X
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date, datetime,timedelta
from odoo import api
from time import time
formatter_string = "%d-%m-%y" 
#from tools.translate import_
#from odoo import tools
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#Importamos la libreria logger
import logging
#Definimos la Variable Global
codigo_ad = ''
_logger = logging.getLogger(__name__)




############################################### Registro de Polizas de Seguro #################################################################################################





class cobertura(models.Model):
     """Registra la Cobertura de la Poliza de Seguro"""
     _name = 'cobertura'
     #_rec_name = 'cobertura_codigo'
     _rec_name = 'cobertura_nombre'
    
     cobertura_codigo   = fields.Char(string='Codigo de la Cobertura',size=3,required=True, help='Registra el Codigo del tipo de Cobertura')
     cobertura_nombre   = fields.Char(string='Nombre de la Cobertura',size=100,required=True, help='Registra la descripcion de la Cobertura de la Poliza')
    
     _sql_constraints = [('cobertura_codigo', 'unique(cobertura_codigo)', 'El Código debe se único!')]  
     _sql_constraints = [('cobertura_nombre', 'unique(cobertura_nombre)', 'El Nombre  debe se único!')]  


class aseguradoras(models.Model):
     """Registra las Compañías Aseguradoras"""
     _name = 'aseguradoras'
     _rec_name = 'aseguradoras_nombre'
     #_rec_name = 'aseguradoras_codigo'
    
     aseguradoras_nombre = fields.Char(string='Nombre de la Aseguradora segun Sudebip',size=100,required=True, help='Registra el nombre de la Compañia aseguradora')
     aseguradoras_codigo = fields.Char(string='Codigo de la Aseguradora segun Sudebip',size=5, required=True,help='Registra el Codigo de la Aseguradora')
    

     _sql_constraints = [('aseguradoras_codigo', 'unique(aseguradoras_codigo)', 'El Código debe se único!')]  
     _sql_constraints = [('aseguradoras_nombre', 'unique(aseguradoras_nombre)', 'El Nombre debe se único!')]  


class poliza(models.Model):
     """Registra el detalle de la Poliza de Seguro"""
     _name = 'poliza'
     _rec_name = 'poliza_numero'
     #_rec_name = 'poliza_numero'
     #_rec_name = 'aseguradoras_id'
     #_rec_name = 'poliza_tipo'
     #_rec_name = 'poliza_monto'
     #_rec_name = 'poliza_fecha_ini'
     #_rec_name = 'ploza_fecha_fin'
     #_rec_name = 'poliza_respon_civil'
     #_rec_name = 'cobertura_id'
    
     poliza_codigo        = fields.Char(string='Codigo de la Poliza',size=3,required=True, help='Registra el Codigo de la Poliza')
     poliza_numero        = fields.Char(string='Numero de la Poliza',size=40,required=True, help='Registra el Número de la Poliza')
     aseguradoras_id      = fields.Many2one('aseguradoras',string='Codigo de la Aseguradora',size=3,required =True, help='Registra el Codigo de Vinculacion con La Aseguradora del Bien')
     aseguradoras_codigo  = fields.Char(string='Codigo de la Aseguradora segun Sudebip',size=5, required=True,help='Registra el Codigo de la Aseguradora')
     poliza_tipo          = fields.Selection([('1','Individual'),('2','Colectiva')],string='Tipo de Poliza',size=1,required=True, help='Registra el Tipo de Poliza N nacional I internacional')
     poliza_monto         = fields.Float(string='Monto Asegurado',required=True, help='Registra el Monto de la Poliza')
     poliza_fecha_ini     = fields.Date(string='Fecha de Inicio de la Poliza',size=8,required=True, help='Registra la Fecha de Inicio de la Poliza')
     poliza_fecha_fin     = fields.Date(string='Fecha Fin de la Poliza',size=8,required=True, help='Registra la Fecha de Finzalizacion de la Poliza')
     poliza_respon_civil  = fields.Selection([('S','Si'),('N','No')],string='Pose Responsabilidad Civil',size=1, help='Registra si la poliza tiene  Seguro de Responsabiliad Civil Si ,No')
     cobertura_id         = fields.Many2one('cobertura',string='Tipo de Cobertura', help='Registra el Codigo de Vinculacion con el Tipo de Cobertura')
     codigo_cobertura     = fields.Char(string='Codigo tipo de Cobertura de la Poliza',size=40,required=True, help='Registra el Codigo  del tipo de Cobertura de la Poliza')

     otro_tipo_cobertura   = fields.Char(string='Otro Tipo de Cobertura de la Poliza',size=40, help='Registra el Otro tipo de Cobertura de la Poliza')
     descrip_otra_cobertura   = fields.Char(string='Descripción del Otro Tipo de Cobertura de la Poliza',size=100, help='Registra la Descripción del Otro tipo de Cobertura de la Poliza')

     _sql_constraints = [('poliza_codigo', 'unique(poliza_codigo)', 'El Código debe se único!')]  

     @api.onchange('cobertura_id')
     def onchange_cobertura(self):
        codigo= ''
        codigo = self.cobertura_id.cobertura_codigo
        self.codigo_cobertura =  codigo 

  
     @api.onchange('aseguradoras_id')
     def onchange_aseguradora(self):
        codigo= ''
        codigo = self.aseguradoras_id.aseguradoras_codigo
        self.aseguradoras_codigo =  codigo 


    

     @api.onchange('poliza_fecha_fin')
     def onchange_poliza_fecha_fin(self):
        if (str(self.poliza_fecha_ini) > str(self.poliza_fecha_fin)):
            raise ValidationError('La Fecha de Inicio no puede ser mayor que la de finalización!')






























############################################Estatus del Bien SUDEBIP#############################################################
class estatus_uso(models.Model):
    """Registra el estatus de uso que tiene el Bien"""
    _name = 'estatus_uso'
    #_rec_name = 'estatus_uso_codigo'
    _rec_name = 'estatus_uso_nombre'
    
    estatus_uso_codigo = fields.Char(string='Codigo del Estatus de Uso',size=3,required=True, help='Registra el Codigo de uso del bien')
    estatus_uso_nombre = fields.Char(string='Nombre del Estatus de Uso',size=40,required=True, help='Registra la Descripcion del Estatus de uso del Bien')

    
    _sql_constraints = [('estatus_uso_codigo', 'unique(estatus_uso_codigo)', 'El Código debe se único!')]    
    _sql_constraints = [('estatus_uso_nombre', 'unique(estatus_uso_nombre)', 'El Nombre debe se único!')] 
    
    



class estado_bien(models.Model):
    """Registra el estatus del Bien"""
    _name = 'estado_bien'
    #_rec_name = 'estado_bien_codigo'
    _rec_name = 'estado_bien_nombre'
    

    estado_bien_codigo = fields.Char(string='Codigo del Estado del Bien',size=3,required=True, help='Registra el Codigo del Estado del Bien')
    estado_bien_nombre = fields.Char(string='Nombre del Estado del bien',size=100,required=True, help='Registra la Descripcion del Estado del Bien')

    _sql_constraints = [('estado_bien_codigo', 'unique(estado_bien_codigo)', 'El Código debe se único!')]    
    _sql_constraints = [('estado_bien_nombre', 'unique(estado_bien_nombre)', 'El Nombre debe se único!')] 


class condicion_fisica(models.Model):

    """Registra la condicion fisica Bien"""
    _name = 'condicion_fisica'
   
    _rec_name = 'condicion_fisica_nombre'
    

    condicion_fisica_codigo = fields.Char(string='Codigo de la Condicion Fisica del Bien',size=3,required=True, help='Registra el Codigo de la Condicion Fisica del Bien')
    condicion_fisica_nombre = fields.Char(string='Nombre de la Condicion Fisica del bien',size=100,required=True, help='Registra la Descripcion de la Condicion Fisica del Bien')

    _sql_constraints = [('condicion_fisica_codigo', 'unique(condicion_fisica_codigo)', 'El Código debe se único!')]    
    _sql_constraints = [('condicion_fisica_nombre', 'unique(condicion_fisica_nombre)', 'El Nombre debe se único!')] 





class tipo_bien(models.Model):
    """Registra el tipo de  Bien"""
    _name = 'tipo_bien'
    #_rec_name = ' tipo_bien_codigo'
    _rec_name = 'tipo_bien_nombre'
    
    tipo_bien_codigo = fields.Char(string='Codigo del Tipo de Bien',size=10,required=True, help='Registra el Codigo del Tipo de Bien')
    tipo_bien_nombre = fields.Char(string='Nombre del Tipo de Bien',size=40,required=True, help='Registra la Descripcion del Tipo de Bien')

    
    _sql_constraints = [('tipo_bien_codigo', 'unique(tipo_bien_codigo)', 'El Código debe se único!')]    
    _sql_constraints = [('tipo_bien_nombre', 'unique(tipo_bien_nombre)', 'El Nombre debe se único!')] 



