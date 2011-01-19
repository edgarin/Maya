'''
Created on 24/08/2010

@author: danielz360
'''
import pygame
from pygame.locals import *
from MayCNucleo import MayCNucleo
from MayCObjeto import MayCObjeto
from MayCReloj import MayCReloj
from MayMColores import *

class MayCCuaTexto(MayCObjeto):
    def __init__(self,p_ID, p_Coordenadas = (0,0),p_Ancho = 200, p_Fuente = 'arial', p_Texto = '' ,p_Habilitado = True):
        self.Nucleo = MayCNucleo()
        self.Texto = p_Texto
        self.TFuente = p_Fuente
        self.CLetra = NEGRO
        self.CFondo = BLANCO
        self.Ancho = p_Ancho
        self.Interface = self.Render() 
        self.T_Objeto = 'CuadroTexto'
        self.Raton_Dentro = False
        self.Raton_Click = False
        self.Mensaje_Ayuda = ''
        self.con = 0
        self.Mayus = False
        
        p_Tamano = (p_Ancho,self.Interface.get_height())
        MayCObjeto.__init__(self,p_ID,p_Coordenadas,p_Tamano,p_Habilitado)
        self.PosenPantalla = self.Nucleo.ObtPosicion((self.pos_x,self.pos_y))
        self.Nucleo.Agregar(self)
        
    def ObtFuente(self):
        return self.TFuente
    def CFuente(self,p_valor):
        self.TFuente = p_valor
        self.Interface = self.Render()

    def ObtTexto(self):
        return self.Texto
    def CTexto(self, p_valor):
        self.Texto = p_valor
        self.Interface = self.Render()
   
    def ObtCLetra(self):
        return self.CLetra
    def CCLetra(self,p_valor):
        self.CLetra = p_valor
        self.Interface = self.Render()    
    
    def ObtCFondo(self):
        return self.CFondo
    def CCFondo(self,p_valor):
        self.CFondo = p_valor
        self.Interface = self.Render()        
        
    def CAncho(self,p_valor):
        self.Ancho = p_valor
        self.Interface = self.Render()       

    def ObtInterface(self):
        return self.Interface    
    
    def MensajeAyuda(self,Mensaje):
        Fuente_Mensaje = pygame.font.SysFont("arial", 11)
        #(0,0,0)=>Color de Letra (150,155,175)=>Color Fondo 
        #Font.render() devuelve una surface
        self.Mensaje_Ayuda = Fuente_Mensaje.render(Mensaje, True, (0, 0, 0), (150, 155, 175))    
    def ObtenerMensaje(self):
        return self.Mensaje_Ayuda  
    
    def Negrita(self, p_valor = False):
        """
            Habilita el dibujado de la fuente en Negrita mientras que esta
            lo soporte, en caso contrario pygame emula dicho modo.
        """
        self.Fuente.set_bold(value)
     
        
    def Cursiva(self, p_valor = False):
        """
            Habilita la imitacion que da de texto en cursiva, por ende como en
            el caso de bold() el tipo de fuente tiene que poder soportar el 
            mismo.        
        """
        self.Fuente.set_italic(value)
    
    def AgregarMensaje(self,p_Interface = None):
        if(self.Mensaje_Ayuda == '' or self.Raton_Dentro == False):
            return
        PantallaPrincipal = pygame.display.get_surface()
        if (p_Interface == None):
            PantallaPrincipal.blit(self.Mensaje_Ayuda,self.Pos_Mensaje)
        else:
            p_Interface.blit(self.Mensaje_Ayuda,self.Pos_Mensaje)
                    
    def Render(self):
        self.Fuente = pygame.font.SysFont(self.TFuente, 16)
        
        texto = self.Texto
        condicion = True
        
        while(condicion):
            w,h = self.Fuente.size(texto)
            if(w >= (self.Ancho - 5) ):
                if(self.caracter != 'del'):
                    self.con += 1

                texto = texto[self.con:]
            else:
                condicion = False
        
        Render = self.Fuente.render(texto, True, self.CLetra)
        return Render  
    
    def Insertar(self,p_Interface = None):
        if (p_Interface == None):
            if(self.Contenedor != True):
                self.Nucleo.Insertar(self)
            else:
                self.Dibujar(self.Interface_Padre,(self.pos_x,self.pos_y))
        else:
            self.Dibujar(p_Interface,(self.pos_x,self.pos_y))
        
    def Dibujar(self, p_InterfacePadre, p_Posicion):
        pos_x,pos_y = p_Posicion
        InterfacePadre = p_InterfacePadre
        w,h = self.Interface.get_size()
        
        rect = (pos_x,pos_y,self.Ancho,h)
        
        pygame.draw.rect(InterfacePadre, self.CFondo, rect, 0) #fondo
        InterfacePadre.blit(self.Interface, (self.pos_x + 3, self.pos_y))
        pygame.draw.rect(InterfacePadre, self.CLetra, rect, 2) #borde    
        
        if (self.Raton_Click == False):
            return
        x1 = w + pos_x + 5
        y1 = pos_y
        pygame.draw.rect(InterfacePadre, self.CLetra,((x1,y1+3),(1,h-6)), 0)
        
    def Busqueda(self,posicion_click,p_posInterPadre = (0,0)):
        pos_x2,pos_y2 = posicion_click
        #Se saca la posicion en relacion a la Pantalla Principal
        pospadrex,pospadrey = p_posInterPadre
        
        #Esta posicion se hace en relacion a un MenuSuperior o MenuLateral, si no hay los valores eran
        #iguales a self.pos_x  y  self.pos_y
        posxnp,posynp = self.PosenPantalla
        
        w,h = self.Interface.get_size()
        
        if(self.Contenedor == True):
            pos_x = pospadrex + self.pos_x
            pos_y = pospadrey + self.pos_y
        else:
            pos_x = pospadrex + posxnp
            pos_y = pospadrey + posynp    
                
        if ((pos_x2 >= pos_x and pos_x2 <= (pos_x + self.Ancho)) and (pos_y2 >= pos_y and pos_y2 <= (pos_y + h))):
            return True    
    
    def MovimientoDRaton(self,p_Evento,npos = False,p_posInterPadre = (0,0)):
        if(npos == True):
            self.PosenPantalla = self.Nucleo.ObtPosicion(( self.pos_x , self.pos_y ))
        
        evento = p_Evento
        if(self.Busqueda(evento.pos,p_posInterPadre = p_posInterPadre) == True and self.Raton_Dentro == False):
            self.Raton_Dentro = True
            self.Pos_Mensaje = evento.pos
            return True
        elif(self.Busqueda(evento.pos,p_posInterPadre = p_posInterPadre) != True and self.Raton_Dentro == True):
            self.Raton_Dentro = False
            return True
    
    def PresionDRaton(self,p_Evento,npos = False,p_posInterPadre = (0,0)):
        if(npos == True):
            self.PosenPantalla = self.Nucleo.ObtPosicion(( self.pos_x , self.pos_y ))
        
        if(self.Busqueda(p_Evento.pos,p_posInterPadre = p_posInterPadre) == True):
            self.CFondo = BLANQUISCO
            self.Raton_Click = True
            return True
        else:
            if(self.Raton_Click == True):
                self.CFondo = BLANCO
                self.Raton_Click = False
                return True
            return False        
    
    def PresionDTeclado(self,evento):
        if (self.Raton_Click == False):
            return False
        
        self.caracter = self.ObtCaracter(evento)
        
        if(self.caracter == 'del'):
            self.Texto = self.BorrarCarac()
        else:
            self.Texto += self.caracter
            
        self.Interface = self.Render()
        return True 
    
    def BorrarCarac(self):
        if(self.con > 0): 
            self.con -= 1
        return self.Texto[:len(self.Texto) - 1]       
    
    def ObtCaracter(self, p_eventokey):
        valor = ''
        #key = pygame.key.get_pressed()
        evento = p_eventokey
        
        if evento.key == pygame.K_BACKSPACE:
            valor = 'del'
        else:              
            valor = evento.unicode 
                 
                        
        #conjunto de caracteres agregados  
        #if key[K_MINUS]:    
        #    valor = '-'    
        #elif key[K_PLUS]:   
        #    valor = '+'        
        #elif key[K_PERIOD]: 
        #    valor = '.'  
        #elif key[K_COMMA]:  
        #    valor = ','  
        #elif key[K_LEFTPAREN]:  
        #    valor = '('  
#        elif key[K_RIGHTPAREN]: 
#            valor = ')'  
#        elif key[K_ASTERISK]:   
#            valor = '*'  
#        elif key[K_UNDERSCORE]: 
#            valor = '_'  
#        elif key[K_KP_EQUALS]:  
#            valor = '='  
#        elif key[K_COLON]:  
#            valor = ':'  
#        elif key[K_SEMICOLON]:  
#            valor = ';'    
#        
#        elif key[K_a]:
#            valor = 'a'
#        elif key[K_b]:
#            valor = 'b'
#        elif key[K_c]:
#            valor = 'c'
#        elif key[K_d]:
#            valor = 'd'
#        elif key[K_e]:
#            valor = 'e'
#        elif key[K_f]:
#            valor = 'f'
#        elif key[K_g]:
#            valor = 'g'
#        elif key[K_h]:
#            valor = 'h'
#        elif key[K_i]:
#            valor = 'i'
#        elif key[K_j]:
#            valor = 'j'
#        elif key[K_k]:
#            valor = 'k'
#        elif key[K_l]:
#            valor = 'l'
#        elif key[K_m]:
#            valor = 'm'
#        elif key[K_n]:
#            valor = 'n'
#        elif key[K_o]:
#            valor = 'o'
#        elif key[K_p]:
#            valor = 'p'
#        elif key[K_q]:
#            valor = 'q'
#        elif key[K_r]:
#            valor = 'r'
#        elif key[K_s]:
#            valor = 's'
#        elif key[K_t]:
#            valor = 't'
#        elif key[K_u]:
#            valor = 'u'
#        elif key[K_v]:
#            valor = 'v'
#        elif key[K_w]:
#            valor = 'w'
#        elif key[K_x]:
#            valor = 'x'
#        elif key[K_y]:
#            valor = 'y'
#        elif key[K_z]:
#            valor = 'z'
#            
#        #reconocimiento del teclado Numerico  
#        elif (key[K_1] or key[K_KP1]):
#            valor = '1'
#        elif (key[K_2] or key[K_KP2]):
#            valor = '2'
#        elif (key[K_3] or key[K_KP3]):
#            valor = '3'
#        elif (key[K_4] or key[K_KP4]):
#            valor = '4'
#        elif (key[K_5] or key[K_KP5]):
#            valor = '5'
#        elif (key[K_6] or key[K_KP6]):
#            valor = '6'
#        elif (key[K_7] or key[K_KP7]):
#            valor = '7'
#        elif (key[K_8] or key[K_KP8]):
#            valor = '8'
#        elif (key[K_9] or key[K_KP9]):
#            valor = '9'
#        elif (key[K_0] or key[K_KP0]):
#            valor = '0'
#        elif key[K_SPACE]:
#            valor = ' '
#        elif key[K_BACKSPACE]:  
#            valor = 'del'   
#            
#        print p_eventokey.unicode     
            
        #if (key[KMOD_CAPS]):
        #    if(self.Mayus == False):
        #        self.Mayus = True
        #    else:
        #        self.Mayus = False
                    
        #if(self.Mayus == True):
        #    valor = valor.upper()
        
        #if (key[KMOD_CAPS] and not(key[KMOD_SHIFT])):
        #    valor = valor.upper()
        #--inverso a lo anterior
        #if (not(key[KMOD_CAPS]) and (key[KMOD_SHIFT])):
        #    valor = valor.upper()
        
        return valor    