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
from MayCNucleo import MayCNucleo
from MayCObjeto import MayCObjeto

class MayCBoton(MayCObjeto):

	def __init__(self,p_ID,p_Imagen_Nombre,p_Coordenadas = (0,0),p_Tamano = (30,30),p_direccionico = None,p_Habilitado = True):
		MayCObjeto.__init__(self,p_ID,p_Coordenadas,p_Tamano,p_Habilitado)
		self.Nucleo = MayCNucleo()
		#Propiedades
		self.Imagen_Nombre = p_Imagen_Nombre
		#Tipo de Objeto
		self.T_Objeto = 'Boton'
		self.Mensaje_Ayuda = ''
		self.Pos_Mensaje = (0,0)
		#Indica si el Boton posee una SubBarraMenu y es donde esta se Almacena
		self.SubBarraMenu = None
		#Evento del Boton
		self.evtclick = None
		self.Raton_Dentro = False
		if(p_direccionico == None):
			self.Directorio_Imagenes = self.Nucleo.ObtDirRecursos()
		else:
			self.Directorio_Imagenes = p_direccionico
		self.PosenPantalla = self.Nucleo.ObtPosicion((self.pos_x,self.pos_y))	
		#Se asigna la Imagen
		self.CInterface()
		self.Nucleo.Agregar(self)
	
	def CPosenPantalla(self,valor):
		self.PosenPantalla = valor
					
	def Insertar(self,p_Interface = None):
		if (p_Interface == None):
			#self.Interface_Padre.blit(self.imagen,(self.pos_x,self.pos_y))
			if(self.Contenedor != True):
				self.Nucleo.Insertar(self)
			else:
				self.Interface_Padre.blit(self.imagen,( self.pos_x , self.pos_y ))	
		else:
			p_Interface.blit(self.imagen,( self.pos_x , self.pos_y ))
					
	def AgregarMensaje(self,p_Interface = None):
		if(self.Mensaje_Ayuda == '' or (self.Contenedor == False and self.Raton_Dentro == False)):
			return
		PantallaPrincipal = pygame.display.get_surface()
		if (p_Interface == None):
			PantallaPrincipal.blit(self.Mensaje_Ayuda,self.Pos_Mensaje)
		else:
			p_Interface.blit(self.Mensaje_Ayuda,self.Pos_Mensaje)
	
	def ObtInterface(self):
		return self.imagen
	def CInterface(self,p_imagen = None):
		if(self.Directorio_Imagenes != None and self.Imagen_Nombre != None):
			self.imagen = pygame.image.load(os.path.join(self.Directorio_Imagenes,self.Imagen_Nombre))
			self.imagen = pygame.transform.scale(self.imagen,( self.Ancho , self.Alto ))			
		elif(p_imagen != None):
			self.imagen = p_imagen
			self.imagen = pygame.transform.scale(self.imagen,( self.Ancho , self.Alto ))
		else:
			self.imagen = None
		
	def MensajeAyuda(self,Mensaje):
		Fuente_Mensaje = pygame.font.SysFont("arial", 11)
		#(0,0,0)=>Color de Letra (150,155,175)=>Color Fondo 
		#Font.render() devuelve una surface
		self.Mensaje_Ayuda = Fuente_Mensaje.render(Mensaje, True, (0, 0, 0), (150, 155, 175))			
	def ObtenerMensaje(self):
		return self.Mensaje_Ayuda
	
	def PosMensaje(self,p_Pos_Mensaje):
		self.Pos_Mensaje = p_Pos_Mensaje
				
	def Busqueda(self,posicion_click,p_posInterPadre = (0,0)):
		pos_x2,pos_y2 = posicion_click
		#Se saca la posicion en relacion a la Pantalla Principal
		pospadrex,pospadrey = p_posInterPadre
		
		#Esta posicion se hace en relacion a un MenuSuperior o MenuLateral, si no hay los valores eran
		#iguales a self.pos_x  y  self.pos_y
		posxnp,posynp = self.PosenPantalla
		
		if(self.Contenedor == True):
			pos_x = pospadrex + self.pos_x
			pos_y = pospadrey + self.pos_y
		else:
			pos_x = pospadrex + posxnp
			pos_y = pospadrey + posynp	
				
		if ((pos_x2 >= pos_x and pos_x2 <= (pos_x + self.Ancho)) and (pos_y2 >= pos_y and pos_y2 <= (pos_y + self.Alto))):
			return True	
			
	def CreacionSubBarraMenu(self,p_SubBarramenu,p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_TamBotones):
		self.SubBarraMenu = p_SubBarramenu
		self.SubBarraMenu.CreacionMenus(p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_Posicion = (10,5),p_Tamano = p_TamBotones)
	
	def ObtenerSubMenu(self):
		return self.SubMenu					

	def MovimientoDRaton(self,p_Evento,npos = False,p_posInterPadre = (0,0)):
		if(npos == True):
			self.PosenPantalla = self.Nucleo.ObtPosicion(( self.pos_x , self.pos_y ))
		
		evento = p_Evento
		if(self.Busqueda(evento.pos,p_posInterPadre) == True and self.Raton_Dentro == False):
			self.EntraRaton()
			self.Pos_Mensaje = evento.pos
			return True
		elif(self.Busqueda(evento.pos,p_posInterPadre) != True and self.Raton_Dentro == True):
			self.SaleRaton()
			return True
	
	def EntraRaton(self):
		self.Raton_Dentro = True
	def SaleRaton(self):
		self.Raton_Dentro = False
	
	def PresionDRaton(self,p_Evento,npos = False ,p_posInterPadre = (0,0)):
		if(npos == True):
			self.PosenPantalla = self.Nucleo.ObtPosicion(( self.pos_x , self.pos_y ))
		
		if(self.Busqueda(p_Evento.pos,p_posInterPadre) == True):
			self.Click()		
	
	def Click(self):	
		if(self.evtclick == None):
			return	
		self.evtclick()		