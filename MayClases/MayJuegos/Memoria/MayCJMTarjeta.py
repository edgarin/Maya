from MayCBoton import MayCBoton
class MayCJMTarjeta(object):
    #Region "Constructor"
    def __init__(self,p_imagentrasera, p_imagendelantera,p_notarjeta,p_Estado):
        self.ImagenTrasera = p_imagentrasera 
        self.ImagenDelantera = p_imagendelantera
        self.BtnTarjeta = MayCBoton(None,None,None,None)
        self.NoTarjeta = p_notarjeta
        self.Estado = p_Estado
        self.IndY,self.IndX=(0,0)
    #End Region

    def Insertar(self,p_Interface):
        self.BtnTarjeta.Insertar(p_Interface=p_Interface)
    #Importante los Eventos solo pueden ser llamados desde una propiedad

#Region "Funciones y Metodos"
    def ObtImagenTrasera(self):
        return self.ImagenTrasera
    def CImagenTrasera(self,p_imagentrasera):    
        self.ImagenTrasera = p_imagentrasera
        
    def ObtImagenDelantera(self):
        return self.ImagenDelantera    
    def CImagenDelantera(self,p_pimagendelantera):
        self.ImagenDelantera = p_pimagendelantera
                
    def ObtPicTarjeta(self):
        return self.BtnTarjeta
    def CPicTarjeta(self,p_BtnTarjeta):
        self.BtnTarjeta = p_BtnTarjeta

    def ObtNoTarjeta(self):
        return self.NoTarjeta
    def CNoTarjeta(self,p_pnotarjeta):
        self.NoTarjeta = p_pnotarjeta

    def ObtEstado(self):
        return self.Estado
    def CEstado(self,p_Estado):
        self.Estado = p_Estado

    def ObtIndices(self):
        return self.IndY,self.IndX
    def CIndices(self,p_Indices):
        self.IndY,self.IndX = p_Indices
            
    def PresionDRaton(self,p_Evento):
        if(self.BtnTarjeta.Busqueda(p_Evento.pos, (0,0))):
            return True
    
    def MovimientoDRaton(self,p_Evento):
        if(self.BtnTarjeta.Busqueda(p_Evento.pos, (0,0))):
            return True
                                
    def VolteoTarjeta(self):
        self.BtnTarjeta.CImagen(p_imagen=self.ImagenDelantera) 

    def RegresoVolteoTarjeta(self):
        self.BtnTarjeta.CImagen(p_imagen=self.ImagenTrasera) 
#End Region