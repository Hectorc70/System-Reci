import sqlite3


conec = 'C:\\pruebas\\mibdat-p.db'

class Bdatos:
    def __init__(self, coneccion):
        self.coneccion = sqlite3.connect(coneccion)
        self.cursor    = self.coneccion.cursor()

    def crear_tabla(self, nombre_tabla, campos):
        """Ejemplo: 'Recibos', ['control text,', 
                    'periodo text,', 'año text'])"""
        
        
        orden = "CREATE TABLE IF NOT EXISTS " + nombre_tabla + '(' 
        for campo in campos:
            orden = orden + campo
        orden = orden + ')'
        
        self.cursor.execute(orden)
        self.coneccion.commit()
        self.coneccion.close()
        

    def escribir_registros(self, nombre_tabla, registros, num_campos):
        orden = "INSERT INTO " + nombre_tabla + "VALUES (" + campos + "), " + registros

        
        self.cursor.executemany(orden)

        self.coneccion.commit()
        self.coneccion.close()
        
campos = ['control VARCHAR(8),', 'IDnomina VARCHAR(10),', 'periodo VARCHAR(2),', 'año VARCHAR(4),', 'pagina INTEGER(4),', 'ruta VARCHAR(300)']


recibos = Bdatos(conec)
recibos.crear_tabla('Recibos', campos)