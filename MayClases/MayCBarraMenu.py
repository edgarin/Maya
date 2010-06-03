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

class MayCBarraMenu(object):
	def __init__(self,p_Interface_Padre,p_Posicion,p_Tamano,p_Directorio_Recursos_Iconos,p_Tipo,p_Habilitado=True):
		#Inicializo SubMódulos de Pygamep_Mensaje
		pygame.init()
		#Interface en la cual la BarraMenu sera Insertada
		self.Interface_Padre=p_Interface_Padre
		self.Tamano=p_Tamano
		self.Posicion_Actual=p_Posicion
		self.Interface=pygame.Surface(p_Tamano,0,32)
		self.Tipo=p_Tipo
		#Propiedades
		self.Directorio_Recursos_Iconos=p_Directorio_Recursos_Iconos	
		self.Interface.fill((255,255,255))
		#Creacion Items Menu Bar
		self.Menus=[]
		#Boton en Juego (Que esta Interactuando con los eventos =>MOUSEMOTION)
		self.Boton_NJuego=None
		#Variables de Eventos de Raton
		self.Raton_Dentro=False
		self.Raton_Fuera=True
		self.Raton_Click=False
		self.Habilitado=p_Habilitado
		
	def Obtener(self):
		return self.Interface
		
	def AgregarMensaje(self,p_posicion_mensaje=None):
		if (p_posicion_mensaje==None):
			#Agrego Mensaje tooltip
			self.Boton_NJuego.AgregarMensaje(p_Interface=self.Interface_Padre)		
	
	def Habilitar(self,p_Si_No):
		self.Habilitado=p_Si_No
		
	def QuitarMensaje(self):
		self.ReIniciarClase(p_QM=True)
	
	def ReIniciarClase(self,p_QM=False):
		self.Interface.fill((255,255,255))

		if (p_QM==False):
			self.Raton_Click=False
		
		for contador in range(len(self.Menus)):
			self.Menus[contador].Insertar()
			
	def BusquedaMenu(self,evento):
		for contador in range(len(self.Menus)):
			if (self.Menus[contador].Busqueda(evento.pos)):
				#Boton en Juego
				self.Boton_NJuego=self.Menus[contador]
				return self.Menus[contador]		
	
	def ObtenerPosicion(self):
		return self.Posicion_Actual
		
	def ObtenerTamano(self):
		return self.Tamano		
	
	def CreacionMenus(self,p_No_Menus,p_Imagenes,p_Mensajes_Ayuda,p_Posicion,p_Tamano,p_Tipo='Menu'):
		posx,posy=p_Posicion
		ancho,alto=p_Tamano
		for contador in range(p_No_Menus):
			nombre='Menu'+str(contador)
			Nombre_Imagen=p_Imagenes[contador]
			Mensaje=p_Mensajes_Ayuda[contador]
			
			if (self.Tipo=='Horizontal'):
				Boton_de_Menu=MayCBoton(self.Interface,nombre,Nombre_Imagen,self.Directorio_Recursos_Iconos,(posx+((ancho+10)*contador),posy),(ancho,alto),p_Tipo)
			elif (self.Tipo=='Vertical'):
				Boton_de_Menu=MayCBoton(self.Interface,nombre,Nombre_Imagen,self.Directorio_Recursos_Iconos,(posx,posy+((alto+10)*contador)),(ancho,alto),p_Tipo)
				
			Boton_de_Menu.MensajeAyuda(Mensaje)
			#Agregar Boton a la Interface
			Boton_de_Menu.Insertar()
			self.Menus.append(Boton_de_Menu)		
	
	def Insertar(self):
		self.Interface_Padre.blit(self.Interface,self.Posicion_Actual)					
		self.InsertarSubMenu()
		
	def InsertarSubMenu(self):
		#Solo se Insertara el Submenu Cuando se haya dado click a la Barra de Menu
		#y Solo cuando sea un Boton que pertenezca a un Menu Superior 
		#ya que solo ellos pueden poseer SubMenus, sino se cumplen estas condiciones se sale del Metodo
		if(self.Boton_NJuego == None or self.Raton_Click==False or self.Boton_NJuego.Tipo!='BMenuSuperior'):
			return

		#Se Imprime el SubMenu solo si se dio Click en un Boton que lo posea
		#En este Juego solo los Menu_Superior los tienen
		self.Interface_Padre.blit(self.Boton_NJuego.ObtenerSubMenu(),(self.Boton_NJuego.pos_x,100))
		
	def EvtEntraRaton(self):
		self.Raton_Dentro=True
		self.Raton_Fuera=False
				
	def EvtSaleRaton(self):
		self.Raton_Fuera=True
		self.Raton_Dentro=False
	
	def MensajesAyuda(self):
		if(self.Raton_Dentro==True):
			self.AgregarMensaje()
		elif(self.Raton_Fuera==True):
			self.QuitarMensaje()
				
	def EvtClick(self):
		#Si el Boton en Juego que es el que se Origina cuando el Mouse entra en un Boton siendo este en Juego pertenece
		#a un Menu Superior este actuara de la Manera Siguiente
		if(self.Boton_NJuego.Tipo=='BMenuSuperior'):
			#Cuando el Boton es presionado dos veces Raton_Click sera falso y ya no se imprimira el submenu del Boton presionado
			if(self.Raton_Click==False):
				self.Raton_Click=True
			else:	
				self.Raton_Click=False
				print 'Se dio click en un '+ self.Tipo
		else:
			pass
				
	def MovimientoDRaton(self,p_Evento):
		if(self.VerificaEvento(p_Evento)==False):
			#Prueba si se ha hecho este evento en el SubMenus
			if(self.Raton_Click==True and self.Boton_NJuego.Tipo=='BMenuSuperior'):
				self.Boton_NJuego.SubMenu.MovimientoDRaton(p_Evento)
				
			return
		Boton=self.BusquedaMenu(p_Evento)
		
		if(self.Raton_Dentro==False and Boton != None):
			self.EvtEntraRaton()
			self.Boton_NJuego.Pos_Mensaje=p_Evento.pos
		elif(self.Raton_Fuera==False and Boton ==None):
			self.EvtSaleRaton()	
					
	def PresionDRaton(self,p_Evento):
		if(self.VerificaEvento(p_Evento)==False):
			#Prueba si se ha hecho este evento en el SubMenus
			if(self.Raton_Click==True and self.Boton_NJuego.Tipo=='BMenuSuperior'):
				self.Boton_NJuego.SubMenu.PresionDRaton(p_Evento)
				return
			else:	
				self.ReIniciarClase()
				return
		
		Boton=self.BusquedaMenu(p_Evento)
		
		if( Boton != None):
			self.EvtClick()
		else:
			self.ReIniciarClase()
						
	#Busca si se concentra un Posible evento en la Interface
	def VerificaEvento(self,p_evento):
		pos_x2,pos_y2=p_evento.pos
		
		pos_x,pos_y=self.ObtenerPosicion()
		Ancho,Alto=self.ObtenerTamano()
			
		if ((pos_x2>=pos_x and pos_x2<=(pos_x+Ancho)) and (pos_y2>=pos_y and pos_y2<=(pos_y+Alto))):
			return True
		else:
			return False		