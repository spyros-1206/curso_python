# -*- coding: utf-8 -*-

class ModeloDePresupuesto:
    
    #datos comerciales
    titulo = "PRESUPUESTO"
    encabezado_nombre = "Emilio del carpio"
    encabezado_web = "www.naatio.com"
    encabezado_email = "emiliodelcarpio@gmail.com"

    #datos impositivos
    alicuota_iva = 21

    #propiedades relativas al formato
    divline = "="*80

    #setear los datos del cliente
    def set_cliente(self):
        self.empresa = raw_input('\tEmpresa: ')
        self.cliente = raw_input('\tNombre del cliente: ')

    #setear los datos básicos del presupuesto
    def set_datos_basicos(self):
        self.fecha = raw_input('\tFecha: ')
        self.servicio = raw_input('\tDescripcion del servicio: ')
        importe = raw_input('\tImporte bruto: $')
        self.importe = float(importe)
        self.vencimiento = raw_input('\tFecha de caducidad: ')

    #Calcular IVA
    def calcular_iva(self):
        self.monto_iva = self.importe*self.alicuota_iva/100

    #calcula el monto total del presupuesto
    def calcular_neto(self):
        self.neto = self.importe+self.monto_iva

    #armar el presupuesto
    def armar_presupuesto(self):
        """
            Esta función se encarga de armar todo el documento
        """
        txt = '\n'+self.divline+'\n'
        txt += '\t'+self.encabezado_nombre+'\n'
        txt += '\tWeb site: '+self.encabezado_email+'\n'
        txt += '\tE-mail: '+self.encabezado_email+'\n'
        txt += self.divline+'\n'
        txt += '\t'+self.titulo+'\n'
        txt += self.divline+'\n\n'
        txt += '\tFecha: '+self.fecha+'\n'
        txt += '\tEmpresa: '+self.empresa+'\n'
        txt += '\tCliente: '+self.cliente+'\n'
        txt += self.divline+'\n\n'
        txt += '\tDetalle del servicio: \n'
        txt += '\t'+self.servicio+'\n\n'
        txt += '\tImporte: $%0.2f | IVA: $%0.2f\n' % (self.importe, self.monto_iva)
        txt += '-'*80
        txt += '\n\tMONTO TOTAL: $%0.2f\n' % (self.neto)
        txt += self.divline+'\n'
        print txt

    #Método constructor
    def __init__(self):
        print self.divline
        print "\nGENERACIÓN DEL PRESUPUESTO"
        print self.divline
        self.set_cliente()
        self.set_datos_basicos()
        self.calcular_iva()
        self.calcular_neto()
        self.armar_presupuesto()

# Instanciar clase
presupuesto = ModeloDePresupuesto()