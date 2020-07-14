import sqlite3


conec = 'C:\\pruebas\\mibdat-p.db'

class Bdatos:
    def __init__(self, coneccion):
        self.coneccion = sqlite3.connect(coneccion)
        self.cursor    = self.coneccion.cursor()

    def crear_tabla(self, nombre_tabla, campos):
        """Ejemplo: 'Recibos', 'control text,', 
                    'periodo text,', 'año text')"""
        
        
        orden = "CREATE TABLE IF NOT EXISTS " + nombre_tabla + '(' 
        for campo in campos:
            orden = orden + campo
        orden = orden + ')'
        
        self.cursor.execute(orden)
        self.coneccion.commit()
        

    def escribir_datos(self):
        pass
campos = ['control VARCHAR(8),', 'IDnomina VARCHAR(10),', 'periodo VARCHAR(2),', 'año VARCHAR(4),', 'pagina INTEGER(4),', 'ruta VARCHAR(300)']


recibos = Bdatos(conec)
recibos.crear_tabla('Recibos', campos)