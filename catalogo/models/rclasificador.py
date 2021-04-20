
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
#from odoo.addons.jasper_reports import jasper_report
#from odoo import pooler
from datetime import  datetime
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
_logger = logging.getLogger(__name__)



class grupo_bien(models.Model):
    """Contiene la Informacion sobre los Grupos de Bienes"""
    _name = 'grupo_bien'
    #_rec_name = 'grupo_bien_codigo'
    _rec_name = 'grupo_bien_nombre'
    #_rec_name = 'grupo_bien_partidapre'
   
    grupo_bien_codigo = fields.Char(string='Codigo del Grupo',size=3,
                        help='Registra el Codigo del Grupo',required=True, 
                        copy=False, readonly=True, index=True, default=lambda self: _('New'))
    
    #grupo_bien_codigo = fields.Char(string='Codigo del Grupo',size=3,help='Registra el Codigo del Grupo')
    grupo_bien_nombre = fields.Char(string='Nombre del Grupo',size=100,required=True, help='Registra el Nombre del Grupo')
    grupo_bien_partidapre = fields.Char(string='Partida Presupuestaria', size=14, help='Registra la Partida Presupuestaria')

    _sql_constraints = [('grupo_bien_nombre', 'unique(grupo_bien_nombre)', 'El Nombre debe se único!')]    





       
    @api.model  
    def create(self,vals):
       if vals.get('grupo_bien_codigo', 'New') == 'New':
          vals['grupo_bien_codigo'] = self.env['ir.sequence'].next_by_code(
           'self.grupo_bien_codigo') or 'New'
          
       result = super(grupo_bien, self).create(vals)
       return result 


       # new_id = super(grupo_bien, self).create(vals)
       # return new_id


    # def create(self, vals):
    #     if vals.get('grupo_bien_codigo', 'New') == 'New':
    #             vals['grupo_bien_codigo'] = self.env['ir.sequence'].next_by_code('grupo_bien.grupo_bien_codigo')       

    #     result = super(grupo_bien, self).create(vals)       

    #     return result




    #@api.multi
    #def create_secuencia(self):
    #    seq = self.env['ir.sequence'].next_by_code('grupo_bien_id_seq')
    #    print seq
        #self.grupo_bien_codigo = chr(seq)
        
       # return super(grupo_bien, self).create(vals)
  

#self.grupo_bien_codigo =  self.env['ir.sequence'].next_by_code('grupo_bien.grupo_bien_codigo')



class clasificador_bien(models.Model):
    """Registra la Clasificacion de Bienes Interna"""
    
    _name = 'clasificador_bien'
    #_rec_name = 'clasificador_codigo'
    _rec_name = 'clasificador_nombre'
    #_rec_name = 'grupo_bien_id '
    _order = 'grupo_bien_id,id' 
    

    clasificador_codigo = fields.Char(string='Codigo del Clasificador',size=3,help='Registra el Codigo de la Clasificación del Bien (Interna)')
    clasificador_nombre = fields.Char(string='Nombre del Clasificador',size=100,required=True, help='Registra el Nombre de la Clasificacion del Bien(Interna)')
    grupo_bien_id = fields.Many2one('grupo_bien',string='Grupo de Bienes', required=True, help='Registra el Codigo de Vinculacion con el Grupo de Bienes')
    
    _sql_constraints = [('clasificador_nombre', 'unique(grupo_bien_id,clasificador_nombre)', 'El Nombre debe se único!')]  
    






class modelo_bien(models.Model):
    """Registra el Modelo de los Bienes (interno)"""
    _name = 'modelo_bien'
    #_rec_name = 'modelo_codigo'
    _rec_name = 'modelo_nombre'
    _order = 'clasificador_id,id' 
    #_rec_name = 'clasificador_id'
    
    modelo_codigo = fields.Char(string='Codigo del Modelo',size=3, help='Registra el Codigo del Modelo (Interno)')
    modelo_nombre = fields.Char(string='Nombre del Modelo',size=100,required=True, help='Registra el Nombre del Modelo (Interno)')
    clasificador_id = fields.Many2one('clasificador_bien',string='Clasificador de Bienes',domain="[('grupo_bien_id','=',grupo_bien_id)]",required=True, help='Registra elCodigo de Vinculacion con el Clasificador de Bienes')
    grupo_bien_id = fields.Many2one('grupo_bien',string='Grupo de Bienes', required=True, help='Registra el Codigo de Vinculacion con el Grupo de Bienes')
  
    _sql_constraints = [('modelo_nombre', 'unique(clasificador_id,modelo_nombre)', 'El Nombre debe se único!')]      



class detalle_modelo_bien(models.Model):
    """Registra el Detalle del Modelo de Bienes (Interno)"""
 
    _name = 'detalle_modelo_bien'
    #_rec_name = 'detalle_modelo_codigo'cd 
    _rec_name = 'detalle_modelo_nombre'
    #_rec_name = 'modelo_id'
    _order = 'clasificador_id,modelo_id' 
    detalle_modelo_codigo = fields.Char(string='Codigo del Detalle',size=3,help='Registra el Codigo del Detalle del Modelo de Bienes (Interno)')
    detalle_modelo_nombre = fields.Char(string='Nombre del Detalle',size=100,required=True, help='Registra el Nombre del Detalle del Modelo de Bienes (Interno)')
    modelo_id = fields.Many2one('modelo_bien',string='Modelos de Bienes',required=True,domain="[('clasificador_id','=',clasificador_id)]", help='Registra el Codigo de Vinculación con el Modelo de Bienes')
    clasificador_id = fields.Many2one('clasificador_bien',string='Clasificador de Bienes',required=True, domain="[('grupo_bien_id','=',grupo_bien_id)]",help='Registra elCodigo de Vinculacion con el Clasificador de Bienes')
    grupo_bien_id = fields.Many2one('grupo_bien',string='Grupo de Bienes', required=True, help='Registra el Codigo de Vinculacion con el Grupo de Bienes')


    _sql_constraints = [('detalle_modelo_nombre', 'unique(modelo_id,detalle_modelo_nombre)', 'El Nombre debe se único!')]    
    




        


class marcas(models.Model):
    """Registra las Marcas de los Bienes"""
    _name = 'marcas'
    #_rec_name = 'marcas_codigo'
    _rec_name = 'marcas_nombre'
    

    marcas_codigo = fields.Char(string='Codigo de la Marca',size=3,help='Registra el Codigo de la Marca')
    marcas_nombre = fields.Char(string='Nombre de la Marca',size=40,required=True, help='Registra el Nombre de la Marca')
    marcas_fabricante = fields.Char(string='Nombre del Fabricante',size=40, help='Registra el Nombre del Fabricante')

    _defaults = { 
        'marcas_fabricante': "XXX",
       
     } 


    _sql_constraints = [('marcas_nombre', 'unique(marcas_nombre)', 'El Nombre debe se único!')]    
    


class modelo_fab(models.Model):
    """Registra el Modelo de Fabrica del Bien"""
    _name = 'modelo_fab'
    #_rec_name = 'modelo_fab_codigo'
    _rec_name = 'modelo_fab_nombre'
    #_rec_name = 'marcas_id'
    
   
    modelo_fab_codigo = fields.Char(string='Codigo del Modelo',help='Registra el Codigo del Modelo de Fabrica')
    modelo_fab_nombre = fields.Char(string='Nombre del Modelo',size=100,required=True, help='Registra el Nombre del Modelo de Fabrica')
    marcas_id         = fields.Many2one('marcas',string='Marcas del Modelo',required=True, help='Registra el Codigo de Vinculacion con la Marca del Bien')
    
    _sql_constraints = [('modelo_fab_nombre', 'unique( marcas_id,modelo_fab_nombre)', 'El Nombre debe se único!')]    


class material(models.Model):
    """Registra los Materiales con que esta hecho el bien"""
    _name = 'material'
    #_rec_name = 'material_codigo'
    _rec_name = 'material_nombre'
    
    
    material_codigo = fields.Char(string='Codigo del Material',size=3, help='Registra el Codigo del Material')
    material_nombre = fields.Char(string='Nombre del Material',size=100,required=True,help='Registra el Nombre del Material')
 
    _sql_constraints = [('material_nombre', 'unique(material_nombre)', 'El Nombre debe se único!')]    



class color(models.Model):
    """Registra el Color de los Bienes (Interno)"""
    _name = 'color'
    #_rec_name = 'codigo_color'
    _rec_name = 'color_nombre'
    

    codigo_color = fields.Char(string='Codigo del Color',size=3, help='Registra el Codigo de Color (Interno)')
    color_nombre = fields.Char(string='Nombre del Color',size=100,required=True, help='Registra el Nombre del Color (Interno)')

    _sql_constraints = [('color_nombre', 'unique(color_nombre)', 'El Nombre debe se único!')]  



class estructura_inmueble(models.Model):
   
    _name = 'estructura_inmueble'
    _rec_name = 'estructura_nombre'
    estructura_codigo = fields.Char(string='Codigo del Tipo de Estructura',size=3,help='Registra el Codigo de Tipo de Estructura')
    estructura_nombre = fields.Char(string='Nombre del Tipo de Estructura',size=100,required=True, help='Registra el Nombre del Tipo de Estructura')
    _sql_constraints = [('estructura_nombre', 'unique(estructura_nombre)','El Nombre debe se único!')]      
    

class tipo_piso(models.Model):
    """Registro del tipo de pisos del edificio"""
    _name = 'tipo_piso'
    _rec_name = 'tipo_piso_nombre'
    tipo_piso_codigo = fields.Char(string='Codigo del Tipo de Piso',size=3,help='Registra el Codigo de Tipo de Piso del Inmueble')
    tipo_piso_nombre = fields.Char(string='Nombre del Tipo de Piso',size=100,required=True, help='Registra el Nombre del Tipo de Piso del Inmueble')
    _sql_constraints = [('tipo_piso_nombre', 'unique(tipo_piso_nombre)', 'El Nombre debe se único!')]      
    
class tipo_paredes(models.Model):
    """Registro del tipo de paredes del edificio"""
    _name = 'tipo_paredes'
    _rec_name = 'tipo_paredes_nombre'
    tipo_paredes_codigo = fields.Char(string='Codigo del Tipo de Pared',size=3,help='Registra el Codigo de Tipo de Paredes del Inmueble')
    tipo_paredes_nombre = fields.Char(string='Nombre del Tipo de Pared',size=100,required=True, help='Registra el Nombre del Tipo de Paredes del Inmueble')
    _sql_constraints = [('tipo_paredes_nombre', 'unique(tipo_paredes_nombre)','El Nombre debe se único!')]  

class tipo_techo(models.Model):
    """Registro del tipo de techo del edificio"""
    _name = 'tipo_techo'
    _rec_name = 'tipo_techo_nombre'
    tipo_techo_codigo = fields.Char(string='Codigo del Tipo de Techo',size=3,help='Registra el Codigo de Tipo de Techos del Inmueble')
    tipo_techo_nombre = fields.Char(string='Nombre del Tipo de Techo',size=100,required=True, help='Registra el Nombre del Tipo de Techos del Inmueble')
    _sql_constraints = [('tipo_techo_nombre', 'unique(tipo_techo_nombre)', 'El Nombre debe se único!')]    


class tipo_puertas(models.Model):
    """Registro del tipo de puertas del edificio"""
    _name = 'tipo_puertas'
    _rec_name = 'tipo_puertas_nombre'
    tipo_puertas_codigo = fields.Char(string='Codigo del Tipo de Puertas',size=3,help='Registra el Codigo de Tipo de Puertas del Inmueble')
    tipo_puertas_nombre = fields.Char(string='Nombre del Tipo de Puertas',size=100,required=True, help='Registra el Nombre del Tipo de Puertas del Inmueble')
    _sql_constraints = [('tipo_puertas_nombre', 'unique(tipo_puertas_nombre)','El Nombre debe se único!')]   


class tipo_servicios(models.Model):
    """Registro del tipo de pisos del edificio"""
    _name = 'tipo_servicios'
    _rec_name = 'tipo_servicios_nombre'
    tipo_servicios_codigo = fields.Char(string='Codigo del Tipo de Servicio',size=3,help='Registra el Codigo de Tipo de Servicios del Inmueble')
    tipo_servicios_nombre = fields.Char(string='Nombre del Tipo de Servicio',size=100,required=True, help='Registra el Nombre del Tipo de Servicios del Inmueble')
    _sql_constraints = [('tipo_servicios_nombre','unique(tipo_servicios_nombre)', 'El Nombre debe se único!')]       


class tipo_anexos(models.Model):
    """Registro del tipo de anexos del edificio"""
    _name = 'tipo_anexos'
    _rec_name = 'tipo_anexos_nombre'
    tipo_anexos_codigo = fields.Char(string='Codigo del Tipo de Anexo',size=3,help='Registra el Codigo de Tipo de Anexos del Inmueble')
    tipo_anexos_nombre = fields.Char(string='Nombre del Tipo de Anexo',size=100,required=True, help='Registra el Nombre del Tipo de Anexos del Inmueble')
    _sql_constraints = [('tipo_anexos_nombre','unique(tipo_anexos_nombre)', 'El Nombre debe se único!')]   




#****************Tipos de Movimientos*******************#
class tipo_movimiento(models.Model):
    """Registra los Tipos movimientos de bienes"""
    _name = 'tipo_movimiento'
    _rec_name = 'nom_mov'
    nom_mov = fields.Char('Nombre del Movimiento',size=100,required=True, help='Registra el Nombre del Movimiento')
    cod_mov = fields.Char('Codigo del Movimiento',size=100,required=True, help='Registra el Codigo del Movimiento ')
    sw_desin = fields.Boolean ('Desincorporado', help='Registra si el bien fue Desincorporado')
    _sql_constraints = [('nom_mov', 'unique(nom_mov)', 'El Nombre del Movimiento debe ser Unico!')]  



#****************Enten Externos a quien se le Envian Bienes*******************#

class ente_externo(models.Model):
    """Registra los Entes Externos"""
    _name = 'ente_externo'
    _rec_name = 'ente_externo_nombre'
    ente_externo_rif = fields.Char('Rif' ,required=True,help='Registra el Rif del Ente Externo')
    ente_externo_cedula = fields.Char('Cedula del Funcionario Responsable' ,required=True, help='Registra la Cedula  Funcionario Responsable del Ente Externo')
    ente_externo_nombre = fields.Char('Nombre del Ente Externo',size=200,required=True, help='Registra el Nombre del Ente Externo')
    ente_externo_funcionario = fields.Char('Nombre del Funcionario Responsable',size=200,required=True, help='Registra el Nombre del Funcionario Responsable del Ente Externo')
    ente_externo_telf   = fields.Char('Telefono del Funcionario Responsable',size=100,required=True, help='Registra el Numero de telefono del Funcionario Responsabledel Ente Externo')
    ente_externo_correo = fields.Char('Correo del Funcionario Responsable',size=200,required=True, help='Registra el Correo del Funcionario Responsable del Ente Externo')
    _sql_constraints = [('ente_externo_nombre', 'unique(ente_externo_nombre)', 'El Ente Externo ya esta Registrado!')] 


#****************Ubicacion Fisica**************************#
class ubicacion_fisica(models.Model):
    """Registra  la Ubicación Fisica del Bien"""
    _name = 'ubicacion_fisica'
    _rec_name = 'ubicacion_fisica_nombre'
    ubicacion_fisica_nombre = fields.Char('Nombre de la Ubicación Fiísica del Bien',size=100,required=True, help='Registra el Nombre de la Categoria de Oficina (SUDEBIP)')



    _sql_constraints = [('ubicacion_fisica_nombre', 'unique(ubicacion_fisica_nombre)', 'El Nombre debe se único!')]

#****************Fin Ubicacion Fisica**************************




#****************Tipos de Estatus de Inventario*******************#
class tipo_estatus_inventario(models.Model):
    """Registra los Tipos de estatus de inventario de bienes"""
    _name = 'tipo_estatus_inventario'
    _rec_name = 'nom_estatus'
    nom_estatus = fields.Char('Nombre del Estatus del Inventario',size=100,required=True, help='Registra el Nombre del Movimiento')
    cod_estatus = fields.Char('Codigo del Movimiento',size=100, help='Registra el Codigo del Estatus de Inventario')
    _sql_constraints = [('nom_estatus', 'unique(nom_estatus)', 'El Nombre del Estatus del Inventario debe ser Unico!')]  


