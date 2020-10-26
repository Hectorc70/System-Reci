import os
from os.path import exists
from os import makedirs

from tkinter.filedialog import askdirectory, askopenfilename



class Rutas():
    """Recupera rutas de una carpeta dada"""       
        


    def recuperar_rutas(self, carpeta, split = False):         
        rutas = list()        

        if split:

            for ruta, carpetas, archivos in os.walk(carpeta, topdown = True):          
            
                for archivo in archivos:
                    
                    ruta_full = self.ruta_completa(ruta, archivo)
                    ruta_split = dividir_cadena('\\',ruta_full)
                    rutas.append(ruta_split)
        
        elif split == False:
            for ruta, carpetas, archivos in os.walk(carpeta, topdown = True):          
            
                for archivo in archivos:
                    
                    ruta_full = self.ruta_completa(ruta, archivo)                
                    rutas.append(ruta_full)
        
        return rutas
        

    def recuperar_carpetas(self, carpeta, carpeta_1 = False):
        carpetas_recuperadas = list()

        if carpeta_1:
            for ruta, carpetas, archivos in os.walk(carpeta,topdown = True):
                for carpeta in carpetas:
                    ruta_full = self.ruta_completa(ruta, carpeta)                
                    carpetas_recuperadas.append(ruta_full)
                break    

        elif carpeta_1 == False:
            for ruta, carpetas, archivos in os.walk(carpeta,topdown = True):          
            
                for carpeta in carpetas:
                    
                    ruta_full = self.ruta_completa(ruta, carpeta)                
                    carpetas_recuperadas.append(ruta_full)
        
        
        return carpetas_recuperadas

                    
     
    
    def ruta_completa(self, ruta, archivo ):
        """Devuelve la ruta completa. Ejemplo: entrada(ruta='C:/documents', archivo='ejemplo.txt'),
        salida(ruta_completa='C:\\documents\\ejemplo.txt')"""

          
        ruta_completa = ruta.replace('/','\\')+ "\\" + archivo
            
        return ruta_completa


def dividir_cadena(separador, cadena):

    cadena_split = cadena.split(separador)

    return cadena_split

    
def unir_cadenas(separador, lista_datos):
    """Une una lista en un string solo, 
        los datos deben ser string.

        Parametros  separador='|', 
        lista_datos= [dato1, dato2, daton...]"""
  
    cadena = separador.join(lista_datos)
    return cadena

def comprobar_rutas(ruta):

    if exists(ruta):
        return True
    else:
        return False


def abrir_archivo():
    ruta = askopenfilename() 

    return ruta

def abrir_directorio():
    ruta = askdirectory()

    return ruta

def crear_directorio(directorio):
    ruta = comprobar_rutas(directorio)

    if not ruta:
        os.makedirs(directorio)