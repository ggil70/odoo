# -*- coding: utf-8 -*-

{
        'name': "Registro Inicial de Vehículos Publicos",
        'version' : "13.1",
        'author' : "Beatriz Coronel",
        'website' : "",
        'category' : "Bienes Publicos",
        
        'description': """
                 Registro Inicial de Vehículos Publicos
         """,
        'depends' : ['base','catalogo','sudebip'],
        
        'data' : ['security/groups.xml',

        'security/ir.model.access.csv',
        'views/vehiculos_view.xml',
      
        #'report/vehiculo/planilla_vehiculo.xml',
        #'report/vehiculo/planilla_vehiculo_template.xml',

        'report/vehiculo/vehiculo.xml',
        #'report/vehiculo/vehiculo_template.xml',        
        
        ], 

        'installable': True,
        'auto_install': False
} 
