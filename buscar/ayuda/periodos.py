
def armar_periodos_intermedios(anno_ini, anno_final):
    """Retorna los periodos intermedios de un rango de 
    periodos los parametros puden ser como string.
    """
    annos = list()


    for anno in range(int(anno_ini)+1, int(anno_final)): 

        periodos = armar_periodos(anno)

        annos.append(periodos)
    return annos


def armar_periodos(anno, periodo_ini ='01',ultimo_periodo='24'):
    """Retorna el año con sus periodos
        tomando como base que el tope del periodo pasado
        como parametro por defecto son 24 periodos
        los parametros pueden ser en string"""

    periodos = list()
    anno_periodos = dict()

    for periodo in range(int(periodo_ini), int(ultimo_periodo)+1):
        periodo_format = str("{:02d}".format(periodo))
        
        periodos.append(periodo_format)
    
    anno_periodos[anno] = periodos

    return anno_periodos

