'''
Created on 23/08/2010

@author: danielz360
'''
import thread
import time
from MayCNucleo import MayCNucleo

class MayCReloj(object):
    def __init__(self,tick = None, metodo = None):
        self.Nucleo = MayCNucleo()
        self.tick = tick
        self.run = True
        self.metodo = metodo
        #Tipo de Objeto
        self.T_Objeto = 'Etiqueta'
        self.Nucleo.CReloj(self)
        self.RParar = False
        
    def Comenzar(self):
        self.run = True
        # Lanzamos el hilo
        thread.start_new_thread(self.Hilo, ())
    
    def Terminar(self):
        self.run = False
        #self.Parar()
        time.sleep(1)
    
    def Continuar(self):
        self.RParar = False
            
    def Parar(self):
        self.RParar = True
            
    def Hilo(self):
        while (self.run):
            time.sleep(self.tick)
            if(self.RParar == True):
                continue

            self.metodo()
            
    