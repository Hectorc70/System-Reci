import base64
from os.path import exists
from os import startfile
from os import getpid
import tempfile
import base64

import eel
import os.path

from login.login import User, ArchivoTemp, Token

from modulos.rutas import (
    crear_directorio,
    abrir_directorio,
    abrir_archivo,
    unir_cadenas)

from modulos.periodo import YearFormatPeriodos, get_interim_periods

from modulos.log import Log

from respaldar.reci_xml import TimbreCop, ReciboCop
from respaldar.originales import ArchivoTimbre, ArchivoRecibo, ArchivosOrig

from validacion.validacion import ArchivosPorValidar, ArchivosValidados

from subir.cliente import Cliente
from subir.empleado import DatosEmpleados
from subir.recibo import RutaRecibo

from buscador.cliente import ClienteBuscador


from herramientas.directorio import Directorio
eel.init('web_folder', allowed_extensions=['.js', '.html'])

file_data_user = ArchivoTemp()


"""
**---------------------------------------------------------------------------------------------**
                        ***GENERALES***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def enviar_ruta():
    directorio = abrir_directorio()

    if exists(directorio):
        return directorio
    else:
        return ''


@eel.expose
def enviar_ruta_archivo():
    ruta = abrir_archivo()

    return ruta


"""
**---------------------------------------------------------------------------------------------**
                        ***RESPALDAR XML Y RECIBOS***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def enviar_rutas(ruta, periodo, anno):
    rutas_timbres = rutas_timbres_orig(ruta, periodo, anno)
    rutas_recibos = rutas_recibos_orig(ruta, periodo, anno)

    return [rutas_timbres, rutas_recibos]


@eel.expose
def rutas_timbres_orig(ruta, periodo, anno):

    originales = ArchivoTimbre(ruta, periodo, anno)
    timbres = originales.recuperar_timbres()

    return timbres


@eel.expose
def rutas_recibos_orig(ruta, periodo, anno):

    originales = ArchivoRecibo(ruta, anno, periodo)
    recibos = originales.recuperar_recibos()

    return recibos


@eel.expose
def respaldar(tipo, carpeta_origen, ruta_archivo, carpt_dest, periodo, anno):

    if tipo == 'timbres':
        respaldar_timbres(carpeta_origen, carpt_dest, ruta_archivo)

    elif tipo == 'recibos':
        respuesta = respaldar_recibos(
            carpeta_origen, ruta_archivo, carpt_dest, periodo, anno)

        return respuesta


@eel.expose
def respaldar_timbres(carpeta_origen, carpt_dest, archivo,):
    timbre = TimbreCop(carpeta_origen, carpt_dest)
    timbre.copiado_archivos(archivo)


@eel.expose
def respaldar_recibos(carpeta_original, ruta_archivo, carpt_destino, periodo, anno):
    periodo_copiado = ArchivoTimbre(carpt_destino, periodo, anno)
    timbres_nombres = periodo_copiado.recuperar_timbres_nombres()

    if timbres_nombres:
        reci = ReciboCop(carpeta_original, ruta_archivo, carpt_destino)
        reci.separar_en_recibos(timbres_nombres)
        return ['EXITOSO', True]
    else:
        return ['ERROR', True]


@eel.expose
def leer_log_recibos():
    try:
        log = Log('Log-copiado-Recibos.txt')
        errores = log.devolver_datos('ERROR')
        if errores:

            return ['ERRORES', True]

        else:
            return [' ', True]
    except FileNotFoundError:
        return [' ', True]

    except:
        return[' ', False]


"""
**---------------------------------------------------------------------------------------------**
                        ***VALIDAR XML Y RECIBOS***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def mostrar_archivos(ruta, anno, periodo):
    archivos_orig = ArchivosOrig(ruta, periodo, anno)

    rutas = archivos_orig.depurar_rutas()

    recibo = ArchivosPorValidar(ruta, rutas[0])
    recibos = recibo.depurar_archivos()

    timbre = ArchivosPorValidar(ruta, rutas[1])
    timbres = timbre.depurar_archivos()

    return [recibos, timbres]


@eel.expose
def validar_archivos(timbres, recibos):

    archivos = ArchivosValidados(timbres, recibos)

    archivos_validados = archivos.validar()

    return archivos_validados


"""
**---------------------------------------------------------------------------------------------**
                        ***ALMACENAR DATOS EN BASE DE DATOS***
**---------------------------------------------------------------------------------------------**
"""

# RECIBOS DE NOMINA


@eel.expose
def mostrar_rutas_recibos(directorio, anno, periodo):
    ruta_archivos = RutaRecibo(directorio, anno, periodo)
    rutas = ruta_archivos.recuperar_periodo()

    return rutas


@eel.expose
def guardar_mdatos_recibos(datos_archivos_pdf):
    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()

        for datos in datos_archivos_pdf:
            control = int(datos[0].split('_')[0])
            datos_format = {
                'archivo': datos[0],
                'ruta': datos[-1],
                'periodo': datos[1],
                'nomina': datos[2],
                'control': str(control)
            }

            cliente = Cliente(token[1])
            cliente.enviar_datos_recibo(datos_format)

        return True
    else:
        return 'ERROR'


@eel.expose
def leer_log_recibos_subidos():
    try:
        log = Log('Log_Send_Recibos_Data.txt')
        errores = log.devolver_datos('ERROR')
        if errores:
            log.abrir_log()
            return ['ERRORES', True]

        else:
            return [' ', True]
    except FileNotFoundError:
        return [' ', True]

    except:
        return[' ', False]

# EMPLEADOS


@eel.expose
def mostrar_datos_empleados(ruta):

    empleados = DatosEmpleados(ruta)
    datos = empleados.leer_datos_empleados()

    return datos


@eel.expose
def subir_datos_empleados(datos_empleados):
    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()

        for datos in datos_empleados:
            datos_format = {
                'control': datos[0],
                'nombre': datos[1],
                'ape_p': datos[2],
                'ape_m': datos[3],
            }

            cliente = Cliente(token[1])
            cliente.enviar_datos_empleado(datos_format)

        return ''
    else:
        return 'ERROR'


@eel.expose
def leer_log_empleados_subidos():
    try:
        log = Log('Log_Send_Empleados_Data.txt')
        errores = log.devolver_datos('ERROR')
        if errores:
            log.abrir_log()
            return ['ERRORES', True]

        else:
            return [' ', True]
    except FileNotFoundError:
        return [' ', True]

    except:
        return[' ', False]


"""
**---------------------------------------------------------------------------------------------**
                        ***BUSCADOR***
**---------------------------------------------------------------------------------------------**
"""


def comprobar_fechas(**kwargs):
    """Busca recibos de los periodos
    indicados pasados como parametros"""

    all_periods = []

    if kwargs['year_ini'] == kwargs['year_f']:
        year_periods = YearFormatPeriodos(
            year=kwargs['year_ini'],
            period_initial=kwargs['period_ini'],
            period_final=kwargs['period_f']
        )
        year_periods.to_create_all_periods()

        return year_periods.all_periods_format

    elif int(kwargs['year_ini']) + 1 == int(kwargs['year_f']):

        year_ini = YearFormatPeriodos(
            year=kwargs['year_ini'],
            period_initial=kwargs['period_ini']
        )
        year_f = YearFormatPeriodos(
            year=kwargs['year_f'],
            period_final=kwargs['period_f']
        )
        
        year_ini.to_create_all_periods()
        year_f.to_create_all_periods()


        year_periods_all = year_ini.all_periods_format + \
            year_f.all_periods_format

        return year_periods_all

    else:
        year_ini = YearFormatPeriodos(
            year=kwargs['year_ini'],
            period_initial=kwargs['period_ini']
        )

        year_periods_all_int = get_interim_periods(
            kwargs['year_ini'],
            kwargs['year_f'])

        year_f = YearFormatPeriodos(
            year=kwargs['year_f'],
            period_final=kwargs['period_f']
        )


        year_ini.to_create_all_periods()
        year_f.to_create_all_periods()

        year_periods_all = year_ini.all_periods_format + \
            year_periods_all_int + year_f.all_periods_format

        return year_periods_all


@eel.expose
def recuperar_por_control(control, period_i, year_ini, period_f, year_f):
    
    years_periods = comprobar_fechas(year_ini=year_ini, period_ini=period_i,
                                    period_f=period_f, year_f=year_f)

    resp = recuperar_datos(years_periods, control)

    print(resp)


def formatear_datos(periodos_datos_recibos):
    for datos_recibos in periodos_datos_recibos:
        for keys in datos_recibos.keys():
            id_recibo = datos_recibos['id_recibo']
            control = datos_recibos['no_control']
            periodo = datos_recibos['periodo']
            nomina = datos_recibos['tipo_nomina']

            return [id_recibo, control, periodo, nomina]


def recuperar_datos(years_periods, control):
    datos_recuperados = list()

    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()
        cliente = ClienteBuscador(token[1])

        for anno in years_periods:
            for periodos in anno.values():
                for periodo in periodos:
                    resp = cliente.recuperar_datos_recibo(control, periodo)
                    if resp[0] == 200:
                        datos_format = formatear_datos(resp[1])
                        datos_recuperados.append(datos_format)

    return datos_recuperados


def recuperar_datos_int(annos_int, control):
    datos_recuperados = list()

    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()
        cliente = ClienteBuscador(token[1])

        for anno in annos_int:
            for _anno in anno:
                for periodo in _anno.values():
                    resp = cliente.recuperar_datos_recibo(control, periodo)
                    if resp[0] == 200:
                        datos_format = formatear_datos(resp[1])
                        datos_recuperados.append(datos_format)

    return datos_recuperados


@eel.expose
def recuperar_recibo(id_recibo):
    """llama al metodo que retorna el recibo
    de nomina con el id pasado como parametro
    """

    data = file_data_user.get_data_user()

    if data or data == ['']:
        user = Token(data[0], data[1])
        token = user.get_token_user()
        cliente = ClienteBuscador(token[1])

        resp = cliente.recuperar_recibo(id_recibo)

        if resp[0] == 200:

            """ pdf_salida = PdfFileWriter()
            pdf_salida.addPage(resp[1])	

            nombre_archivo ='nombre_pdf' + '.pdf'
            with open(nombre_archivo,'wb') as fp: 
                pdf_salida.write(fp)	 """

            return resp


@eel.expose
def descargar_recibo(data):
    data_format = data.split(',')
    nombre_recibo = unir_cadenas(
        '_', [data_format[0], data_format[1], data_format[2], data_format[3]])
    resp = recuperar_recibo(data_format[0])

    if resp[0] == 200:
        directorio = enviar_ruta()
        if directorio != '':

            directorio_comp = unir_cadenas(
                '\\', [directorio.replace('/', '\\'), data_format[1]])
            crear_directorio(directorio_comp)
            ruta_completa = unir_cadenas(
                '\\', [directorio_comp, nombre_recibo])

            with open(ruta_completa + '.pdf', "wb") as f:
                f.write(base64.b64decode(resp[1]))

            return [1, 'Se guardo en {}'.format(directorio_comp)]
        else:
            return [0, 'No se selecciono Ruta Intentente Nuevamente']
    else:
        return [0, 'Error {} Intente nuevamente'.format(str(resp[0]))]


"""
**---------------------------------------------------------------------------------------------**
                        ***CONFIG EEL***
**---------------------------------------------------------------------------------------------**
"""


@eel.expose
def login_user(control, password):

    user = User()
    resp = user.get_database_user(control, password)
    if resp[0] == 200:
        file_data_user.save_data_user(control, password)

    return resp


try:
    opciones = [{'size': (1080, 720)}]

    eel.start('login.html', port=8080)


except(SystemExit, MemoryError, KeyboardInterrupt):
    pass

print("ventana cerrada")
