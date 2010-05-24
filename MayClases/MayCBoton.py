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

class MayCBoton(object):
	def __init__(self,p_ID,p_Imagen_Nombre,p_Directorio_Imagen,p_Coordenadas,p_Tamano,p_Rango):
		#Inicializo SubMódulos de Pygamep_Mensaje
		pygame.init()
		#Propiedades
		self.ID=p_ID
		self.nombre=p_Imagen_Nombre
		self.pos_x,self.pos_y=p_Coordenadas
		self.Ancho,self.Alto=p_Tamano
		self.Directorio_Imagenes=p_Directorio_Imagen
		self.imagen=pygame.image.load(os.path.join(p_Directorio_Imagen,p_Imagen_Nombre))
		self.imagen=pygame.transform.scale(self.imagen,(self.Ancho,self.Alto))
		self.Mensaje_Ayuda=''
		self.Rango=p_Rango
		self.SubMenu=None
				
	def Agregar(self,p_Superficie):
		p_Superficie.blit(self.imagen,(self.pos_x,self.pos_y))
				
	def AgregarMensaje(self,p_Superficie,p_Posicion):
		p_Superficie.blit(self.Mensaje_Ayuda,p_Posicion)
	
	def MensajeAyuda(self,Mensaje):
		Fuente_Mensaje = pygame.font.SysFont("arial", 16)
		self.Mensaje_Ayuda = Fuente_Mensaje.render(Mensaje, True, (0, 0, 0), (150, 155, 175))	
			
	def ObtenerMensaje(self):
		return self.Mensaje_Ayuda
			
	def Busqueda(self,posicion_click):
		pos_x2,pos_y2=posicion_click
		
		if ((pos_x2>=self.pos_x and pos_x2<=(self.pos_x+self.Ancho)) and (pos_y2>=self.pos_y and pos_y2<=(self.pos_y+self.Alto))):
			return True	
			
	def CreacionSubMenu(self,p_No_Botones,p_SubBarraMenu,p_Imagenes,p_Mensajes_Ayuda):
		self.SubMenu=p_SubBarraMenu
		self.SubMenu.CreacionMenus(p_No_Botones,p_Imagenes,p_Mensajes_Ayuda,(0,0),(40,50),'SubMenu')
	
	def ObtenerSubMenu(self):
		return self.SubMenu.Obtener()	
		
	def Click(self,p_Interface):		
		if (self.Rango=='Menu'):
			p_Interface.blit(self.SubMenu.Obtener(),(0,100))			
