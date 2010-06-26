class MayCJMGlobalesI(object):
#Region "Variables Globales"
    def __init__(self):
        self.nivel_actual = 4
        self.timermin = 0
        self.timerseg = 0
        #Tiempo de Espera para la Verificacion
        self.TMPEVeri = 1
        #Solamente es uno debido a que cuando se selcciona la segunda tarjeta, coordenadas ya no necesitan guardarse
        #ya que son las de ese mismo instante
        self.CoorSelecTar1 =(0,0)
        #Cuenta el Numero de veces que se da enter por jugada
        self.ConEnter = 0
        self.enEspera = False
        #Total de Tarjetas del Juego(Posiciones en Vector)
        self.Mod_totalTar = 24
        self.IniApli = True
        self.Nivelf=0
        self.Jugador=''
        self.noVentanas = 0
        self.VentanaActual=0
        #Impide que se vuelva a comparar que esta fuera del juego nuevamente, hasta que el cursor se mueva del 
        #lugar en donde esta estaba
        self.VeriVEsPR= False
        self.TableroCargar=None
        self.Tamano_Pantalla=(1000,650)
#End Region

#Region "Funciones y Metodos Globales"
    def AvanzarNvel(self,Nivelp):
        try:
            if (self.nivel_actual < 4) :
                self.nivel_actual += 1
                #Limpio los objetos del Tablero
                self.RemObjetos(Nivelp)
                Nivelp = None
                self.TableroCargar()
        except (NameError,ValueError):
            print "Error en AvanzarNvel" 

    def RemObjetos(self,Nivelp):
        X = Nivelp.CoorX
        Y = Nivelp.CoorY

        #Destruir Tarjetas
        while(Y>=0):
            while(X>=0):
                del Nivelp.Tarjetas[Y][X]
                X-=1
            X=Nivelp.CoorX
            Y-=1    

                
    def CNuevaPartida(self,p_frmTablero):
        Tablero=p_frmTablero
        try:
            Tablero.Timer1.Stop()
            Tablero.lbVerificaciona.Text = "Estado: "
            #Limpio los objetos del Tablero
            self.RemObjetos()
            self.Nivelf = 0
            Tablero.Cargar()
        except (NameError,ValueError):
            print "Error en CNuevaPartida"                 
#End Region
