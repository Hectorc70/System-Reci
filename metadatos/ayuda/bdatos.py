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
    
    
    def crear_tabla(self, tabla):
        orden = "CREATE TABLE {}.{}('id' VARCHAR(100) NOT NULL ,'control' INT(8) \
                NOT NULL, 'periodo'VARCHAR(2), 'anno' VARCHAR(4) NOT NULL, \
                'ruta' VARCHAR(300) NOT NULL, PRIMARY KEY('id'))"
    
    def insertar_filas(self, nombre_tabla, campos, datos):
        if nombre_tabla:
            orden = "INSERT INTO {}({}) \
                    VALUES({})".format(nombre_tabla, campos, datos)

            try: 
                self.cursor.execute(orden)
                self.conexion.commit()

                self.conexion.close()
            except pymysql.err.IntegrityError:
                self.errores_guardado[datos[0]] = datos
                pass
        else:
            

        


campos = 'id, control, periodo, anno, pagina, ruta'
datos = "'31821201202010', 318212, '01', '2020', 10, 'C:/pruebas/prueba.pdf'"

""" recibos = Bdatos(host, usuario, psword, bd_nombre)
recibos.insertar_filas('r2020', datos, campos) """