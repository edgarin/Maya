import pygame
class MayCJMGlobalesII(object):
#Region "Variables Globales"    
    def __init__(self):
        self.Imagenes=[]
        self.ClaseImagen=1
        self.ImagenTrasera=None
#End Region

#Region "Funciones y Metodos Globales"
    def AsignarTImagen(self): 
        if (self.ClaseImagen==1):
            #Imagen Trasera
            self.ImagenTrasera=pygame.image.load('./MayRecursos/MayJuegos/Memoria/Atras.jpg')
            #Imagenes Delantera
            self.Imagenes = self.ImagenesSeleccionadas('d')
        elif (self.ClaseImagen==2):
            #Imagen Trasera
            self.ImagenTrasera=pygame.image.load('./MayRecursos/MayJuegos/Memoria/AtrasSIMP.JPG')  
            #Imagenes Delantera
            self.Imagenes = self.ImagenesSeleccionadas('s')
        elif (self.ClaseImagen==3):
            #Imagen Trasera
            self.ImagenTrasera=pygame.image.load('./MayRecursos/MayJuegos/Memoria/AtrasYUGI.JPG')  
            #Imagenes Delantera
            self.Imagenes = self.ImagenesSeleccionadas('y')
        elif (self.ClaseImagen==4):
            #Imagen Trasera
            self.ImagenTrasera=pygame.image.load('./MayRecursos/MayJuegos/Memoria/AtrasCARR.JPG')
            #Imagenes Delantera
            self.Imagenes = self.ImagenesSeleccionadas('c')

        return self.Imagenes
    
    def ObtImagenTrasera(self):
        return self.ImagenTrasera
    
    def ImagenesSeleccionadas(self,parametro):
        Lista=[]
        a=1
        while (a<=25):
            imagen=pygame.image.load('./MayRecursos/MayJuegos/Memoria/'+parametro+''+str(a)+'.jpeg')          
            Lista.append(imagen)
            a+=1
        return Lista    
#End Region

