
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


def armar_periodos(anno, periodo_ini ='01',ultimo_periodo='24', format=False):
    """Retorna el año con sus periodos
        tomando como base los periodos pasados
        como parametros, tanto como donde inicia y donde
        termina, por defecto son 24 periodos,
        los parametros deben ser en string
        
        format = True retorna dict{'2019':'201901' n...}
        format = False retorna dict{'2019':01 n...}"""

    periodos = list()
    anno_periodos = dict()

    for periodo in range(int(periodo_ini), int(ultimo_periodo)+1):

        if format:
            periodo_format = str(anno) + str("{:02d}".format(periodo))
        else:
            periodo_format = str("{:02d}".format(periodo))
        
        periodos.append(periodo_format)
    
    anno_periodos[anno] = periodos

    return anno_periodos



