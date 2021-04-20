# -*- coding= utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.osv import expression




#from Datetime import Date, Datetime,timedelta
##############from odoo.addons.jasper_reports import jasper_report
#from odoo import pooler
#from Datetime import  Datetime
from time import time
formatter_string = "%d-%m-%y" 
#from tools.translate import_
#from odoo import tools
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")
#Importamos la libreria logger
import logging, csv, operator
#Definimos la Variable Global
_logger = logging.getLogger(__name__)
  




class bienes(models.Model):
    """Registro de Bienes"""
    _name = 'bienes'
    _rec_name = 'bienes_numbien'
    _order = 'bienes_numbien'  
   # _rec_name =  'bienes_nombre'
    #_rec_name = 'bienes_numbien_ant'
    #_rec_name = 'bienes_serial
    #_rec_name = 'grupo_bien_id'
    #_rec_name = 'clasificador_bien_id'
    #_rec_name = 'modelo_bien_id'
    #_rec_name = 'detalle_modelo_id'
    #_rec_name = 'color_id'
    #_rec_name = 'material_id'
    #_rec_name = 'oficinas_id'
    #_rec_name = 'marcas_id'
    #_rec_name = 'modelo_fab_id'
    #_rec_name = 'medidas'
    #_rec_name = 'resp_uso_id'
    #_rec_name = 'resp_pat_id'
    #_rec_name = 'costo'
    #_rec_name = 'estatus_uso_id'
    #_rec_name = 'estatus_bien_id'
    #_rec_name = 'detalle_adquisi_id'
    #_rec_name = 'catalogo_sudebi_id'
    #_rec_name = 'catalogo_sudebi_sub_id'
    #_rec_name = 'catalogo_sudebi_esp_id'
    #_rec_name = 'estado_id'
    #_rec_name = 'municipios_id'
    #_rec_name = 'parroquias_id'
    #_rec_name = 'poliza_id'
    #_rec_name = 'clase_sudebi_id'
    
    
    
    bienes_numbien = fields.Char('Numero del Bien',size=20, help='Registra el Numero de Bien Nacional')
    bienes_nombre  = fields.Text('Descripcion del Bien', size=300, help='Registra la Descripcion del Bien')
    tipo_bien_id      = fields.Many2one('tipo_bien', 'Código del Tipo de Bien', size=10, help='Registra el Código del Tipo de Bien')
    tipo_bien_codigo = fields.Char(string='Codigo del Tipo de Bien',size=10,required=True, help='Registra el Codigo del Tipo de Bien')

    bienes_serial = fields.Char('Serial del Bien',size=50, help='Registra el Numero de Serial del Bien Nacional')
    bienes_piso   = fields.Integer('Num. de Piso ',size=2, help='Registra el Piso donde se encuentra el Bien Nacional')
    
    bienes_ubica_id  = fields.Many2one('ubicacion_fisica', 'Ubicacion Fisica del Bien', size=3, help='Registra la Ubicación Física del Bien')
    ubicacion_fisica_codigo = fields.Char(string='Codigo de la Ubicacion Física',
                    size=3,
                    help='Registra el Codigo de la Ubicacion Física (Interno)')
    
    grupo_bien_id = fields.Many2one('grupo_bien', 'Grupo del Bien', size=3, domain="[('grupo_bien_codigo','!=',5) ,('grupo_bien_codigo','!=',16)]",  help='Registra el Grupo al Cual Pertenece elBien')   
    grupo_bien_codigo =  fields.Char(string='Codigo del Grupo',size=3,  required=True,help='Registra el Codigo del Grupo (Interna)')

    clasificador_bien_id = fields.Many2one('clasificador_bien', 'Clasificador del Bien', domain="[('grupo_bien_id','=',grupo_bien_id)]", size=3, help='Registra el Codigo de Clase del Bien')
    clasificador_codigo = fields.Char(string='Codigo de la Clase',
                          size=3,
                          required=True,
                        
                          help='Registra el Codigo de la Clase del Bien (Interna)')
    modelo_bien_id = fields.Many2one('modelo_bien', 'Modelo del Bien', size=3, domain="[('clasificador_id','=',clasificador_bien_id)]", help='Registra el Modelo del Bien')   
    modelo_codigo = fields.Char(string='Codigo del Modelo',size=3,
                    required=True,
                    help='Registra el Codigo del Modelo (Interno)')
    detalle_modelo_id = fields.Many2one('detalle_modelo_bien', 'Detalle del Modelo del Bien', size=3, domain="[('modelo_id','=',modelo_bien_id)]", help='Registra el Modelo Especifico del Bien')
    detalle_modelo_codigo = fields.Char(string='Codigo del Detalle',
                            size=3,
                            
                            help='Registra el Codigo del Detalle del Modelo de Bienes (Interno)') 
    material_id = fields.Many2one('material', 'Material del Bien', size=3, required=True,help='Registra el Material con que esta hecho el Bien')
    material_codigo = fields.Char(string='Codigo del Material',
                      size=3,
                      required=True,
                      help='Registra el Codigo del Material')
    color_id = fields.Many2one('color', 'Color del Bien', size=3, required=True,help='Registra el Color del Bien')
    color_codigo = fields.Char(string='Codigo del Color',
                    size=3,
                    required=True,
                    help='Registra el Codigo de Color (Interno)')
    bienes_oficinas_id = fields.Many2one('oficinas', 'Oficina', size=3, domain="[('sedes_id','=',bienes_sedes_id)]",required=True,help='Registra la Oficina donde esta Ubicado el Bien')
    bienes_oficinas_codigo       = fields.Char(string='Nomenclatura de la Oficina',size=20,required=True, help='Registra la Nomenclatura de la Oficina')

    bienes_sedes_id  = fields.Many2one('sedes',string='Sedes del Ministerio', required=True,domain="[('regiones_id','=',bienes_regiones_id)]",help='Registra el Codigo de Vinculacion con las Sedes del Ministerio')
    bienes_sedes_codigo       = fields.Char(string='Código de la Sede',size=7,required=True, help='Registra el Código de la Sede')

    bienes_regiones_id  = fields.Many2one('regiones',string= 'Regiones de Ubicación de la Sede',size=3,required=True, help='Regiones de Ubicación de la Sede')    
    bienes_regiones_codigo       = fields.Char(string='Codigo de la Región',size=3,required=True, help='Registra el Codigo de la Región')

    resp_uso_id = fields.Many2one('personas', 'Responsable de Uso', domain="[('personas_oficinas_id','=',bienes_oficinas_id)]",size=3,required=True, help='Registra el Responsable del Uso del Bien')
    cedu_resp_uso = fields.Integer(string='Cédula del Responsable de Uso',size=10,required=True, help='Registra la Cedula de la persona')

    marcas_id = fields.Many2one('marcas', 'Marca del Bien', size=3, help='Registra la Marca del Bien')
    marcas_codigo = fields.Char(string='Codigo de la Marca',
                    size=3,
                    required=True,
                    help='Registra el Codigo de la Marca')
    modelo_fab_id = fields.Many2one('modelo_fab', 'Modelo de Fabrica', size=3, domain="[('marcas_id','=',marcas_id)]", help='Registra el Modelo de Fabrica del Bien')
    modelo_fab_codigo = fields.Char(string='Codigo del Modelo',
                         size=3,
                         required=True,help='Registra el Codigo del Modelo de Fabrica')
    


    medidas = fields.Char('Medidas del Bien', size=50, help='Registra las Medidas del Bien')
    costo = fields.Float('Costo de Bien', help='Registra el Costo del Bien',digits=(16, 7))
    
    estatus_uso_id = fields.Many2one('estatus_uso', 'Estatus de Uso', size=3, help='Registra el Estatus de Uso del Bien ')
    estatus_uso_codigo = fields.Char(string='Codigo del Estatus de Uso',size=3,required=True, help='Registra el Codigo de uso del bien')
    
    estado_bien_id = fields.Many2one('estado_bien', 'Estado del Bien', size=3, help='Registra el Estado del Bien')
    estado_bien_codigo = fields.Char(string='Codigo del Estado del Bien',size=3,required=True, help='Registra el Codigo del Estado del Bien')
    
    condicion_fisica_id = fields.Many2one('condicion_fisica', 'Condicion Física del Bien', size=3,help='Registra la Condicion Física del Bien')
    condicion_fisica_codigo = fields.Char(string='Codigo de la Condicion Fisica del Bien',size=3,required=True, help='Registra el Codigo de la Condicion Fisica del Bien')
    
    detalle_adquisi_id = fields.Many2one('detalle_adquisi', 'Detalle de Aquisicion del Bien', size=3,help ='Registra el detalle de la Adquisición del Bien')
    detalle_adquisi_codigo   = fields.Char(string='Código del Detalle',size=12,
                              help='Registra el Codigo del Detalle de la Adquisicion del Bien')

    forma_adquisicion_codigo = fields.Char(string='Codigo de la Forma de Adquisicion',size=3, help='Registra el Codigo de la Forma de Adquisicion')


    catalogo_sudebi_id = fields.Many2one('catalogo_sudebi', 'Categoría  General(SUDEBIP)', help='Registra el Catalogo General de la SUDEBIP')
    catalogo_sudebi_codigo   = fields.Char(string='Codigo de la Categoria',size=10,required=True, help='Codigo de la Categoria General de la (SUDEBIP)')

    catalogo_sudebi_sub_id = fields.Many2one('catalogo_sudebi_sub','Categoría  Sub-General(SUDEBIP)', domain="[('catalogo_sudebi_id','=',catalogo_sudebi_id)]", help='Registra la Categoria Sub- General de la SUDEBIP')
    catalogo_sudebi_sub_codigo  = fields.Char(string='Codigo de la SubCategoria',size=10,required=True, help='Codigo de la Categoria Sub-General de la (SUDEBIP)')

    catalogo_sudebi_esp_id = fields.Many2one('catalogo_sudebi_esp','Categoría  Específica (SUDEBIP)', domain="[('catalogo_sudebi_sub_id','=',catalogo_sudebi_sub_id)]",help='Registra la Categoria Específica de la SUDEBIP')
    catalogo_sudebi_esp_codigo   = fields.Char(string='Codigo de la Categoria Específica',size=10, help='Codigo de la Categoria Especifica de la (SUDEBIP)')

    color_sudebi_id = fields.Many2one('color_sudebi','Color segun (SUDEBIP)', help='Registra el Color segun SUDEBIP')
    color_sudebi_codigo = fields.Char(string='Codigo del Color segun Sudebip',size=3, help='Registra el Codigo de Color segun (SUDEBIP)')

    poliza_id = fields.Many2one('poliza','Poliza de Seguro', size=3)
    poliza_codigo        = fields.Char(string='Codigo de la Poliza',size=3, help='Registra el Codigo de la Poliza')

    garantia = fields.Integer('Garantía',size=5,help='Registra la Garantía del Bien')
    unidad_garantia = fields.Selection([('1','Días'),('2','Meses'),('3','Años'),('99',"No Aplica")],'Unidad de Garantía',size=2,help='Registra la Unidad de Medida de la Garantía')
    fecha_ini_garantia = fields.Date('Fecha Inicio de la Garantía', size=8,help='Registra la Fecha de Inicio de la Garantía')
    fecha_fin_garantia = fields.Date('Fecha Fin de la Garantía', size=8,help='Registra la Fecha de Fin de la Garantía')
    fech_inventario = fields.Date('Fecha de Registro en el Inventario', size=8,help='Registra la Fecha de Registro en el Inventario de la Oficina')   
    observacion =   fields.Text('Observaciones al Bien', help='Registra las Observaciones al Bien')
    tipo_estatus_inventario_id = fields.Many2one('tipo_estatus_inventario','Estatus de Inventario del Bien')
    cod_estatus = fields.Char('Codigo del Estatus del Inventario',size=100, help='Registra el Codigo del Estatus de Inventario')

    #bienes_ministerio =  fields.Many2one('bienes_ministerio',string='Información del Ministerio para la Remisión', help='Registra la Información del Ministerio para la Remisión del Inventario')



    sw_desin = fields.Boolean ('Desincorporado',  default = lambda self:'True', help='Registra si el bien fue Desincorporado')    
    active = fields.Boolean ('Activo', default=True, help='Si esta Activo el motro lo icluira en la vista')    
    
    
    @api.onchange('bienes_regiones_id')
    def onchange_bienes_regiones(self):
        codigor= ''
        codigor = self.bienes_regiones_id.regiones_codigo
        self.bienes_regiones_codigo =  codigor

    @api.onchange('bienes_sedes_id')
    def onchange_bienes_sedes(self):
        codigos= ''
        codigos = self.bienes_sedes_id.sedes_codigo
        self.bienes_sedes_codigo =  codigos

    @api.onchange('bienes_oficinas_id')
    def onchange_bienes_oficinas(self):
        codigoo= ''
        codigoo = self.bienes_oficinas_id.oficinas_codigo
        self.bienes_oficinas_codigo =  codigoo

    @api.onchange('resp_uso_id')
    def onchange_resp_uso(self):
        codigore= ''
        codigore = self.resp_uso_id.personas_cedula
        self.cedu_resp_uso =  codigore


    @api.onchange('tipo_bien_id')
    def onchange_tipo_bien(self):
        codigo= ''
        codigo = self.tipo_bien_id.tipo_bien_codigo
        self.tipo_bien_codigo =  codigo
    

    @api.onchange('bienes_ubica_id')
    def onchange_bienes_ubica(self):
        codigo= ''
        codigo = self.bienes_ubica_id.ubicacion_fisica_codigo
        self.ubicacion_fisica_codigo =  codigo


        
    @api.onchange('grupo_bien_id')
    def onchange_grupo(self):
        codigo= ''
        codigo = self.grupo_bien_id.grupo_bien_codigo
        self.grupo_bien_codigo =  codigo
        self.clasificador_bien_id = ''
          
    @api.onchange('clasificador_bien_id')
    def onchange_clasif(self):
        codigoc= ''
        codigoc = self.clasificador_bien_id.clasificador_codigo
        self.clasificador_codigo =  codigoc
        self.modelo_bien_id =  ''
    
    @api.onchange('modelo_bien_id')
    def onchange_modelo(self):
        codigom= ''
        codigom = self.modelo_bien_id.modelo_codigo
        self.modelo_codigo =  codigom
        self.detalle_modelo_id =  ''
    
    @api.onchange('grupo_bien_id','clasificador_bien_id','modelo_bien_id','detalle_modelo_id','material_id','color_id')
    def onchange_categorias(self):
        catego =''
        detamod = ''
       
        if self.clasificador_bien_id.clasificador_nombre:
            catego += str(self.clasificador_bien_id.clasificador_nombre)
        if self.modelo_bien_id.modelo_nombre:
              catego += ' '+ str(self.modelo_bien_id.modelo_nombre)
        if self.detalle_modelo_id.detalle_modelo_nombre:
            if self.detalle_modelo_id.detalle_modelo_nombre != False:
                self.detalle_modelo_codigo = self.detalle_modelo_id.detalle_modelo_codigo
                catego += ' '+str(self.detalle_modelo_id.detalle_modelo_nombre)
        if self.material_id.material_nombre:
            catego += ' '+str(self.material_id.material_nombre)
        if  self.color_id.color_nombre:
            catego += ' '+str(self.color_id.color_nombre)
            
        #self.bienes_nombre = str(self.clasificador_bien_id.clasificador_nombre)+' '+ str(self.modelo_bien_id.modelo_nombre)+ ' ' + str(self.detalle_modelo_id.detalle_modelo_nombre).encode('utf-8') +' '+ str(self.material_id.material_nombre) +' '+ str(self.color_id.color_nombre)
        self.bienes_nombre = catego
        self.active = 'true'
    
    
    @api.onchange('material_id')
    def onchange_material(self):
        codigoma= ''
        codigoma = self.material_id.material_codigo
        self.material_codigo =  codigoma

    @api.onchange('color_id')
    def onchange_color(self):
        codigoco= ''
        codigoco = self.color_id.color_codigo
        self.color_codigo =  codigoco


    @api.onchange('estatus_uso_id')
    def onchange_estatus_uso(self):
        codigo= ''
        codigo = self.estatus_uso_id.estatus_uso_codigo
        self.estatus_uso_codigo =  codigo

    @api.onchange('estado_bien_id')
    def onchange_estado_bien(self):
        codigo= ''
        codigo = self.estado_bien_id.estado_bien_codigo
        self.estado_bien_codigo =  codigo   

    @api.onchange('condicion_fisica_id')
    def onchange_condicion_fisica(self):
        codigo= ''
        codigo = self.condicion_fisica_id.condicion_fisica_codigo
        self.condicion_fisica_codigo =  codigo

    @api.onchange('detalle_adquisi_id')
    def onchange_detalle_adquisi(self):
        codigo= ''
        codigoad =''
        codigo = self.detalle_adquisi_id.detalle_adquisi_codigo
        codigoad = self.detalle_adquisi_id.codigo_ad
        self.detalle_adquisi_codigo =  codigo
        self.forma_adquisicion_codigo = codigoad


    @api.onchange('catalogo_sudebi_id')
    def onchange_catalogo_sudebi(self):
        codigo= ''
        codigo = self.catalogo_sudebi_id.catalogo_sudebi_codigo
        self.catalogo_sudebi_codigo =  codigo

    @api.onchange('catalogo_sudebi_sub_id')
    def onchange_catalogo_sudebi_sub(self):
        codigo= ''
        codigo = self.catalogo_sudebi_sub_id.catalogo_sudebi_sub_codigo
        self.catalogo_sudebi_sub_codigo =  codigo

    @api.onchange('catalogo_sudebi_esp_id')
    def onchange_catalogo_sudebi_esp(self):
        codigo= ''
        codigo = self.catalogo_sudebi_esp_id.catalogo_sudebi_esp_codigo
        self.catalogo_sudebi_esp_codigo =  codigo


    @api.onchange('color_sudebi_id')
    def onchange_color_sudebi(self):
        codigo= ''
        codigo = self.color_sudebi_id.color_sudebi_codigo
        self.color_sudebi_codigo =  codigo


    @api.onchange('poliza_id')
    def onchange_poliza(self):
        codigo= ''
        codigo = self.poliza_id.poliza_codigo
        self.poliza_codigo =  codigo
  
    @api.onchange('tipo_estatus_inventario_id')
    def onchange_tipo_estatus_inventario(self):
        codigo= ''
        codigo = self.tipo_estatus_inventario_id.cod_estatus
        self.cod_estatus =  codigo
    
    @api.onchange('marcas_id')
    def onchange_marcas(self):
        codigo= ''
        codigo = self.marcas_id.marcas_codigo
        self.marcas_codigo =  codigo

    @api.onchange('modelo_fab_id')
    def onchange_modelo_fab(self):
        codigo= ''
        codigo = self.modelo_fab_id.modelo_fab_codigo
        self.modelo_fab_codigo =  codigo   



    _sql_constraints = [('bienes_numbien', 'unique(bienes_numbien)', 'El Número de Bien debe se único!')]
 
    _defaults = { 
        'sw_desin': False,
        'active' : True,
        } 
   

  










#****************Modificacion de bienes**************************
# class modificaciones_bienes(models.Model):
#     """Registra  la Ubicación Fisica del Bien"""
#     _name = 'modificaciones_bienes'
#     _rec_name = 'modificaciones_motivo'
    
#     modificaciones_motivo= fields.Char('Nombre de la Ubicación Fiísica del Bien',size=100,required=True, help='Registra el Nombre de la Categoria de Oficina (SUDEBIP)')
#     sw_modificacion_analista = fields.Boolean ('Desincorporado', help='Registra si el bien fue Desincorporado')  
#     sw_modificacion_director = fields.Boolean ('Desincorporado', help='Registra si el bien fue Desincorporado')  
#     fecha_solicitud          = fields.Date('Fecha Solicitud de la Modificación', size=8,help='Registra la Fecha Solicitud de la Modificación')
#     fecha_aprobacion         = fields.Date('Fecha Aprobación de la Modificación', size=8,help='Registra la Fecha Solicitud de la Modificación')
    
#     _sql_constraints = [('ubicacion_fisica_nombre', 'unique(ubicacion_fisica_nombre)', 'El Nombre debe se único!')]

#****************Fin modificacion de bienes**************************

