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
            
            print("Se ha encontrado la palabra:")
            self.posiciones.append(buscador.span())            
            return buscador.span()
        else:
            print("No se ha encontrado la palabra:", self.texto)
    
        return self.posiciones