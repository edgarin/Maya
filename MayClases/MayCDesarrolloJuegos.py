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

class MayCDesarrolloJuegos(Object):
	def __init__(self,p_Interface_Padre,p_Posicion,p_Tamano,p_Directorio_Recursos_Iconos,p_Juego,p_Habilitado=True):
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