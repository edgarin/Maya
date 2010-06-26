import random
from MayCJTarjeta import MayCJMTarjeta

class MayCJMNivel(object):
#Region "Constructor"
    def __init__(self,p_GlobalesI,p_GlobalesII):
        self.Nivel = p_GlobalesI.nivel_actual
        self.GlobalesI=p_GlobalesI
        self.GlobalesII=p_GlobalesII
        self.Tarjetas=[]
        self.LImagenes=[]
        self.CoorX=0
        self.CoorY=0
        self.ordenfinal= 0
        self.entableroX = 0
        self.entableroY = 0
        self.PicTamX = 0
        self.PicTamY = 0  
        self.verificacionNivel()

#Region "Funciones y Metodos"
    def ObtTarjetas(self):
        return self.Tarjetas
    def CTarjeta(self,p_tarjetas):
        self.Tarjetas = p_tarjetas

    def ObtNivel(self):
        return self.Nivel
    def CNivel(self,p_Nivel):
        self.Nivel = p_Nivel

    def ObtPicTamX(self):
        return self.PicTamX
    def CPicTamX(self,p_picTamX):
        self.PicTamX = p_picTamX
    
    def ObtPicTamY(self):
        return self.PicTamY
    def CPicTamY(self,p_picTamY):
        self.PicTamY = p_picTamY
    
    def ObtentableroX(self):
        return self.entableroX
    def CentableroX(self,p_entableroX):
        self.entableroX = p_entableroX
        
    def ObtentableroY(self):
        return self.entableroY
    def CentableroY(self,p_entableroY):
        self.entableroY = p_entableroY                
                
    def verificacionNivel(self):
        Nivel = self.Nivel

        if (Nivel==1):
            self.ManipuTarjetas(3, 3)
            self.entableroX = 270
            self.entableroY = 45
            self.PicTamX = 100
            self.PicTamY = 120        
        elif (Nivel==2):
            self.ManipuTarjetas(5, 4)
            self.entableroX = 215
            self.entableroY = 25
            self.PicTamX = 80
            self.PicTamY = 100
        elif (Nivel==3):
            self.ManipuTarjetas(7, 4)
            self.entableroX = 120
            self.entableroY = 25
            self.PicTamX = 80
            self.PicTamY = 100
        elif (Nivel==4):
            self.ManipuTarjetas(9, 4)
            self.entableroX = 50
            self.entableroY = 37
            self.PicTamX = 75
            self.PicTamY = 95

    def ManipuTarjetas(self,coorX,coorY ):
        try:
            self.CoorX = coorX
            self.CoorY = coorY

            #No de Tarjetas en Juego
            tarjejue = ((coorX + 1) * (coorY + 1))
            self.ManiTarjetas(tarjejue)

            contador_im = 0

            for y in range(coorY+1):
                ListaCartas=[]
                for x in range (coorX+1):
                    #Asignar Imagenes Delanteras
                    tarjeta= MayCJMTarjeta(self.GlobalesII.ObtImagenTrasera(), self.LImagenes[contador_im], (self.ordenfinal[contador_im] - 1), False)
                    ListaCartas.append(tarjeta)
                    contador_im += 1
                self.Tarjetas.append(ListaCartas)     
        except (NameError,ValueError):
            print ("Ocurrio un Error ManipuTarjetas")

    def ManiTarjetas(self, totalima):
        try:
            MitadTarjetas = totalima / 2
            self.ordenfinal = self.ObtOrden((totalima-1), MitadTarjetas)

            imagenes = []

            #Asigno todas las imagenes disponibles a imagenes con la funcion Siguiente 
            imagenes = self.GlobalesII.AsignarTImagen()

            for a in range (totalima): 
                self.LImagenes.append(imagenes[(self.ordenfinal[a] - 1)])

        except (NameError,ValueError):
            print ("Ocurrio un Error")

    def ObtOrden(self, totalima1, MidTar):
        aleanu = []
        Contador = 0

        numero=0
        existe = False

        while (Contador <= totalima1):
            #random.randint(a, b)
            #Return a random integer N such that a <= N <= b
            numero = random.randint(1, (totalima1+1))

            if (Contador == 0):
                aleanu.append(numero) 
                Contador += 1

            for a in range(Contador):
                if (numero == aleanu[a]):
                    existe = True
                    break

            if (existe == False):
                aleanu.append(numero) 
                Contador += 1
            existe = False

        for a in range((totalima1+1)):
            if(aleanu[a] > MidTar):
                aleanu[a]=aleanu[a] - MidTar
            else:
                aleanu[a]=aleanu[a]
             
        return aleanu

    def VeriTarjetas(self, SelecTarjeta1,SelecTarjeta2,p_Nivel,lblestado) :
        if (SelecTarjeta1.NoTarjeta == SelecTarjeta2.NoTarjeta):
            lblestado.Text('Estado: Las Cartas Coinciden! :)')
            #El estado indica que ya fueron Descubiertas las cartas seleccionadas, y que son iguales
            SelecTarjeta1.CEstado (True)
            SelecTarjeta2.CEstado (True)
            #Impide que se vuelva a comparar que esta fuera del juego nuevamente, hasta que el cursor se mueva del 
            #lugar en donde esta estaba
            #Mientras sea true no se podra presionar enter hasta que se mueva el cursor de dicha carta
            self.GlobalesI.VeriVEsPR = True
            #Comprabacion, Finalizacion de Nivel
            self.FinalizacionN(p_Nivel)
            return True
        else:
            lblestado.Text('Estado: Las Cartas No Coinciden :(')
            SelecTarjeta1.RegresoVolteoTarjeta()
            SelecTarjeta2.RegresoVolteoTarjeta()
            return False


    def FinalizacionN(self,Nivelp):
        X  = Nivelp.CoorX
        Y = Nivelp.CoorY

        #Si encuentra una Tarjeta en Estado=False(No descubierta) se sale del sub y no se avanza de nivel
        for b in range((Y+1)):
            for a in range((X+1)):
                if(Nivelp.Tarjetas[b][a].Estado == False): 
                    return

        self.GlobalesI.AvanzarNvel(Nivelp)
#End Region
