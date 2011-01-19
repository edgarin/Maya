import pygame
from GlobalesI import *

##Esta Clase no esta en uso todavia
class MayCObjeto(object):
    def __init__(self,p_ID,p_Coordenadas,p_Tamano,p_Habilitado):
        #Propiedades
        self.ID = p_ID
        self.pos_x,self.pos_y = p_Coordenadas
        self.Ancho,self.Alto = p_Tamano
        self.Interface_Padre = pygame.display.get_surface()
        self.Habilitado = p_Habilitado
        #Indica si esta adentro de algun contenedor como un panel o Barra de Menu
        self.Contenedor = False
        self.EnFrente = False
        #Manejado por el Nucleo
        self.MNucleo = True
        #En que esta centrado si es que esta Centrado
        self.CentradoEn = ""
        
    def CEnFrente(self, valor):
        self.EnFrente = valor
    def ObtEnFrente(self):
        return self.EnFrente
        
    def CMNucleo(self,valor):
        #Manejado por el Nucleo
        self.MNucleo = valor
    def ObtMNucleo(self):
        #Manejado por el Nucleo
        return self.MNucleo
    
    def ObtIPadre(self):
        return self.Interface_Padre     
    def CInterfacePadre(self,p_Interface_Padre):
        #La Interface Padre sera otra Interface diferente de la Pantalla Principal
        self.Interface_Padre = p_Interface_Padre
        self.Contenedor = True
        self.Nucleo.Remover(self)
    
    def CPosenPantalla(self,valor):
        self.PosenPantalla = valor
            
    def ObtInterfacePadre(self):
        return self.Interface_Padre
    
    def ObtTamano(self):
        return self.Ancho,self.Alto    
    def CTamano(self,p_tamano):
        self.Ancho,self.Alto = p_tamano
    
    def ObtID(self):
        return self.ID    
    def CID(self,p_id):
        self.ID = p_id
        
    def ObtCoordenadas(self):
        return (self.pos_x,self.pos_y)    
    def CCoordenadas(self,p_coordenadas):
        self.pos_x,self.pos_y = p_coordenadas
        self.PosenPantalla = self.Nucleo.ObtPosicion((self.pos_x,self.pos_y))
                
    def Habilitar(self,p_Si_No):
        self.Habilitado = p_Si_No
    def ObtHabilitado(self):
        return self.Habilitado     
    
    def Centrar(self,p_Eje):
        w,h = Tamano_Pantalla
        
        if(p_Eje.lower() == "x"):
            self.pos_x = (w / 2) - (self.Ancho / 2)
            self.CentradoEn = p_Eje.lower()
        elif(p_Eje.lower() == "y"):
            self.pos_y = (h / 2) - (self.Alto / 2)
            self.CentradoEn = p_Eje.lower()
        else:
            print "Los ejes son solo X o Y"