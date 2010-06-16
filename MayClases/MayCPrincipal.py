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
from MayJuegos.MayCJAhorcado import MayCJAhorcado
			
class MayCPrincipal():
	def __init__(self,p_path_recursos):
		self.path_recursos_Ico=p_path_recursos+"/MayIconos"
		self.Tamano_Pantalla=(640, 500)
		#Parametros Barra Superior
		self.Imagenes_Barra_Superior=['MayI01.png','MayI02.png','MayI03.png']
		self.Mensajes_Barra_Superior=['Mensaje Ayuda 1','Mensaje Ayuda 2','Mensaje Ayuda 3']
		self.Ids_Botones_Barra_Superior=['btnArchivo','btnAcerca_de','btnIncognito']
		
		#Parametros Menus Barra Superior
		self.Imagenes_SubBarraMenus=[['MayINavegar.png','MayIOff.png'],['MayITools.png','MayIStop.png'],['MayIFrwd.png','MayIFavs-caution.png']]
		self.Mensajes_SubBarraMenus=[['Salir','Submensaje Ayuda 2'],['Submensaje Ayuda 1','Submensaje Ayuda 2'],['Submensaje Ayuda 1','Submensaje Ayuda 2']]
		self.Ids_Botones_SubBarraMenus=[['Nuevo','Incognito'],['Ayuda','Incognito'],['Incognito','Incognito']]
		self.Menus_xSubBarraMenus=[2,2,2]
		
		#Parametros Barra Lateral
		self.Imagenes_Barra_Lateral=['MayIBuy-shop.png','MayIComment-help.png','MayIPrint.png']
		self.Mensajes_Barra_Lateral=['Juego Ahorcado Teorico','Mensaje Late 2','Mensaje Late 3']
		self.Ids_Botones_Barra_Lateral=['btnAhorcado','btnMemoria','btnIncognito']
		
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
			
			########################################Creacion Menu Superior########################################################
			self.Menu_Superior=MayCBarraMenu(self.Pantalla_Principal,self.Posicion_Surface1,self.Tamano_Surface1,self.path_recursos_Ico,'Horizontal',p_SubMenu=True)
			#Parametros a enviar para la creacion de los Botones del Menu Superior
			#Listas
			L_IDs_Botones=self.Ids_Botones_Barra_Superior
			L_Imagenes=self.Imagenes_Barra_Superior
			L_Mensajes=self.Mensajes_Barra_Superior
			
			self.Menu_Superior.CreacionBotones(L_IDs_Botones,L_Imagenes,L_Mensajes,p_Posicion=(10,5),p_Tamano=(70,90),p_No_Menus=3)
			#Parametros a enviar para la creacion de los SubMenus del Menu Superior
			#Listas
			L_IdsBotones=self.Ids_Botones_SubBarraMenus
			L_Imagenes=self.Imagenes_SubBarraMenus
			L_Mensajes=self.Mensajes_SubBarraMenus
			L_NoBotones=self.Menus_xSubBarraMenus
			
			self.Menu_Superior.CreacionSubBarraMenu(L_IdsBotones,L_Imagenes,L_Mensajes,L_NoBotones)

			self.Menu_Superior.InsertarInterface()

			#########################################Creacion Menu Lateral##########################################################
			self.Menu_Lateral=MayCBarraMenu(self.Pantalla_Principal,self.Posicion_Surface2,self.Tamano_Surface2,self.path_recursos_Ico,'Vertical')
			
			#Parametros a enviar para la creacion de los Botones del Menu Lateral
			#Listas
			L_IDs_Botones=self.Ids_Botones_Barra_Lateral
			L_Imagenes=self.Imagenes_Barra_Lateral
			L_Mensajes=self.Mensajes_Barra_Lateral
						
			self.Menu_Lateral.CreacionBotones(L_IDs_Botones,L_Imagenes,L_Mensajes,p_Posicion=(10,10),p_Tamano=(80,90),p_No_Menus=3)
			self.Menu_Lateral.InsertarInterface()
			
			##################################Creacion de la pantalla donde se desarrolla el juego#################################
			self.Interface_Juego=MayCDesarrolloJuegos(self.Pantalla_Principal,self.Posicion_Surface3,self.Tamano_Surface3,self.path_recursos_Ico,'MayIGJaguar.png',1)
			self.Interface_Juego.Insertar()
			
			#Asigna eventos a los Objetos (Botones)
			self.AsignacionEventos()
			
		except pygame.error, e:
			print "Error al crear la Pantalla"
			print e
			exit()
	
	def AsignacionEventos(self):
		#Barra Superior
		self.Menu_Superior.Menus[0].SubBarraMenu.SubMenus[0].evtclick=self.Salir
		
		#Barra Lateral
		self.Menu_Lateral.Menus[0].evtclick=self.Ahorcado
					
	def Salir(self):
		exit()
	
	def Ahorcado(self):
		MayCJAhorcado()
					
	def ReImprimir(self,p_Evento=None):
		
		#Inserccion de la Interface donde se desarrolla el juego
		self.Interface_Juego.Insertar()
				
		#Inserccion Menu Lateral a la Pantalla
		self.Menu_Lateral.InsertarInterface()
		
		#Inserccion Menu Superior a la Pantalla
		#Esta Inserccion incluye la de los submenus si se dio click a un Boton
		self.Menu_Superior.InsertarInterface()
		
		#Inserccion de Mensajes de Ayuda (Tooltips)
	#	self.Menu_Superior.InsertarMensajesAyuda()
	#	self.Menu_Lateral.InsertarMensajesAyuda()
												
	def MayaCiclo(self):
		#Capturador de Eventos
		while True:
			for evento in pygame.event.get():
				#El Evento Quit ocurre cuando se ha presionado el boton de cerrar
				if evento.type==QUIT:
					self.Salir()
					
				#Este Tipo de Evento indica que se ha Presionado algun Boton del Raton
				#Sobre la Pantalla Display		
				if evento.type==MOUSEBUTTONDOWN:
					#El Evento PresionDRaton Verifica si el evento MOUSEBUTTONDOWN afecta a Menu
					#Dependiendo de eso se realiza una Accion 
					if(self.Menu_Superior.PresionDRaton(evento)):
						self.ReImprimir(evento)
						continue
					
					self.Menu_Lateral.PresionDRaton(evento)
					
					#Reimprime la Pantalla Principal
					self.ReImprimir(evento)
				#Este Tipo de Evento indica que se ha movido el Raton
				#Sobre la Pantalla Display							
				if evento.type==MOUSEMOTION:
					#El Evento MovimientoDRaton Verifica si el evento MOUSEMOTION afecta a Menu
					#Dependiendo de eso se realiza una Accion 
					if(self.Menu_Superior.MovimientoDRaton(evento)):
						self.ReImprimir(evento)
						continue
					self.Menu_Lateral.MovimientoDRaton(evento)
					#Reimprime la Pantalla Principal
					self.ReImprimir(evento)
			#Actualiza la Pantalla Completa
			pygame.display.flip()						
