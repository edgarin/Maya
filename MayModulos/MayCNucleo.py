# -*- coding: utf-8 -*
#Variables Globales utilizadas en la Jerarquia del Juego
#1-Barra de Menu Superior
#2-Barra de Menu Inferior
#3-Botones y Etiquetas(Labels)

import pygame
import time
from MayMColores import *
class MayCNucleo(object):    
    _iInstance = None       
    
    class Singleton:
        def __init__(self):
            self.Pantalla_Principal = pygame.display.get_surface()
            ######################################Variable y Listass#########################################
            self.objetos = []
            #Indica si Exite una Barra de Menu 
            self.HayBarS = False
            #Guardara la Barra de Menu si existe
            self.BarraMenu = None
            #Indica si Exite una Barra de Menu Lateral 
            self.HayBarL = False
            #Guardara la Barra de Menu Lateral si existe
            self.BarraLateral = None
            #Origen Recursos
            self.dirRecursos = None
            #Fondo para la Pantalla Principal
            self.Fondo = None
            #Mensaje
            self.Mnsj = None
            #Objeto Desktop de la libreria SPG
            self.SPGDesk = None
            #Reloj
            self.NReloj = None
            #Fondo Congelado
            self.ConFondo = None
            self.NKeyDown = None
            self.NMOUSEMOTION = None    
            self.NMBUTTONDOWN = None
            
        #############################Metodos y Funciones##################################
        def CSPGDesk(self, p_Desk):
            self.SPGDesk = p_Desk
                
        def CDirRecursos(self,p_dirRecursos):
            self.dirRecursos = p_dirRecursos
        def ObtDirRecursos(self):
            return self.dirRecursos

        def CFondo(self,p_Fondo):
            self.Fondo = p_Fondo
        def ObtFondo(self):
            return self.Fondo

        def CReloj(self,p_Reloj):
            self.NReloj = p_Reloj
        def ObtReloj(self):
            return self.NReloj        
                     
        def Insertar(self,p_obj):
            #Interface del Objeto
            interobj = p_obj.ObtInterface()
            if(p_obj.T_Objeto == 'Panel'):
                Posicion = p_obj.Posicion_Actual
            elif(p_obj.T_Objeto == 'Boton' or p_obj.T_Objeto == 'Imagen' or p_obj.T_Objeto == 'Etiqueta' or p_obj.T_Objeto == 'CuadroTexto'):
                if(p_obj.CentradoEn != ""):
                   p_obj.Centrar(p_obj.CentradoEn)     
                Posicion = p_obj.pos_x,p_obj.pos_y
            
            Posicion = self.ObtPosicion(Posicion)
            
            if (p_obj.T_Objeto != 'CuadroTexto'):
                self.Pantalla_Principal.blit(interobj,Posicion)
            else:
                p_obj.Dibujar(self.Pantalla_Principal,Posicion)    
        
        def ObtPosicion(self,p_Posicion):
            pos_x,pos_y = p_Posicion
            
            if(self.HayBarS == True):
                #Posicion de la Barra de Menu
                posxBS,posyBS = self.BarraMenu.ObtTamano()
                return (pos_x,( pos_y + posyBS ))
            
            if(self.HayBarL == True):
                posxBL,posyBL = self.BarraLateral.ObtTamano()
                return ((pos_x + posxBL),pos_y)
            
            if(self.HayBarS == True and self.HayBarL == True):
                posxBS,posyBS = self.BarraMenu.ObtTamano()
                posxBL,posyBL = self.BarraLateral.ObtTamano()
                return ((pos_x + posxBL),(pos_y + posyBS))
            
            return p_Posicion
                
        def Agregar(self,p_Objeto):
            Objeto = p_Objeto
    
            if(Objeto.T_Objeto == 'BarraMenu'):
                self.BarraMenu = Objeto
                self.HayBarraMenu()
        
            self.objetos.append(p_Objeto)

        def Remover(self,p_Objeto):
            Objeto = p_Objeto
    
            self.objetos.remove(Objeto)
                    
        def HayBarraMenu(self):
            self.HayBarS = True
    
        #Congelar Objetos
        def CongObjetos(self, valor):
            if (self.Fondo != None and valor == False):
                self.ConFondo = self.Fondo
            
            if (valor == True and self.ConFondo != None):
                self.Fondo = self.ConFondo
                    
            for obj in self.objetos:
                if(obj.T_Objeto != 'BarraMenu'):                      
                    obj.CMNucleo(valor)                 
                   
        #Remover Objetos
        def RemObjetos(self):
            if (self.NReloj != None):
                self.NReloj.Terminar()
                self.NReloj = None
            
            if (self.Fondo != None):
                self.Fondo = None    
                
            Lista = []
            for con in range(len(self.objetos)):
                print con
                if(self.objetos[con].T_Objeto != 'BarraMenu' and self.objetos[con].ObtMNucleo() != True):                      
                    Lista.append(self.objetos[con]) 
            self.objetos = Lista   
            #Se Remueven los Metodos de la Instanciacion de la cual se remueven los objetos
            self.NKeyDown = None
            self.NMOUSEMOTION = None    
            self.NMBUTTONDOWN = None
            #Se Remueve el objeto desktop de la libreria SPG por si fue enviado al singleton      
            self.SPGDesk = None
                                            
        def Imprimir(self):    
            if(self.Fondo != None and self.Fondo.ObtMNucleo() == True):
                self.Fondo.Insertar()
                
            #Inserccion de los Objetos que no estan enFrente a la Pantalla
            for obj in self.objetos:
                if(obj.ObtEnFrente() == False and obj.ObtMNucleo() == True and obj.ObtHabilitado() == True and obj.T_Objeto != 'BarraMenu' and obj != self.Fondo):                      
                    obj.Insertar()

            #Inserccion de los Objetos que estan al enFrente a la Pantalla
            for obj in self.objetos:
                if(obj.ObtEnFrente() == True and obj.ObtMNucleo() == True and obj.ObtHabilitado() == True and obj.T_Objeto != 'BarraMenu' and obj != self.Fondo):                      
                    obj.Insertar()         
            
            #Inserccion de los Mensajes de Ayuda de los Botones  a la Pantalla
            for obj in self.objetos:
                if(obj.ObtMNucleo() == True and obj.ObtHabilitado() == True and obj != self.Fondo):
                    if(obj.T_Objeto == 'Boton' or obj.T_Objeto == 'CuadroTexto'):                      
                        obj.AgregarMensaje()                 
                    elif (obj.T_Objeto == 'Panel' and obj.ObtMsj() == False):
                        obj.InsertarMensajesAyuda()    

            if(self.HayBarS == True):
                #Inserccion Menu Superior a la Pantalla
                #Esta Inserccion incluye la de los submenus si se dio click a un Boton
                self.BarraMenu.Insertar()
            
            if (self.Mnsj != None):
                self.ActualizarSPGD()
                self.Mnsj.Insertar()
                self.Mnsj.InsertarMensajesAyuda()
                    
        def Salir(self):
            valor = self.Msj('Realmente desea Salir?', p_Tipo = 1)
            if(valor == 1):
                exit()    
        
        def ActualizarSPGD(self):
            if(self.SPGDesk != None):
                self.SPGDesk.draw()
                        
        def Msj(self, p_Mensaje = None, p_Tipo = 0):
            if (self.NReloj != None):
                self.NReloj.Parar()
            Mensaje = p_Mensaje
            
            if(p_Tipo == 0):
                self.MSI(p_Mensaje = Mensaje)
            elif(p_Tipo == 1):
                return self.MSINO(p_Mensaje = Mensaje)
            elif(p_Tipo == 2):
                return self.Inp(p_Mensaje = Mensaje)
                 
        def MSI(self, p_Mensaje = None):
            Mensaje = p_Mensaje
            #Valor que sera devuelto
            self.valor = -1
            #Eventos de los Botones
            def Aceptar():
                self.valor = 1
                    
            import MayMONucleo
            MON = MayMONucleo
            
            lblMensaje = MON.MLabel(Mensaje,'lblMensaje',(5,25),'Blanco')
            
            lblancho,lblalto = lblMensaje.ObtTamano()
            
            btnx = ( (lblancho + 10) / 2) - (30 / 2)
            btny = 35 + lblalto
            
            btnSi = MON.MBoton('btnSi','Si.png',p_Coordenadas = (btnx,btny),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
            btnSi.MensajeAyuda('Aceptar')
            btnSi.evtclick = Aceptar
            
            btnancho, btnalto = btnSi.ObtTamano()
            panancho, panalto = self.Pantalla_Principal.get_size()
            
            ImgEncabezdo = MON.MImagen('ImgEncabezado','FondoImg.png',p_Coordenadas = (0,0),p_Tamano = (panancho,15),p_direccionico = './MayRecursos/MayIconos')
            
            pancho = lblancho + 10 
            palto = lblalto + btnalto + 45
            
            px = (panancho / 2) - (pancho / 2)
            py = (panalto / 2) - (palto / 2)
            
            tamPane = (pancho, palto)
            posPane= (px, py)
            
            Panel = MON.MPanel(posPane,tamPane)
            Panel.CInterfacePadre(self.Pantalla_Principal)
            Panel.CColor(ARENA)
            Panel.CMsj(True)
            Panel.Adherir(ImgEncabezdo)
            Panel.Adherir(btnSi)
            Panel.Adherir(lblMensaje)
            self.Mnsj = Panel
            self.ActualizarSPGD()
            self.Mnsj.Insertar()
            pygame.display.update()
            
            run = True
            while(run):
                evento = pygame.event.wait()
                self.MEventos(evento)
                
                if(self.valor != -1):
                    self.Remover(self.Mnsj)
                    self.Mnsj = None
                    if (self.NReloj != None):
                        self.NReloj.Continuar()
                    self.Imprimir()
                    pygame.display.update()
                    return 
                
                pygame.display.update()    
                        
        def MSINO(self, p_Mensaje = None):
            Mensaje = p_Mensaje
            #Valor que sera devuelto
            self.valor = -1
            #Eventos de los Botones
            def Aceptar():
                self.valor = 1
            def Cancelar():
                self.valor = 0
                    
            import MayMONucleo
            MON = MayMONucleo
            
            lblMensaje = MON.MLabel(Mensaje,'lblMensaje',(5,25),'Blanco')
            
            lblancho,lblalto = lblMensaje.ObtTamano()
            
            btnx = ( (lblancho + 10) / 2) - (((30 * 2) + 10) / 2)
            btny = 35 + lblalto
            
            btnSi = MON.MBoton('btnSi','Si.png',p_Coordenadas = (btnx,btny),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
            btnSi.MensajeAyuda('Aceptar')
            btnSi.evtclick = Aceptar
            btnNo = MON.MBoton('btnNo','No.png',p_Coordenadas = ((btnx + 40),btny),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
            btnNo.MensajeAyuda('Cancelar')
            btnNo.evtclick = Cancelar
            
            btnancho, btnalto = btnSi.ObtTamano()
            panancho, panalto = self.Pantalla_Principal.get_size()
            
            ImgEncabezdo = MON.MImagen('ImgEncabezado','FondoImg.png',p_Coordenadas = (0,0),p_Tamano = (panancho,15),p_direccionico = './MayRecursos/MayIconos')
            
            pancho = lblancho + 10 
            palto = lblalto + btnalto + 45
            
            px = (panancho / 2) - (pancho / 2)
            py = (panalto / 2) - (palto / 2)
            
            tamPane = (pancho, palto)
            posPane= (px, py)
            
            Panel = MON.MPanel(posPane,tamPane)
            Panel.CInterfacePadre(self.Pantalla_Principal)
            Panel.CColor(DORADO)
            Panel.CMsj(True)
            Panel.Adherir(ImgEncabezdo)
            Panel.Adherir(btnSi)
            Panel.Adherir(btnNo)
            Panel.Adherir(lblMensaje)
            self.Mnsj = Panel
            self.ActualizarSPGD()
            self.Mnsj.Insertar()
            pygame.display.update()
            
            run = True
            while(run):
                evento = pygame.event.wait()
                self.MEventos(evento)
                
                if(self.valor != -1):
                    self.Remover(self.Mnsj)
                    self.Mnsj = None
                    if (self.NReloj != None):
                        self.NReloj.Continuar()
                    self.Imprimir()
                    pygame.display.update()
                    return self.valor
                
                pygame.display.update()    
                
        def Inp(self, p_Mensaje = None):
            Mensaje = p_Mensaje
            #Valor que sera devuelto
            self.valor = -1
            #Eventos de los Botones
            def Aceptar():
                self.valor = 1
                    
            import MayMONucleo
            MON = MayMONucleo
                        
            lblMensaje = MON.MLabel(Mensaje,'lblMensaje',(5,25),'Blanco')
            
            lblancho,lblalto = lblMensaje.ObtTamano()
            
            txtx = ( (lblancho + 10) / 2) - (100 / 2)
            txty = 35 + lblalto
            
            TxtDato = MON.MCuaTexto('txtDato',p_Coordenadas = (txtx,txty) ,p_Ancho = 100)
            TxtDato.MensajeAyuda('Escribe Aqui!')
            
            txtancho,txtalto = TxtDato.ObtTamano()
            
            btnx = ( (lblancho + 10) / 2) - (30 / 2)
            btny = 45 + lblalto + txtalto
            
            btnSi = MON.MBoton('btnSi','Si.png',p_Coordenadas = (btnx,btny),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
            btnSi.MensajeAyuda('Aceptar')
            btnSi.evtclick = Aceptar
            
            btnancho, btnalto = btnSi.ObtTamano()
            panancho, panalto = self.Pantalla_Principal.get_size()
            
            pancho = lblancho + 10 
            palto = lblalto + btnalto + txtalto + 55
            
            ImgEncabezdo = MON.MImagen('ImgEncabezado','FondoImg.png',p_Coordenadas = (0,0),p_Tamano = (panancho,15),p_direccionico = './MayRecursos/MayIconos')
            
            px = (panancho / 2) - (pancho / 2)
            py = (panalto / 2) - (palto / 2)
            
            tamPane = (pancho, palto)
            posPane= (px, py)
            
            Panel = MON.MPanel(posPane,tamPane)
            Panel.CInterfacePadre(self.Pantalla_Principal)
            Panel.CColor(TURQUESA)
            Panel.CMsj(True)
            Panel.Adherir(ImgEncabezdo)
            Panel.Adherir(btnSi)
            Panel.Adherir(TxtDato)
            Panel.Adherir(lblMensaje)
            self.Mnsj = Panel
            self.ActualizarSPGD()
            self.Mnsj.Insertar()
            pygame.display.update()
            
            run = True
            while(run):
                evento = pygame.event.wait()
                self.MEventos(evento)
                
                if(self.valor != -1):
                    dato = TxtDato.ObtTexto()
                    self.Remover(self.Mnsj)
                    self.Mnsj = None
                    
                    if (self.NReloj != None):
                        self.NReloj.Continuar()
                    self.Imprimir()
                    pygame.display.update()
                    return dato
                
                pygame.display.update()
                        
        #Manejador de Eventos
        def MEventos(self,p_Evento):
            evento = p_Evento
                
            #El Evento Quit ocurre cuando se ha presionado el boton de cerrar
            if evento.type == pygame.QUIT:
                if (self.Mnsj == None):
                    self.Salir()
        
            #Este Tipo de Evento indica que se ha Presionado algun Boton del Raton
            #Sobre la Pantalla Display        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if (self.Mnsj != None):
                    if(self.Mnsj.PresionDRaton(evento)):        
                        self.Imprimir()
                    return
                
                if (self.NMBUTTONDOWN != None):
                     self.NMBUTTONDOWN(evento)               
                     
                if(self.HayBarS == True and self.BarraMenu.PresionDRaton(evento)):
                    self.Imprimir()
                    return
                for obj in self.objetos:
                    if(obj.ObtHabilitado() == True and obj.ObtMNucleo() == True):
                        if(self.HayBarS == True or self.HayBarL == True):
                            if((obj.T_Objeto == "Panel"  or obj.T_Objeto == "Boton" or obj.T_Objeto == 'CuadroTexto') and obj.PresionDRaton(evento,npos = True)):        
                                self.Imprimir()
                                return        
                        else:
                            if((obj.T_Objeto == "Panel"  or obj.T_Objeto == "Boton" or obj.T_Objeto == 'CuadroTexto') and obj.PresionDRaton(evento)):        
                                self.Imprimir()
                                return        

            #Este Tipo de Evento indica que se ha movido el Raton
            #Sobre la Pantalla Display                            
            if evento.type == pygame.MOUSEMOTION:
                if (self.Mnsj != None):
                    if(self.Mnsj.MovimientoDRaton(evento)):        
                        self.Imprimir()
                    return
                
                if (self.NMOUSEMOTION != None):
                     self.NMOUSEMOTION(evento)            
                     
                if(self.HayBarS == True and self.BarraMenu.MovimientoDRaton(evento)):
                    self.Imprimir()
                    return
                for obj in self.objetos:
                    if(obj.ObtHabilitado() == True and obj.MNucleo == True):
                        if(self.HayBarS == True or self.HayBarL == True):
                            if((obj.T_Objeto == "Panel"  or obj.T_Objeto == "Boton" or obj.T_Objeto == 'CuadroTexto') and obj.MovimientoDRaton(evento,npos = True)):        
                                self.Imprimir()
                                return              
                        else:     
                            if((obj.T_Objeto == "Panel"  or obj.T_Objeto == "Boton" or obj.T_Objeto == 'CuadroTexto') and obj.MovimientoDRaton(evento)):        
                                self.Imprimir()
                                return              

            if evento.type == pygame.KEYDOWN: 
                if (self.Mnsj != None):
                    if(self.Mnsj.PresionDTeclado(evento)):        
                        self.Imprimir()
                    return                
                
                if (self.NKeyDown != None):
                    self.NKeyDown(evento)
                    
                for obj in self.objetos:
                    if(obj.ObtHabilitado() == True and obj.MNucleo == True):
                        if(self.HayBarS == True or self.HayBarL == True):
                            if((obj.T_Objeto == 'CuadroTexto' or obj.T_Objeto == 'Panel') and obj.PresionDTeclado(evento)):        
                                self.Imprimir()
                                return                        
                        
    ## The constructor
    #  @param self The object pointer.
    def __init__( self ):
        # Check whether we already have an instance
        if MayCNucleo._iInstance is None:
            # Create and remember instanc
            MayCNucleo._iInstance = MayCNucleo.Singleton()
 
        # Store instance reference as the only member in the handle
        self._EventHandler_instance = MayCNucleo._iInstance
 
 
    ## Delegate access to implementation.
    #  @param self The object pointer.
    #  @param attr Attribute wanted.
    #  @return Attribute
    def __getattr__(self, aAttr):
        return getattr(self._iInstance, aAttr)
 
 
    ## Delegate access to implementation.
    #  @param self The object pointer.
    #  @param attr Attribute wanted.
    #  @param value Vaule to be set.
    #  @return Result of operation.
    def __setattr__(self, aAttr, aValue):
        return setattr(self._iInstance, aAttr, aValue)                              