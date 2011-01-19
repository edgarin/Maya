from MayCNucleo import MayCNucleo
from MayCLabel import MayCLabel
from MayCBoton import MayCBoton
from MayCJMTablero import MayCJMTablero
from MayCPanel import MayCPanel
from MayMColores import *
import GlobalesI
import pygame

class MayCAcercaD(MayCPanel):
    def __init__(self):
        self.Nucleo = MayCNucleo()
        
        w,h = (250,120)
        wp,hp = GlobalesI.Tamano_Pantalla        
        px = (wp / 2) - (w / 2)
        py = (hp / 2) - (h / 2)

        MayCPanel.__init__(self,(px,py),(w,h))
        
        self.CColor(VERDE)
        self.CMsj(True);
        self.lbl1 = MayCLabel("Maya es un Juego Educativo", "lblIngresadas", (25, 25), "blanco")
        self.Adherir(self.lbl1)
        self.lbl2 = MayCLabel("Desarrollado en Guatemala", "lblIngresadas", (25, 50), "blanco")
        self.Adherir(self.lbl2) 
        
        bx = (w / 2) - (30 / 2)
        self.btnCerrar = MayCBoton('btnCerrar','No.png',p_Coordenadas = (bx,80),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
        self.btnCerrar.MensajeAyuda('Cerrar')
        self.btnCerrar.evtclick = self.Salir
        self.Adherir(self.btnCerrar)    
        
        self.Insertar()
        pygame.display.update()    
        self.run = True
        self.Ciclo();
    
    
    def Salir(self):
        self.Nucleo.RemObjetos()
        self.run = False
        
    def Ciclo(self):
        while self.run:
                evento = pygame.event.wait()
                if evento.type == pygame.QUIT:
                    self.Nucleo.Salir()
                    continue
                self.Nucleo.MEventos(evento)
                pygame.display.update()        
#a = MayCAcercaD()    
    