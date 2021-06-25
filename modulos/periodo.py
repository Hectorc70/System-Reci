
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
        self.all_periods_format  =list()


    def to_create_all_periods(self):
        """
        Retorna lista de todos los periodos
        los parametros deben ser en string
        retorna ['201901', '201902' n...]
        """


        for period in range(int(self.period_initial), int(self.period_final)+1):
            periodo_f = PeriodFormat(period, self.year)
            periodo_format = periodo_f.period_format

            self.all_periods_format.append(periodo_format)
    





def get_interim_periods(year_ini, year_final):
    """Retorna los periodos de los años intermedios del rango pasado 
    como parametro.  
    ejemplo: anno_ini='2017', anno_final='2020'.    
    
    Retorna: list['201801','201802',n...,'201901','20190102',n...].
    """
    years = list()
    years_all = list()

    for year in range(int(year_ini)+1, int(year_final)): 
        year_f = YearFormatPeriodos(year)
        year_f.to_create_all_periods()
        
        years.append(year_f.all_periods_format)
    

    for list_year in years:
        years_all = years_all + list_year
    
    return years_all

