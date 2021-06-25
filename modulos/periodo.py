
from typing import ClassVar



class PeriodFormat():

    def __init__(self, period, year):

        self.period        = period
        self.year           = year
        self.period_format = self.__format_period()

    def __format_period(self):
        period_format = str(self.year) + str("{:02d}".format(self.period))

        return period_format


class YearFormatPeriodos():
    """Clase que arma los periodos del año 
        pasado como parametro y del  rango de periodos
        pasados como parametro por default son init=01, final=24"""


    def __init__(self, year, period_initial='01', period_final='24'):
        self.period_initial = period_initial
        self.period_final   = period_final
        self.year           = year

    def to_create_all_periods(self):
        """
        Retorna lista de todos los periodos
        los parametros deben ser en string
        retorna ['201901', '201902' n...]
        """
        all_periods_format = []

        for period in range(int(self.period_initial), int(self.period_final)+1):
            periodo_f = PeriodFormat(period, self.year)
            periodo_format = periodo_f.period_format

            all_periods_format.append(periodo_format)
    





def armar_periodos_intermedios(anno_ini, anno_final, format):
    """Retorna los periodos de los años intermedios del rango pasado 
    como parametro.  
    ejemplo: anno_ini='2017', anno_final='2020'.    
    
    format = False, Retorna: list({'2018':['01','02',n...]},{'2019':['01','02',n...]}).

    format = True, Retorna: list({'2018':['201801','201802',n...]},{'2019':['201901','201902',n...]})
    """
    annos = list()


    for anno in range(int(anno_ini)+1, int(anno_final)): 

        periodos = armar_periodos(anno,format=format)

        annos.append(periodos)
    return annos


