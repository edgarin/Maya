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
import pygame,time
from pygame.locals import *
from sys import exit
from MayCBarraMenu import MayCBarraMenu
from MayCDesarrolloJuegos import  MayCDesarrolloJuegos
import os.path
			
class MayCPrincipal():
	def __init__(self,p_path_recursos):
		self.path_recursos_Ico=p_path_recursos+"/MayIconos"
		self.Tamano_Pantalla=(640, 500)
		self.Imagenes_Barra_Superior=['MayI01.png','MayI02.png','MayI03.png']
		self.Mensajes_Barra_Superior=['Mensaje Ayuda 1','Mensaje Ayuda 2','Mensaje Ayuda 3']
		
		self.Imagenes_Barra_Lateral=['MayIBuy-shop.png','MayIComment-help.png','MayIPrint.png']
		self.Mensajes_Barra_Lateral=['Mensaje Late 1','Mensaje Late 2','Mensaje Late 3']
		
		self.Imagenes_SubMenus=[['MayINavegar.png','MayIOff.png'],['MayITools.png','MayIStop.png'],['MayIFrwd.png','MayIFavs-caution.png']]
		self.Mensajes_SubMenus=[['Submensaje Ayuda 1','Submensaje Ayuda 2'],['Submensaje Ayuda 1','Submensaje Ayuda 2'],['Submensaje Ayuda 1','Submensaje Ayuda 2']]
		self.Menus_xSubmenus=[2,2,2]
		#Menu Superior
		self.Tamano_Surface1=(640,100)
		self.Posicion_Surface1=(0,0)
		#Menu Lateral
		self.Tamano_Surface2=(110,465)
		self.Posicion_Surface2=(0,100)
		#Desarrollo del Juego
		self.Tamano_Surface3=(530,400)
		self.Posicion_Surface3=(110,100)
		
		self.Iniciar()
		self.MayaCiclo()

	def Iniciar(self):
		#Inicializo los Submódulos de Pygame
		pygame.init()
		
		try:
			pygame.display.set_icon(pygame.image.load(os.path.join(self.path_recursos_Ico, "MayI01.png")))
			pygame.display.set_caption("Juegos Para el Desarrollo Maya")
			self.Pantalla_Principal = pygame.display.set_mode(self.Tamano_Pantalla, 0, 32)
			
			#Creacion Menu Superior
			self.Menu_Superior=MayCBarraMenu(self.Pantalla_Principal,self.Posicion_Surface1,self.Tamano_Surface1,self.path_recursos_Ico,'Horizontal')
			self.Menu_Superior.CreacionMenus(3,self.Imagenes_Barra_Superior,self.Mensajes_Barra_Superior,(10,5),(70,90),p_Tipo='BMenuSuperior')
			self.Subme(len(self.Menu_Superior.Menus))
			self.Menu_Superior.Insertar()
			
			#Creacion Menu Lateral
			self.Menu_Lateral=MayCBarraMenu(self.Pantalla_Principal,self.Posicion_Surface2,self.Tamano_Surface2,self.path_recursos_Ico,'Vertical')
			self.Menu_Lateral.CreacionMenus(3,self.Imagenes_Barra_Lateral,self.Mensajes_Barra_Lateral,(10,10),(80,90),p_Tipo='BMenuLateral')
			self.Menu_Lateral.Insertar()
			
			#Creacion de la pantalla donde se desarrolla el juego
			self.Interface_Juego=MayCDesarrolloJuegos(self.Pantalla_Principal,self.Posicion_Surface3,self.Tamano_Surface3,self.path_recursos_Ico,'MayIGJaguar.png',1)
			#self.Interface_Juego.Insertar()
			#self.Pantalla_Principal.blit(self.Fondo,(75,100))
			
		except pygame.error, e:
			print "Error al crear la Pantalla"
			print e
			exit()
	
	def Subme(self,p_No_Menus):
		for contador in range(p_No_Menus):
			SubBarraMenu=MayCBarraMenu(self.Pantalla_Principal,(0,0),(150,60),self.path_recursos_Ico,'Horizontal')
			self.Menu_Superior.Menus[contador].CreacionSubMenu(self.Menus_xSubmenus[contador],SubBarraMenu,self.Imagenes_SubMenus[contador],self.Mensajes_SubMenus[contador])		
			
	def ReImprimir(self,p_Reimprime=None):
		#Si se dio Click en un Menu con Submenu ya no vuelve a Reimprimir hasta q se de click 
		#afuera del Menu seleccionado
		if (p_Reimprime==True):
			return				
		
		#Inserccion Menu Lateral a la Pantalla
		self.Menu_Lateral.Insertar()
		
		#Inserccion de la Interface donde se desarrolla el juego
		#self.Interface_Juego.Insertar()
		
		#Inserccion Menu Superior a la Pantalla
		#Esta Inserccion incluye la de los submenus si se dio click a un Boton
		self.Menu_Superior.Insertar()
		
		self.Menu_Superior.MensajesAyuda()
		self.Menu_Lateral.MensajesAyuda()
												
	def MayaCiclo(self):
		entro=False
		Reimprime=False
		Boton_Jue=None
		Interface_Jue=None
		
		#Capturador de Eventos
		while True:
			for evento in pygame.event.get():
				#El Evento Quit ocurre cuando se ha presionado el boton de cerrar
				if evento.type==QUIT:
					exit()
					
				#Este Tipo de Evento indica que se ha Presionado algun Boton del Raton
				#Sobre la Pantalla Display		
				if evento.type==MOUSEBUTTONDOWN:
					#El Evento PresionDRaton Verifica si el evento MOUSEBUTTONDOWN afecta a Menu
					#Dependiendo de eso se realiza una Accion 
					self.Menu_Superior.PresionDRaton(evento)
					self.Menu_Lateral.PresionDRaton(evento)
					#Reimprime la Pantalla Principal
					self.ReImprimir()
				#Este Tipo de Evento indica que se ha movido el Raton
				#Sobre la Pantalla Display							
				if evento.type==MOUSEMOTION:
					#El Evento MovimientoDRaton Verifica si el evento MOUSEMOTION afecta a Menu
					#Dependiendo de eso se realiza una Accion 
					self.Menu_Superior.MovimientoDRaton(evento)
					self.Menu_Lateral.MovimientoDRaton(evento)
					#Reimprime la Pantalla Principal
					self.ReImprimir()
			self.Interface_Juego.Desktop.update()
			self.Interface_Juego.Desktop.draw()
			#Actualiza la Pantalla						
			pygame.display.update()
