# -*- coding: utf-8 -*-

{
        'name': "Registro Inicial de Bienes Publicos",
        'version' : "13.1",
        'author' : "Beatriz Coronel",
        'website' : "",
        'category' : "Bienes Publicos",
        
        'description': """
                 Registro Inicial de Bienes Publicos
         """,
        'depends' : ['base','catalogo','sudebip'],
        
        'data' : ['security/groups.xml',

        'security/ir.model.access.csv',
        'views/bienespu_view.xml',

        
        ], 


      
        
        'installable': True,
        'auto_install': False
        
} 
