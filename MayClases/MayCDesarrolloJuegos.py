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
#
import pygame
import os.path
from MayCBoton import MayCBoton
from MayJuegos.MayCJAhorcado import MayCJAhorcado

import MayJuegos.gui
from MayJuegos.gui import *
import MayJuegos.defaultStyle

class MayCDesarrolloJuegos(object):
	def __init__(self,p_Interface_Padre,p_Posicion,p_Tamano,p_Directorio_Recursos_Iconos,p_Imagen_Fondo,p_Juego,p_Habilitado=True):
		#Inicializo SubMódulos de Pygamep_Mensaje
		pygame.init()
		#Interface en la cual la BarraMenu sera Insertada
		self.Interface_Padre=p_Interface_Padre
		self.Interface=pygame.Surface(p_Tamano,0,32)
		MayJuegos.defaultStyle.init(MayJuegos.gui)
		
		self.Desktop = MayJuegos.gui.Desktop()
			 
		#Propiedades
		self.Tamano=p_Tamano
		self.Posicion_Actual=p_Posicion	
		self.Habilitado=p_Habilitado
		self.Directorio_Imagenes=p_Directorio_Recursos_Iconos
		self.Imagen_Fondo=None
		#self.Fondo(p_Imagen_Fondo,self.Directorio_Imagenes)
		#Integrar Juego Selccionado
		self.QueJuego(p_Juego)
	
	def Fondo(self,p_Imagen_Nombre,p_Directorio_Imagen,p_Tamano=None):
		if(p_Tamano==None):
			self.Imagen_Fondo=pygame.image.load(os.path.join(p_Directorio_Imagen,p_Imagen_Nombre))
			self.Imagen_Fondo=pygame.transform.scale(self.Imagen_Fondo,self.Tamano)
		
	def InsertarFondo(self):
		self.Interface.blit(self.Imagen_Fondo,(0,0))
	
	def ObtenerFondo(self):
		return self.Imagen_Fondo
					
	def Insertar(self):
		self.InsertarFondo()
		self.Interface_Padre.blit(self.Interface,self.Posicion_Actual)					
		 
	def QueJuego(self,p_Juego):
		if (p_Juego==1):
			self.Ahorcado=MayCJAhorcado(self.Interface,self.Desktop)
			pass