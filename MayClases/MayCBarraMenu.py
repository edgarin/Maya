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
from MayCSubBarraMenu import MayCSubBarraMenu

class MayCBarraMenu(object):
	def __init__(self,p_Interface_Padre,p_Posicion,p_Tamano,p_Directorio_Recursos_Iconos,p_Tipo,p_SubMenu=False,p_Habilitado=True):
		#Inicializo SubMódulos de Pygame
		pygame.init()
		#Propiedades
		#Interface en la cual la BarraMenu sera Insertada
		self.Interface_Padre=p_Interface_Padre
		self.Tamano=p_Tamano
		self.Posicion_Actual=p_Posicion
		self.Interface=pygame.Surface(p_Tamano,0,32)
		self.Interface.fill((255,255,255))
		self.Tipo=p_Tipo
		self.Directorio_Recursos_Iconos=p_Directorio_Recursos_Iconos	
		#Indica si posee o  no un SubMenu la Barra de Menu
		self.SubMenu=p_SubMenu
		#Creacion Items Menu Bar
		self.Menus=[]
		#Boton en Juego (Que esta Interactuando con los eventos =>MOUSEMOTION)
		self.Boton_NJuego=None
		#Variables de Eventos de Raton
		self.Raton_Dentro=False
		self.Raton_Fuera=True
		self.Raton_Click=False
		self.Habilitado=p_Habilitado
		
	def ObtenerInterface(self):
		return self.Interface
		
	def AgregarMensaje(self,p_posicion_mensaje=None):
		if (p_posicion_mensaje==None):
			#Agrego Mensaje tooltip
			self.Boton_NJuego.AgregarMensaje(p_Interface=self.Interface_Padre)		
	
	def QuitarMensaje(self):
		self.ReIniciar(p_QM=True)
			
	def Habilitar(self,p_Si_No):
		self.Habilitado=p_Si_No
	
	def ReIniciar(self,p_QM=False):
		self.Interface.fill((255,255,255))

		if (p_QM==False):
			self.Raton_Click=False
		
		for contador in range(len(self.Menus)):
			self.Menus[contador].Insertar()	
	
	def ObtenerPosicion(self):
		return self.Posicion_Actual
		
	def ObtenerTamano(self):
		return self.Tamano		
	
	def CreacionBotones(self,p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_Posicion=(0,0),p_Tamano=(20,10),p_No_Menus=1):
		posx,posy=p_Posicion
		ancho,alto=p_Tamano
		for contador in range(p_No_Menus):
			nombre=p_IDs[contador]
			Nombre_Imagen=p_Imagenes[contador]
			Mensaje=p_Mensajes_Ayuda[contador]
			
			if (self.Tipo=='Horizontal'):
				Boton_de_Menu=MayCBoton(self.Interface,nombre,Nombre_Imagen,self.Directorio_Recursos_Iconos,(posx+((ancho+10)*contador),posy),(ancho,alto))
			elif (self.Tipo=='Vertical'):
				Boton_de_Menu=MayCBoton(self.Interface,nombre,Nombre_Imagen,self.Directorio_Recursos_Iconos,(posx,posy+((alto+10)*contador)),(ancho,alto))
				#print nombre + ' ' + str(posy+((alto+10)*contador))
				
			Boton_de_Menu.MensajeAyuda(Mensaje)
			#Agregar Boton a la Interface
			Boton_de_Menu.Insertar()
			self.Menus.append(Boton_de_Menu)		
	
	def CreacionSubBarraMenu(self,p_Ids_Botones,p_Imagenes_Botones,p_Mensajes_Botones,p_NoMenusxSubMenu):
		for contador in range(len(self.Menus)):
			#Listas para el SubMenu a Crear
			L_IdsBotones=p_Ids_Botones[contador]
			L_Imagenes=p_Imagenes_Botones[contador]
			L_Mensajes=p_Mensajes_Botones[contador]
			L_NoBotones=p_NoMenusxSubMenu[contador]
			
			posx1,posy1=self.Posicion_Actual
			w,h=self.Tamano
			#La posicion del Submenu sera la posicion en x del boton y la posicion en y
			#de la barra de menu q lo posea mas su alto
			posx=self.Menus[contador].pos_x
			posy=posy1+h
		
			SubBarraMenu=MayCSubBarraMenu(self.Interface_Padre,(posx,posy),(150,60),self.Directorio_Recursos_Iconos)
			self.Menus[contador].CreacionSubBarraMenu(SubBarraMenu,L_IdsBotones,L_Imagenes,L_Mensajes,p_No_Botones=L_NoBotones)
			
	def InsertarInterface(self):
		self.Interface_Padre.blit(self.Interface,self.Posicion_Actual)					
		self.InsertarSubMenu()
		self.InsertarMensajesAyuda()
		
	def InsertarSubMenu(self):
		#Solo se Insertara el Submenu Cuando se haya dado click a la Barra de Menu
		#y Solo cuando sea un Boton que pertenezca a un Menu Superior 
		#ya que solo ellos pueden poseer SubMenu, sino se cumplen estas condiciones se sale del Metodo
		if(self.Boton_NJuego == None or self.Raton_Click==False or self.SubMenu==False):
			return

		#Se Imprime el SubMenu solo si se dio Click en un Boton que lo posea
		self.Boton_NJuego.SubBarraMenu.InsertarInterface()
	
	def InsertarMensajesAyuda(self):
		if(self.Raton_Dentro==True):
			self.AgregarMensaje()
		elif(self.Raton_Fuera==True):
			self.QuitarMensaje()
								
	def MovimientoDRaton(self,p_Evento):
		if(self.VerificaEvento(p_Evento)==True):
			Boton=self.BusquedaBoton(p_Evento)
		
			if(self.Raton_Dentro==False and Boton != None):
				self.EvtEntraRaton()
				self.Boton_NJuego.Pos_Mensaje=p_Evento.pos
			elif(self.Raton_Fuera==False and Boton ==None):
				self.EvtSaleRaton()
			return True		
		else:
			#Prueba si se ha hecho este evento en la Subbarra de Menu
			if(self.SubMenu==True and self.Raton_Click==True):
				if(self.Boton_NJuego.SubBarraMenu.MovimientoDRaton(p_Evento)):
					return True				
	
	def EvtEntraRaton(self):
		self.Raton_Dentro=True
		self.Raton_Fuera=False
				
	def EvtSaleRaton(self):
		self.Raton_Fuera=True
		self.Raton_Dentro=False
								
	def PresionDRaton(self,p_Evento):
		if(self.VerificaEvento(p_Evento)==True):
			Boton=self.BusquedaBoton(p_Evento)
			if(Boton != None):
				self.EvtClick()
				print 'Click en  Menu'
			else:
				self.ReIniciar()
			return True	
		else:
			#Prueba si se ha hecho este evento en la Subbarra de Menu
			if(self.SubMenu==True and self.Raton_Click==True):
				if (self.Boton_NJuego.SubBarraMenu.PresionDRaton(p_Evento)):
					return True
			self.ReIniciar()
	
	def EvtClick(self):
		#Cuando el Boton es presionado dos veces Raton_Click sera falso y ya no se imprimira el submenu del Boton presionado
		if(self.Raton_Click==False):
			self.Raton_Click=True
			if (self.SubMenu==False):
				self.Boton_NJuego.Click()
		else:	
			self.Raton_Click=False
											
	#Busca si se concentra un Posible evento en la Interface
	def VerificaEvento(self,p_evento):
		pos_x2,pos_y2=p_evento.pos
		
		pos_x,pos_y=self.ObtenerPosicion()
		Ancho,Alto=self.ObtenerTamano()
	
		if ((pos_x2>=pos_x and pos_x2<=(pos_x+Ancho)) and (pos_y2>=pos_y and pos_y2<=(pos_y+Alto))):
			self.Habilitado=True
			return True
		else:
			self.Habilitado=False
			return False

	def BusquedaBoton(self,evento):
		for contador in range(len(self.Menus)):
			if (self.Menus[contador].Busqueda(evento.pos,self.Posicion_Actual)):
				#Boton en Juego
				self.Boton_NJuego=self.Menus[contador]
				return self.Menus[contador]					