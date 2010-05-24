#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
#       
#       Copyright 2010 Daniel Sola <danielz360@danielz360-laptop>
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
	def __init__(self,p_Posicion,p_Tamano,p_Directorio_Recursos_Iconos,p_Tipo):
		#Inicializo SubMódulos de Pygamep_Mensaje
		pygame.init()
		self.Tamano=p_Tamano
		self.Posicion_Actual=p_Posicion
		self.Interface=pygame.Surface(p_Tamano,0,32)
		self.Tipo=p_Tipo
		#Propiedades
		self.Directorio_Recursos_Iconos=p_Directorio_Recursos_Iconos	
		self.Interface.fill((255,255,255))
		#Creacion Items Menu Bar
		self.Menus=[]
		self.Menu_Presionado=None
		
	def Obtener(self):
		return self.Interface
		
	def AgregarMensaje(self,p_Boton,p_posicion_mensaje):
		#Agrego Mensaje
		p_Boton.AgregarMensaje(self.Interface,p_posicion_mensaje)		
	
	def QuitarMensaje(self):
		self.Interface.fill((255,255,255))
		for contador in range(len(self.Menus)):
			self.Menus[contador].Agregar(self.Interface)
		
	def BusquedaMenu(self,evento):
		for contador in range(len(self.Menus)):
			if (self.Menus[contador].Busqueda(evento.pos)):
				self.Menu_Presionado=contador
				return self.Menus[contador]		
	
	def ObtenerPosicion(self):
		return self.Posicion_Actual
		
	def ObtenerTamano(self):
		return self.Tamano		
	
	def CreacionMenus(self,p_No_Menus,p_Imagenes,p_Mensajes_Ayuda,p_Posicion,p_Tamano,p_Rango):
		posx,posy=p_Posicion
		ancho,alto=p_Tamano
		for contador in range(p_No_Menus):
			nombre='Menu'+str(contador)
			Nombre_Imagen=p_Imagenes[contador]
			Mensaje=p_Mensajes_Ayuda[contador]
			
			if (self.Tipo=='Horizontal'):
				Boton_de_Menu=MayCBoton(nombre,Nombre_Imagen,self.Directorio_Recursos_Iconos,(posx+((ancho+10)*contador),posy),(ancho,alto),p_Rango)
			elif (self.Tipo=='Vertical'):
				Boton_de_Menu=MayCBoton(nombre,Nombre_Imagen,self.Directorio_Recursos_Iconos,(posx,posy+((alto+10)*contador)),(ancho,alto),p_Rango)
				
			Boton_de_Menu.MensajeAyuda(Mensaje)
			#Agregar Boton a la Interface
			Boton_de_Menu.Agregar(self.Interface)
			self.Menus.append(Boton_de_Menu)		
	
	def Agregar(self,p_Interface):
		p_Interface.blit(self.Interface,self.Posicion_Actual)					
