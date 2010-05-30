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

import pygame
import os.path
from MayCBoton import MayCBoton

class MayCBarraMenu(object):
	def __init__(self,p_Interface_Padre,p_Posicion,p_Tamano,p_Directorio_Recursos_Iconos,p_Tipo):
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
		#Boton al que se le ha dado click
		self.Boton_Presionado=None
		#Variables de Eventos de Raton
		self.Raton_Dentro=False
		self.Raton_Fuera=True
		self.Raton_Click=False
		
	def Obtener(self):
		return self.Interface
		
	def AgregarMensaje(self,p_posicion_mensaje):
		#Agrego Mensaje tooltip
		self.Boton_NJuego.AgregarMensaje(p_posicion_mensaje)		
	
	def QuitarMensaje(self):
		#Indica que se Movio del Boton en q tal vez se dio click y se pone como false
		#--------------------------------------------- self.Menu_Presionado=None
		self.Interface.fill((255,255,255))
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
		
	def EvtEntraRaton(self,p_Evento):
		self.Raton_Dentro=True
		self.Raton_Fuera=False
		self.AgregarMensaje(p_Evento.pos)
		
	def EvtSaleRaton(self):
		self.Raton_Fuera=True
		self.Raton_Dentro=False
		self.QuitarMensaje()
		
	def EvtClick(self):
		#Cuando el Boton es presionado dos veces Raton_Click sera falso y ya no se imprimira el submenu del Boton presionado
		if(self.Boton_NJuego==self.Boton_Presionado):
			self.Raton_Click=False
			self.Boton_Presionado=None
		else:	
			self.Raton_Click=True
			self.Boton_Presionado=self.Boton_NJuego