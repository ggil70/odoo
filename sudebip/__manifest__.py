# -*- coding: utf-8 -*-

{
        'name': "Registro de Datos Requeridos por la SUDEBIP",
        'version' : "13.1",
        'author' : "Beatriz Coronel",
        'website' : "",
        'category' : "Bienes Publicos",
        
        'description': """
               Datos Requeridos por la SUDEBIP
         """,
        'depends' : ['base',],
        



        'data' : ['security/groups.xml',
                
                  'views/catalogo_sudebip_view.xml',
                  'views/estatus_sudebip_view.xml',
                  'views/formas_adquisicion_view.xml',
                  'views/area_geografica_view.xml',
                  'views/seguros_sudebip_view.xml',
                  'security/ir.model.access.csv', 
       
                  'data/catalogo_general.xml',
                  'data/catalogo_subgeneral.xml',
                  'data/catalogo_esp.xml',
                  'data/color_sudebi.xml',
                  'data/clase_sudebi.xml',
                  'data/estatus_uso.xml',
                  'data/estado_bien.xml',
                  'data/condicion_fisica.xml',
                  'data/tipo_bien.xml',
                  'data/cargo_autoridad.xml',
                  'data/forma_adquisicion.xml',
                  'data/tipos_lugares_ubicacion_sudebip.xml',
                  'data/paises.xml',
                  'data/estados.xml',
                  'data/municipios.xml',
                  'data/parroquias.xml',
                  'data/ciudades.xml',
                  'data/uniadm_sudebi.xml',
                  'data/coberturas.xml',
                  'data/aseguradoras.xml',

                  'data/ir.sequence.xml',
        
      




        ], 


       
        
        #'installable': True,
        #'auto_install': False
        
} 
