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

class MayCBoton(object):
	def __init__(self,p_Interface_Padre,p_ID,p_Imagen_Nombre,p_Directorio_Imagen,p_Coordenadas=(0,0),p_Tamano=(0,0),p_Habilitado=True):
		#Inicializo SubMódulos de Pygamep_Mensaje
		pygame.init()
		#Propiedades
		self.ID=p_ID
		self.pos_x,self.pos_y=p_Coordenadas
		self.Ancho,self.Alto=p_Tamano
		self.Directorio_Imagenes=p_Directorio_Imagen
		self.Imagen_Nombre=p_Imagen_Nombre
		#Se asigna la Imagen
		self.CImagen()
		self.Mensaje_Ayuda=''
		self.Pos_Mensaje=(0,0)
		#Indica si el Boton posee una SubBarraMenu
		self.SubBarraMenu=None
		#Evento del Boton
		self.evtclick=None
		#Menu al Que Pertenece le Boton
		self.Interface_Padre=p_Interface_Padre 
		self.Habilitado=p_Habilitado
				
	def Insertar(self,p_Interface=None):
		if (p_Interface==None):
			self.Interface_Padre.blit(self.imagen,(self.pos_x,self.pos_y))
		else:
			p_Interface.blit(self.imagen,(self.pos_x,self.pos_y))
					
	def AgregarMensaje(self,p_Interface=None):
		if (p_Interface==None):
			self.Interface_Padre.blit(self.Mensaje_Ayuda,self.Pos_Mensaje)
		else:
			p_Interface.blit(self.Mensaje_Ayuda,self.Pos_Mensaje)
	
	def ObtImagen(self):
		return self.imagen
	def CImagen(self,p_imagen=None):
		if(self.Directorio_Imagenes!=None and self.Imagen_Nombre!=None):
			self.imagen=pygame.image.load(os.path.join(self.Directorio_Imagenes,self.Imagen_Nombre))
			self.imagen=pygame.transform.scale(self.imagen,(self.Ancho,self.Alto))			
		elif(p_imagen!=None):
			self.imagen=p_imagen
			self.imagen=pygame.transform.scale(self.imagen,(self.Ancho,self.Alto))
		else:
			self.imagen=None
			
	def ObtTamano(self):
		return self.Ancho,self.Alto	
	def CTamano(self,p_tamano):
		self.Ancho,self.Alto = p_tamano
	
	def ObtID(self):
		return self.ID	
	def CID(self,p_id):
		self.ID = p_id
		
	def ObtCoordenadas(self):
		return (self.pos_x,self.pos_y)	
	def CCoordenadas(self,p_coordenadas):
		self.pos_x,self.pos_y = p_coordenadas
				
	def Habilitar(self,p_Si_No):
		self.Habilitado=p_Si_No
		
	def MensajeAyuda(self,Mensaje):
		Fuente_Mensaje = pygame.font.SysFont("arial", 12)
		#(0,0,0)=>Color de Letra (150,155,175)=>Color Fondo 
		#Font.render() devuelve una surface
		self.Mensaje_Ayuda = Fuente_Mensaje.render(Mensaje, True, (0, 0, 0), (150, 155, 175))	
			
	def ObtenerMensaje(self):
		return self.Mensaje_Ayuda
	def PosMensaje(self,p_Pos_Mensaje):
		self.Pos_Mensaje=p_Pos_Mensaje
				
	def Busqueda(self,posicion_click,p_pos_Interface_Padre):
		pos_x2,pos_y2=posicion_click
		#Se saca la posicion en relacion a la Pantalla Principal
		pospadrex,pospadrey=p_pos_Interface_Padre
		pos_x=pospadrex+self.pos_x
		pos_y=pospadrey+self.pos_y
				
		if ((pos_x2>=pos_x and pos_x2<=(pos_x+self.Ancho)) and (pos_y2>=pos_y and pos_y2<=(pos_y+self.Alto))):
			return True	
			
	def CreacionSubBarraMenu(self,p_SubBarramenu,p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_No_Botones=1):
		self.SubBarraMenu=p_SubBarramenu
		self.SubBarraMenu.CreacionBotones(p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_Posicion=(0,0),p_Tamano=(40,50),p_No_SMenus=p_No_Botones)
	
	def ObtenerSubMenu(self):
		return self.SubMenu	
		
	def Click(self):	
		if(self.evtclick==None):
			return	
		self.evtclick()					
