# -*- coding: utf-8 -*- 
from string import Template     # Importo la clase Template del módulo string 
                                # nativos de Python
                                # Agregado en el capítulo 3

class ModeloDePresupuesto: 

    # Datos comerciales 
    titulo = "PRESUPUESTO"
    encabezado_nombre = "Eugenia Bahit" 
    encabezado_web = "www.eugeniabahit.com.ar" 
    encabezado_email = "mail@mail.com" 

    # Datos impositivos 
    alicuota_iva = 21 

    # Propiedades relativas al formato
    divline = "="*80
    html = 'templates/template.html'      # Plantilla HTML
    txt = 'templates/template.txt'        # Plantilla TXT

    # Planes y servicios - Capítulo 3
    planes = ('corporativo', 'personal', 'mantenimiento')       # Tupla
    corporativo = ['Diseño Sitio Web corporativo', 7200]        # Lista
    personal = ['Diseño Sitio Web básico', 4500]                # Lista
    mantenimiento = ['Mantenimiento sitio Web (mensual)', 500]  # Lista
    lista_precios = {'corporativo':corporativo,
                     'personal':personal,
                     'mantenimiento':mantenimiento}             # Diccionario


    # Setear los datos del cliente 
    def set_cliente(self): 
        self.empresa = raw_input('\tEmpresa: ')
        self.cliente = raw_input('\tNombre del cliente: ')

    # Incorporación de nuevo método - Capítulo 3
    # Seleccionar tipo de plan 
    def seleccionar_plan(self): 
        texto_a_mostrar = "\tServicio ofrecido " 
        codigo_plan = 0 

        # Nuevo! Estructura de control -> bucle "for"
        for plan in self.planes: 
            texto_a_mostrar += '(%d)%s  ' % (codigo_plan, plan) 
            codigo_plan = codigo_plan+1 

        texto_a_mostrar += ": " 
        elegir_plan = raw_input(texto_a_mostrar)
        elegir_plan = int(elegir_plan) # int() convierte a número entero
        self.plan = self.planes[elegir_plan]
        datos_servicio = self.lista_precios[self.planes[elegir_plan]]
        self.servicio = datos_servicio[0]
        importe = datos_servicio[1]
        self.importe = float(importe)

    # Setear los datos básicos del presupuesto 
    # Modificado en el capítulo 3
    def set_datos_basicos(self): 
        self.fecha = raw_input('\tFecha: ') 
        self.seleccionar_plan() # llamo al nuevo método para seleccionar plan
        self.vencimiento = raw_input('\tFecha de caducidad: ')  

    # Calcular IVA 
    def calcular_iva(self): 
        self.monto_iva = self.importe*self.alicuota_iva/100 

    # Calcula el monto total del presupuesto 
    def calcular_neto(self): 
        self.neto = self.importe+self.monto_iva 

    # Armar numero de presupuesto
    def armar_numero_presupuesto(self):
        contador = open('contador.txt', 'r+')   # Abro contador
        ultimo_num = int(contador.read())       # obtengo ultimo numero
        nuevo = ultimo_num+1                    # genero nuevo número
        contador.seek(0)                        # muevo cursor a byte 0
        nuevo = str(nuevo)                      # convierto numero a string
        contador.write(nuevo)                   # sobreescribo el número
        contador.close()                        # cierro contador
        self.numero_presupuesto = nuevo         # seteo el nuevo número

    # Guardar presupuesto en archivo
    def guardar_presupuesto(self, txt, html):
        respuesta = raw_input('\n\t¿Desea guardar el presupuesto? (s/n): ')
        # Si el usuario indica s
        if respuesta.lower() == 'n':
            print txt
        # si en cambio el usuario indica n
        elif respuesta.lower() == 's':
            filename = 'presupuestos/'+self.numero_presupuesto+'.html'
            presupuesto = open(filename, 'w')   # Creo el archivo
            presupuesto.write(html)             # escribo el contenido
            presupuesto.close()                 # cierro el archivo
            print '\n\tEl archivo se ha guardado en '+filename+'\n\n'
        # sino
        else:
            print '\n\tOpción incorrecta. No se guardó el presupuesto.\n\n'
            self.guardar_presupuesto(txt, html)

    # Armar el presupuesto 
    def armar_presupuesto(self):
        """Esta función se encarga de armar todo el presupuesto"""

        self.armar_numero_presupuesto()         # traigo numero de presupuesto

        html_file = open(self.html, 'r')        # tarer template HTML
        html = html_file.read()                 # leo el template HTML
        html_file.close()                       # cierro el archivo HTML

        txt_file = open(self.txt, 'r')          # tarer template TXT
        txt = txt_file.read()                   # leo el template TXT
        txt_file.close()                        # cierro el archivo TXT

        # armo un diccionario con todos los datos que utilizo en el template
        diccionario = dict(nombre=self.encabezado_nombre,
                           web=self.encabezado_web,
                           email=self.encabezado_email,
                           titulo=self.titulo,
                           numero=self.numero_presupuesto,
                           fecha=self.fecha,
                           empresa=self.empresa,
                           cliente=self.cliente,
                           plan=self.plan,
                           servicio=self.servicio,
                           precio=self.importe,
                           iva=self.monto_iva,
                           total=self.neto,
                           limite=self.vencimiento)

        # Hago un render del template - reemplazo datos dinámicamente
        txt = Template(txt).safe_substitute(diccionario)
        html = Template(html).safe_substitute(diccionario)
        self.guardar_presupuesto(txt, html)     # ofrezco guardarl presupuesto

    # Método constructor 
    def __init__(self):
        print self.divline 
        print "\tGENERACIÓN DEL PRESUPUESTO" 
        print self.divline 
        self.set_cliente() 
        self.set_datos_basicos() 
        self.calcular_iva() 
        self.calcular_neto() 
        self.armar_presupuesto()

# Instanciar clase 
presupuesto = ModeloDePresupuesto()
