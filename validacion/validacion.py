from re import split

from modulos.rutas import dividir_cadena, unir_cadenas


class ArchivosPorValidar():
    """Clase que depura los recibos y timbres 
    del backup limpio quitando honorarios y jubilados.
    """

    def __init__(self, ruta_directorio, archivos):
        self.archivos = archivos

        self.num_directorio = len(ruta_directorio.split('/'))

    def depurar_archivos(self):
        """Parametros: list:rutas_archivos(rutas divididas). \n
        Salida: retorna una lista con rutas dividas quitando las nominas
        de honorarios y jubilados.
        """

        archivos = list()
        for archivo in self.archivos:
            nomina = archivo[self.num_directorio+1].split('_')
            try:
                if (nomina[0] != 'HONORARIOS' and
                    nomina[1] != 'HONORARIOS' and
                        nomina[0] != 'JUBILADOS'):
                    ruta = unir_cadenas('\\', archivo)
                    archivo.append(ruta)
                    archivos.append(archivo)
            except:
                if (nomina[0] != 'HONORARIOS' and
                        nomina[0] != 'JUBILADOS'):
                    ruta = unir_cadenas('\\', archivo)
                    archivo.append(ruta)
                    archivos.append(archivo)

        return archivos


class ArchivosValidados():
    """Clase que valida los recibos y timbres 
    que empaten uno a uno, tomando en cuenta
    todas las nominas, excepto jubilados y honorarios \n
    Parametros: list:timbres, list:recibos
    salida.... 
    """

    def __init__(self, timbres, recibos):
        self.timbres = self.__armar_archivos(timbres)
        self.recibos = self.__armar_archivos(recibos)

    def __armar_archivos(self, rutas_archivos):
        """Parametros: list:rutas_archivos(rutas completas de los 
        archivos para poder hacerlos unicos e identificables). \n
        Salida: retorna una lista con dos diccionarios:\n 
        {periodo+nomina+control: nombre de archivo},
        {periodo+nomina+control: ruta archivo}.
        """

        archivos_unicos = dict()
        ruta_archivos = dict()
        for archivo in rutas_archivos:
            datos = archivo.split('\\')
            periodo = datos[-4]
            nomina = datos[-3]
            tipo_carpeta = datos[-2].split('_')[0]
            control = datos[-1].split('_')[0]
            nombre_archivo = datos[-1]
            clave = unir_cadenas('_', [periodo, nomina, control])

            if tipo_carpeta == 'BASE4':
                clave = unir_cadenas(
                    '_', [periodo, nomina, tipo_carpeta, control])

            archivos_unicos[clave] = [nombre_archivo]
            ruta_archivos[clave]   = archivo
        
        
        return [archivos_unicos, ruta_archivos]

    def validar(self):
        """Busca el timbre del recibo solo si lo encuentra
        agrega en las dos estructuras el recibo y el timbre. \n 
        retorna los que no tienen estos dos datos"""

        for clave in self.recibos[0].keys():
            if clave in self.timbres[0]:
                self.timbres[0][clave] = [self.recibos[0][clave], self.timbres[0][clave]]
                self.recibos[0][clave] = [self.recibos[0][clave], self.timbres[0][clave]]

        archivos_sin_todos_datos = self.__no_encontrados()

        return archivos_sin_todos_datos


    def __no_encontrados(self):
        """Retorna los archivos de timbres sin 
        recibos y recibos sin timbres"""

        timbres = list()
        recibos = list()

        for clave, datos in self.timbres[0].items():
            if len(self.timbres[0][clave]) == 1:
                datos = clave.split('_')
                periodo = unir_cadenas('_', [datos[0],datos[1]])
                nomina = datos[2]

                datos_salida = [periodo, nomina, self.timbres[1][clave]]
                timbres.append(datos_salida)



        for clave, datos in self.recibos[0].items():
            if len(self.recibos[0][clave]) == 1:
                datos = clave.split('_')
                periodo = unir_cadenas('_', [datos[0],datos[1]])
                nomina = datos[2]

                datos_salida = [periodo, nomina, self.recibos[1][clave]]
                recibos.append(datos_salida)
        
        return [recibos, timbres]