import re


class Buscador:
    """Busca los caracteres dados en un texto"""

    def __init__ (self, caracter_buscado, texto):

        self.palabra =  caracter_buscado
        self.texto = texto 

        
    
    
    def buscar(self):  
        """Busca la cadena y retorna sus posiciones"""  
        self.posiciones = list()

        buscador = re.search(self.palabra, self.texto)
        
        if buscador:            
            
            return buscador.span()       
            
        else:
            pass
        