# -*- coding: utf-8 -*-

from odoo import api, fields, models



from odoo.exceptions import ValidationError

#import logging, csv, operator
##Definimos la Variable Global
#_logger = logging.getLogger(__name__)
import logging.config




class FichaOficinaBienReporteWizard(models.TransientModel):
    _name = 'bienes.ficha.oficina.bien.reporte.wizard'
    bienes_sedes_id = fields.Many2one('sedes',string='Sedes del Organismo', required=True, 
                                        help='Seleccione Sedes del Organismo')
    bienes_oficinas_id = fields.Many2one('oficinas', 'Oficina', size=3, domain="[('sedes_id','=',bienes_sedes_id)]",
                         required=True, help='Registra la Oficina donde esta Ubicado el Bien')


  


    def action_report_bienes(self):
        sede = self.bienes_sedes_id.sedes_nombre
        #sede_id
        oficina = self.bienes_oficinas_id.oficinas_nombre
        
        today = fields.Datetime.now()
        
        fecha = today.strftime('%d/%m/%Y')
        
        #fecha = str(today.day) + "/" + str(today.month) + "/" + str(today.year)  
      
        
        domain = []
        domain = [('bienes_oficinas_id','=',self.bienes_oficinas_id.id)]
        
        bienes_data = self.env['bienes'].search_read(domain)
        
        tot_costo = 0.00
        #Permite obtener total de bienes
        for rec in bienes_data:
            tot_costo = tot_costo + rec['costo']

        tot_costo = "{0:.7f}".format(tot_costo)
        
        
        #cantidad = self.env['bienes'].search_count(domain)
        cantidad = len(bienes_data)
        
        datas = {
            'ids' : self.env.context.get('active_ids',[]),
            'sede' : sede,
            'oficina' : oficina,
            'nro_bienes' : cantidad,
            'tot_costo': tot_costo, 
        }         
        
        if cantidad == 0:
            raise ValidationError('No existen Bienes asociado a la consulta realizada')
        else:
            datas['bienes_data'] = bienes_data
            return self.env.ref('bienes.action_report_bien_oficina').report_action(self, data=datas)
   
            
            
            

        
        
        
        

        
        
        
        
        #raise ValidationError('Hay Datos ' + str(oficina))
        
        ##fields = ['nombre','fecha_pago','estudiante_tarifa']
        #bienes_data = self.env['bienes'].search_read(domain, fields)

        #if bienes_data:
        #   raise ValidationError('Hay Datos')
        #raise ValidationError('NOOOOO Hay Datos')    


        #datas['estudiante_data'] = estudiante_data     
        #return self.env.ref('escuela.action_report_personalizado_estudiante').report_action(self, data=datas)




        #datas = {
        #    'ids' : self.env.context.get('active_ids',[]),
        #    'title' : self.title, 
        #    'date_init' : self.date_init,          
        #}
        #value=[]

        #Con execute
        
        
        #query = """SELECT * FROM escuela_estudiante as ee """
        #if self.date_init:
        #   date_init = str(self.date_init)
        #   query = query + "WHERE ee.fecha_pago <= '" + date_init + "'"
        #self._cr.execute(query, value)

        #record = self._cr.dictfetchall()
        #datas['estudiante_data'] = record
        #return self.env.ref('escuela.action_report_personalizado_estudiante').report_action(self, data=datas)


        #Sin execute 

        #domain = []
        #if self.date_init:
        #    domain = [('fecha_pago','<=',datas["date_init"])]
        #fields = ['nombre','fecha_pago','estudiante_tarifa']
        #estudiante_data = self.env['escuela.estudiante'].search_read(domain,fields)
        #datas['estudiante_data'] = estudiante_data     
        #return self.env.ref('escuela.action_report_personalizado_estudiante').report_action(self, data=datas)
        
        

            
