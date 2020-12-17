import datetime
from modulos.rutas import unir_cadenas




class RangoFechas():
    def __init__(self):

        self.dias = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', 
                        '21', '22', '23', '24', '25', '26', '27','28', '29', '30', '31'
                    ]

        self.meses = ['01', '02', '03', '04', '05', '06', '07', '08', 
                        '09', '10', '11', '12'
                        ]


    def armar_annos_incompletos(self, fecha, reverse=False):
        """Parametros fecha= [20,05,2020]
            Arma un año incompleto, devuelve los dias y meses
            que le faltan para el 31-12-2020 en este caso.(todos los mes son de 31 dias)
            ejemplo: 21-05-2020, 22-05-2020... 31-12-2020"""

        anno_con_meses_dias = list()
        
        dia = fecha[0]
        mes = fecha[1]
        anno = fecha[2]

        #primer mes dias que le faltan
        if reverse:
            ultimo_mes  = self.armar_dias_restantes(dia, mes, reverse=True)
            mes_limite = int(mes)-1
            mes_format = str(mes_limite).zfill(2)
            meses_restantes_completos = self.armar_meses_completos(1, mes_format)
        
            todos_los_meses = meses_restantes_completos + ultimo_mes

            for mes in todos_los_meses:

                fecha_con_meses = mes + '-' + anno

                anno_con_meses_dias.append(fecha_con_meses)

        else:
            mes_uno_dias = self.armar_dias_restantes(dia, mes) #arma el primer mes 
           
            meses_restantes_completos = self.armar_meses_completos(int(mes)+1)

            todos_los_meses = mes_uno_dias + meses_restantes_completos

            for mes in todos_los_meses:

                fecha_con_meses = mes + '-' + anno

                anno_con_meses_dias.append(fecha_con_meses)

        return anno_con_meses_dias






    def armar_annos_completos(self, anno_ini, anno_final):
        """Parametros año inicial = 2019 y año final= 2020
        Arma años con formato de dd-mm-aaa
        ejemplo: '01.01.2019', '02.01.2019'...'30.12.2020', '31.12.2020
        (todos los meses tienen 32 dias'"""

        annos_intermedios = list()

        for anno in range(anno_ini, anno_final+1):
                for mes in self.meses:
                    for dia in self.dias:
                        annos_intermedios.append(dia + '-'+ mes + '-' + str(anno))
        

        return annos_intermedios

    def armar_dias_restantes(self, dia_ini, mes, dia_final='31', reverse=False):
        """Argumentos: dia_ini = '05', mes = '05', reverse=False(cuenta de la fecha
            dada hacia el 01 del mes).(como cadenas)
            Retorna dias restantes de un mes en formato string:
            ejemplo, 05.05 devolveria desde '06-05' al '31-05',
            todos los meses los toma como de 31 dias"""
        
        dias_restantes = list()
        if reverse:
            for dia in range(1, int(dia_ini)):                
                dia_str = str(dia)

                dia_format = dia_str.zfill(2)

                mes_dias = dia_format + '-' + mes

                dias_restantes.append(mes_dias)

        
        else:
            for dia in range(int(dia_ini)+1, int(dia_final)+1):
                
                dia_str = str(dia)

                dia_format = dia_str.zfill(2)

                mes_dias = dia_format + '-' + mes

                dias_restantes.append(mes_dias)

        return dias_restantes

    def armar_meses_completos(self, mes_ini, mes_final='12'):
        
        """Arma los meses con 31 dias 
            Parametros mes_ini= '05'
            devolveria '01-05', '02.05'....'30.12', '31.12',
            todos los meses son de 31 dias"""

        
        meses_dias = list()


        for mes in range(int(mes_ini), int(mes_final)+1):
            for dia in self.dias:

                
                mes_str = str(mes)
                mes_format = mes_str.zfill(2)
                mes_con_dias = dia + '-' + mes_format
                meses_dias.append(mes_con_dias)
        
        return meses_dias

    def fecha_actual(self, hora=True):
        """Retona la fecha dia y mes actual en formato
            DD-MM-AAAA
        
        Parametros: hora=True Retorna con DD-MM-AAAA:HH-mm-ss"""


        fecha_s_formato =  datetime.datetime.now()
        dia = fecha_s_formato.strftime("%d")
        mes = fecha_s_formato.strftime("%m")
        anno = fecha_s_formato.strftime("%Y")
        hora = fecha_s_formato.strftime("%H")
        minuto = fecha_s_formato.strftime("%M")
        segundo = fecha_s_formato.strftime("%S")
        
        datos_fecha = [dia, mes, anno]
        datos_hora =[ hora, minuto, segundo]
        fecha = unir_cadenas('-', datos_fecha)  
        hora = unir_cadenas('-', datos_hora)    
        
        if hora:
            fecha_completa = fecha + ':' + hora
                
            
            
            return fecha_completa
        else:

            return fecha    
        
