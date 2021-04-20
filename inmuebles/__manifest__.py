# -*- coding: utf-8 -*-

{
        'name': "Registro Inicial de Inmuebles Publicos",
        'version' : "13.1",
        'author' : "Beatriz Coronel",
        'website' : "",
        'category' : "Bienes Publicos",
        
        'description': """
                 Registro Inicial de Inmuebles Publicos
         """,
        'depends' : ['base','catalogo','sudebip','web_readonly_bypass'],
        
        'data' : ['security/groups.xml',
        'data/estado_ocupacion_inmueble.xml',
        'data/unidades_medida_area_construccion.xml',
        'data/unidades_medida_area_terreno.xml',
        'data/clase_funcional_terr.xml',

        'security/ir.model.access.csv',
        'views/bienesinmu_view.xml',
        #'report/inmuebles/planilla_inmueble.xml',
        #'report/inmuebles/planilla_inmueble_template.xml',   
        
       


        ], 


      
        
        'installable': True,
        'auto_install': False
        
} 
