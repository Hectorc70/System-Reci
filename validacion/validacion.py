

class ArchivosValidar():
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
        Salida: retorna un diccionario con clave = periodo+nomina+control+carpeta
        y como valor una lista vacia [] donde iran los nombres
        de los dos archivos xml y pdf.
        """

        archivos_unicos =  list()
        for archivo in rutas_archivos:
            archivo
            print(archivo)
        return