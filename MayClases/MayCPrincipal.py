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

import pygame,time
from pygame.locals import *
from sys import exit
from MayCBarraMenu import MayCBarraMenu
import os.path

class MayCPrincipal():
	def __init__(self,p_path_recursos):
		self.path_recursos_Ico=p_path_recursos+"/MayIconos"
		self.Tamano_Pantalla=(640, 500)
		self.Imagenes_Barra_Superior=['MayI01.png','MayI02.png','MayI03.png']
		self.Mensajes_Barra_Superior=['Mensaje Ayuda 1','Mensaje Ayuda 2','Mensaje Ayuda 3']
		
		self.Imagenes_Barra_Lateral=['MayIBuy-shop.png','MayIComment-help.png','MayIPrint.png']
		self.Mensajes_Barra_Lateral=['Mensaje Lateral Ayuda 1','Mensaje Lateral Ayuda 2','Mensaje Lateral Ayuda 3']
		
		self.Imagenes_SubMenus=[['MayINavegar.png','MayIOff.png'],['MayITools.png','MayIStop.png'],['MayIFrwd.png','MayIFavs-caution.png']]
		self.Mensajes_SubMenus=[['Submensaje Ayuda 1','Submensaje Ayuda 2'],['Submensaje Ayuda 1','Submensaje Ayuda 2'],['Submensaje Ayuda 1','Submensaje Ayuda 2']]
		self.Menus_xSubmenus=[2,2,2]
		#Menu Superior
		self.Tamano_Surface1=(640,100)
		self.Posicion_Surface1=(0,0)
		#Menu Lateral
		self.Tamano_Surface2=(100,465)
		self.Posicion_Surface2=(0,100)
		#Desarrollo del Juego
		self.Tamano_Surface3=(530,400)
		self.Posicion_Surface3=(100,100)
		
		self.Iniciar()
		self.MayaCiclo()

	def Iniciar(self):
		#Inicializo los Submódulos de Pygame
		pygame.init()
		try:
			pygame.display.set_icon(pygame.image.load(os.path.join(self.path_recursos_Ico, "MayI01.png")))
			pygame.display.set_caption("Juegos Para el Desarrollo Maya")
			self.Pantalla_Principal = pygame.display.set_mode(self.Tamano_Pantalla, 0, 32)
			self.Fondo=pygame.image.load(os.path.join(self.path_recursos_Ico,'MayIGJaguar.png')).convert_alpha()
			self.Fondo=pygame.transform.scale(self.Fondo,(565,400))
			
			#Creacion Menu Superior
			self.Menu_Superior=MayCBarraMenu(self.Posicion_Surface1,self.Tamano_Surface1,self.path_recursos_Ico,'Horizontal')
			self.Menu_Superior.CreacionMenus(3,self.Imagenes_Barra_Superior,self.Mensajes_Barra_Superior,(10,5),(70,100),'Menu')
			self.Subme(len(self.Menu_Superior.Menus))
			self.Menu_Superior.Agregar(self.Pantalla_Principal)
			
			#Creacion Menu Lateral
			self.Menu_Lateral=MayCBarraMenu(self.Posicion_Surface2,self.Tamano_Surface2,self.path_recursos_Ico,'Vertical')
			self.Menu_Lateral.CreacionMenus(3,self.Imagenes_Barra_Lateral,self.Mensajes_Barra_Lateral,(10,5),(70,100),'Menu')
			self.Menu_Lateral.Agregar(self.Pantalla_Principal)
			
			#Creacion de la pantalla donde se desarrolla el juego
			self.Pantalla_Principal.blit(self.Fondo,(75,100))
			
		except pygame.error, e:
			print "Error al crear la Pantalla"
			print e
			exit()
	
	def Subme(self,p_No_Menus):
		for contador in range(p_No_Menus):
			SubBarraMenu=MayCBarraMenu((0,0),(150,60),self.path_recursos_Ico,'Horizontal')
			self.Menu_Superior.Menus[contador].CreacionSubMenu(self.Menus_xSubmenus[contador],SubBarraMenu,self.Imagenes_SubMenus[contador],self.Mensajes_SubMenus[contador])		
		
	def ReImprimir(self,p_Boton):
		
		self.Pantalla_Principal.fill((0,0,0))		
		#Inserccion Menu Superior
		self.Menu_Superior.Agregar(self.Pantalla_Principal)		
		
		#Inserccion Menu Lateral
		self.Menu_Lateral.Agregar(self.Pantalla_Principal)
		
		#Creacion de la pantalla donde se desarrolla el juego
		self.Pantalla_Principal.blit(self.Fondo,(75,100))
		
		if (p_Boton !=None):
			self.Pantalla_Principal.blit(p_Boton.ObtenerSubMenu(),(p_Boton.pos_x,100))
	
	def BusquedaGeneral(self,p_evento):
		Interfaces=[self.Menu_Superior,self.Menu_Lateral]
		pos_x2,pos_y2=p_evento.pos
		
		for interface in Interfaces:
			pos_x,pos_y=interface.ObtenerPosicion()
			Ancho,Alto=interface.ObtenerTamano()
			
			if ((pos_x2>=pos_x and pos_x2<=(pos_x+Ancho)) and (pos_y2>=pos_y and pos_y2<=(pos_y+Alto))):
				return interface
													
	def MayaCiclo(self):
		entro=False
		click=False
		#Capturador de Eventos
		while True:
			for evento in pygame.event.get():
				if evento.type==QUIT:
					exit()
						
				if evento.type==MOUSEBUTTONDOWN:
					interface=self.BusquedaGeneral(evento)
					if (interface!=None):
						Boton=interface.BusquedaMenu(evento)
					else:
						Boton=None	
					if (Boton != None):
						if (Boton.Rango=='Menu'):
							self.ReImprimir(Boton) 
							click=True
							print 'Se ha Dado click a un Menu'
					else:
						self.ReImprimir(None)
						click=False	
							
				if evento.type==MOUSEMOTION:
					interface=self.BusquedaGeneral(evento)
					if (interface!=None):
						Boton=interface.BusquedaMenu(evento)
					else:
						Boton=None
							
					if (entro==False and Boton != None):
						entro=True
						interface.AgregarMensaje(Boton,evento.pos)
						#Reimprime la Pantalla Principal			
						self.ReImprimir(None)	
					elif (entro==True and Boton==None):
						entro=False
						interface.QuitarMensaje()
						#Reimprime la Pantalla Principal			
						self.ReImprimir(None)
			
			#Actualiza la Pantalla						
			pygame.display.flip()