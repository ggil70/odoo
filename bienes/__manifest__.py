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
        #'report/daily_interna_layout.xml',
        #'report/daily_external_layout.xml',
        #'report/dates_external_layout.xml',
        #'wizard/data_report.xml',

        'views/bienespu_view.xml',
        'report/ficha_bien_oficina_listado_template.xml',

        'wizard/ficha_bien_oficina_reporte_wizard.xml',
        #'views/views.xml',
        #'report/report.xml',
        #'report/inventario_bienes_template.xml',

        
        #'report/action_report_personalizado_estudiante.xml',        

        
        ], 
#

      
        
        'installable': True,
        'auto_install': False
        
} 
