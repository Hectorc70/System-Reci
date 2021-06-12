
from modulos.excel import ArchivoExcel

class DatosEmpleados(ArchivoExcel):

    def __init__(self, ruta):
        self.ruta = ruta
        ArchivoExcel.__init__(self, self.ruta)

        self.hoja_lectura = 'Hoja1'
        self.columnas_lectura = ['No. Control', 'Nombre', 
                                'Apellido Paterno', 'Apellido Materno']     

    def leer_datos_empleados(self):

        datos_empleados = list()

        self.leer_titulos(self.hoja_lectura, 1)
        columna_lectura1 = self.claves_columnas[self.columnas_lectura[0]]
        columna_lectura2 = self.claves_columnas[self.columnas_lectura[1]]
        columna_lectura3 = self.claves_columnas[self.columnas_lectura[2]]
        columna_lectura4= self.claves_columnas[self.columnas_lectura[3]]

        control = self.hojas[0][self.hoja_lectura][columna_lectura1] 
        nombre = self.hojas[0][self.hoja_lectura][columna_lectura2] 
        ape_p = self.hojas[0][self.hoja_lectura][columna_lectura3] 
        ape_m = self.hojas[0][self.hoja_lectura][columna_lectura4] 

        
        for datos1, datos2,datos3,datos4 in zip(range(1, len(control)),range(1, len(nombre)),
                                                range(1, len(ape_p)), range(1, len(ape_m))):

            control_datos =str([control[datos1].value][0]).strip()
            nombre_datos = str([nombre[datos2].value][0]).strip()
            apellido_p_datos = str([ape_p[datos3].value][0]).strip()
            apellido_m_datos = str([ape_m[datos4].value][0]).strip()

            datos = [control_datos,nombre_datos, apellido_p_datos, apellido_m_datos]
            
            datos_empleados.append(datos)
        
        self.wb.close()
        return datos_empleados

