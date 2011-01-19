#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
#       
#       Copyleft 2010 Informática al Alcance de Todos (CA)
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
import pygame
import os.path
from MayCBoton import MayCBoton
from MayCNucleo import MayCNucleo
from MayMColores import *

class MayCPanel(object):
    def __init__(self,p_Posicion,p_Tamano,p_direccionico =  None,p_Habilitado = True):
        self.Nucleo = MayCNucleo()
        #Propiedades
        #Interface en la cual la BarraMenu sera Insertada
        self.Interface_Padre = pygame.display.get_surface()
        self.Tamano = p_Tamano
        self.Posicion_Actual = p_Posicion
        self.Interface = pygame.Surface(p_Tamano,0,32)
        #Tipo de Objeto
        self.T_Objeto = 'Panel'
        #Objetos adheridos al panel
        self.Objetos = []
        #Objeto en Juego (Que esta Interactuando con los eventos =>MOUSEMOTION)
        self.ObjN_Juego = None
        self.Habilitado = p_Habilitado
        self.Color = BLANCO
        self.PosenPantalla = self.Nucleo.ObtPosicion(self.Posicion_Actual)
        #Manejado por el Nucleo
        self.MNucleo = True
        self.EnFrente = False
        if(p_direccionico == None):
            self.Directorio_Imagenes = self.Nucleo.ObtDirRecursos()
        else:
            self.Directorio_Imagenes = p_direccionico
        #Indica si el Panel es un Mensaje    
        self.Msj = False    
        self.Nucleo.Agregar(self)
    
    def CInterfacePadre(self,p_Interface_Padre):
        #La Interface Padre sera otra Interface diferente de la Pantalla Principal
        self.Interface_Padre = p_Interface_Padre

    def CEnFrente(self, valor):
        self.EnFrente = valor
    def ObtEnFrente(self):
        return self.EnFrente
            
    def Adherir(self,objeto):
        objeto.CInterfacePadre(self.Interface)
        objeto.Insertar()
        self.Objetos.append(objeto)
    
    def CMsj(self,valor):
        self.Msj = valor
    def ObtMsj(self):
        return self.Msj 
        
    def CMNucleo(self,valor):
        #Manejado por el Nucleo
        self.MNucleo = valor
    def ObtMNucleo(self):
        #Manejado por el Nucleo
        return self.MNucleo  
    def ObtInterface(self):
        return self.Interface   
    
    def CColor(self,p_Color):
        self.Color = p_Color
        self.ReIniciar()
        
    def ObtColor(self):
        return self.Color
            
    def Habilitar(self,p_Si_No):
        self.Habilitado = p_Si_No
    def ObtHabilitado(self):
        return self.Habilitado
    
    def ReIniciar(self,p_QM = False):
        self.Interface.fill(self.Color)
        
        for contador in range(len(self.Objetos)):
            self.Objetos[contador].Insertar()    
    
    def ObtenerPosicion(self):
        return self.Posicion_Actual
    
    def ObtenerPosPantalla(self):
        return self.PosenPantalla
        
    def ObtenerTamano(self):
        return self.Tamano        
    
    def CreacionBotones(self,p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_Posicion = (0,0),p_Tamano = (20,10),p_NoBoton = 1):
        posx,posy = p_Posicion
        ancho,alto = p_Tamano
        for contador in range(p_NoBoton):
            nombre = p_IDs[contador]
            Nombre_Imagen = p_Imagenes[contador]
            Mensaje = p_Mensajes_Ayuda[contador]
            
            Boton = MayCBoton(nombre,Nombre_Imagen,( posx + ( (ancho + 10) * contador ) , posy),( ancho , alto ))
            
            #Indico que la Interface Padre es la de la Barra de Menu    
            Boton.CInterfacePadre(self.Interface)    
            Boton.MensajeAyuda(Mensaje)
            #Agregar Boton a la Interface
            Boton.Insertar()
            self.Objetos.append(Boton)        
            
    def Insertar(self):
        self.Nucleo.Insertar(self)
        if(self.Msj ==  True):
            pygame.draw.rect(self.Interface_Padre, NEGRO, (self.PosenPantalla,self.Tamano), 2)
    
    def InsertarMensajesAyuda(self):
        obj = self.ObjN_Juego
        if (obj == None):
            return
        
        if (obj.T_Objeto == "Boton" or obj.T_Objeto == "CuadroTexto"):
            if(obj.Raton_Dentro == True):
                obj.AgregarMensaje()

    def BusquedaEvt(self,metodo,p_evento):
        for obj in self.Objetos:
            if (obj.T_Objeto == 'Etiqueta' or obj.T_Objeto == 'Imagen'):
                continue
            elif(metodo == 2 and obj.T_Objeto == 'Boton'):
                continue
            
            if (metodo == 0):
                Metodo = obj.PresionDRaton
            elif (metodo == 1):
                Metodo = obj.MovimientoDRaton
            elif (metodo == 2):
                Metodo = obj.PresionDTeclado
            
            if (metodo == 2):                
                if(Metodo(p_evento)):
                    #Objeto en Juego
                    self.ObjN_Juego = obj
                    return True
                continue
            else:                        
                if (Metodo(p_evento , npos = False ,p_posInterPadre = self.PosenPantalla)):
                    #Objeto en Juego
                    self.ObjN_Juego = obj
                    return True
            
    def PresionDRaton(self,p_Evento,npos = False):
        if(npos == True):
            self.PosenPantalla=self.Nucleo.ObtPosicion(self.Posicion_Actual)
            
        if(self.VerificaEvento(p_Evento) == True):
            if (self.BusquedaEvt(0,p_Evento)):
                self.ReIniciar()
                return True
        else:
            return False
                
    def MovimientoDRaton(self,p_Evento,npos = False):
        if(npos == True):
            self.PosenPantalla = self.Nucleo.ObtPosicion(self.Posicion_Actual)
        
        if(self.VerificaEvento(p_Evento) == True):
            
            if (self.BusquedaEvt(1,p_Evento)):
                self.ReIniciar()
                return True
        
    def PresionDTeclado(self,evento):
        if(self.BusquedaEvt(2,evento)):
            self.ReIniciar()
            return True    
                                            
    #Busca si se concentra un Posible evento en la Interface
    def VerificaEvento(self,p_evento):
        pos_x2,pos_y2 = p_evento.pos
        
        pos_x,pos_y = self.ObtenerPosPantalla()
        Ancho,Alto = self.ObtenerTamano()
    
        if ((pos_x2 >= pos_x and pos_x2 <= (pos_x + Ancho)) and (pos_y2 >= pos_y and pos_y2 <= (pos_y + Alto))):
            return True
        else:
            return False
