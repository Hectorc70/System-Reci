import pymysql


class Bdatos:
    def __init__(self, host, usuario, psword, nombre_bd):       
        self.host    = host
        self.usuario = usuario
        self.psw     = psword
        self.nombre_bd = nombre_bd
        self.conexion = pymysql.connect(self.host, self.usuario, self.psw, self.nombre_bd)
        self.cursor    = self.conexion.cursor()
        self.errores_guardado = dict()

    def insertar_filas(self, nombre_tabla, datos, campos):
        
        orden = "INSERT INTO {}({}) \
                VALUES({})".format(nombre_tabla, campos, datos)
        
        try: 
            self.cursor.execute(orden)
            self.conexion.commit()

            self.conexion.close()
        except pymysql.err.IntegrityError:
            self.errores_guardado[datos[0]] = datos
            pass
        

host = '127.0.0.1'
usuario = 'root'
psword = ''
bd_nombre = 'recibosnomina'

campos = 'id, control, periodo, anno, pagina, ruta'
datos = "'31821201202010', 318212, '01', '2020', 10, 'C:/pruebas/prueba.pdf'"

recibos = Bdatos(host, usuario, psword, bd_nombre)
recibos.insertar_filas('r2020', datos, campos)