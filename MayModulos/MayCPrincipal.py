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
import GlobalesI

from MayCNucleo import MayCNucleo
from MayCLabel import MayCLabel
from MayCBarraMenu import MayCBarraMenu
from MayCPanel import MayCPanel
from MayCImagen import MayCImagen
from MayCCuaTexto import MayCCuaTexto

from MayCJAhorcado import MayCJAhorcado
from MayCJMTablero import MayCJMTablero
from MayCAcercaD import  MayCAcercaD

class MayCPrincipal():
	def __init__(self):
		self.Iniciar()
		self.MayaCiclo()

	def Iniciar(self):
		try:
			GI = GlobalesI
			self.Pantalla_Principal = pygame.display.get_surface()
			self.MayCNucleo = MayCNucleo()
			self.MayCNucleo.Pantalla_Principal = self.Pantalla_Principal
			self.MayCNucleo.CDirRecursos(GI.path_recursosico)
			#########################################Creacion Panel##########################################################
			Menu_Superior = MayCBarraMenu(p_SubMenu = True)
			Menu_Superior.CFondo(GI.Fon_BarSu)
			#Parametros a enviar para la creacion de los Botones del Menu Superior
			#Listas
			L_IDs_Botones = GI.Id_Btn_BarSu
			L_Imagenes = GI.Img_BarSu
			L_Mensajes = GI.Mnj_BarSu
			#Parametros Botones
			Tam_btnsu = GI.TamBtn_BarSu
			Pos_btnsu = GI.PosBtn_BarSu
            
	   		Menu_Superior.CreacionMenus(L_IDs_Botones,L_Imagenes,L_Mensajes,p_Posicion = Pos_btnsu,p_Tamano = Tam_btnsu)      
	   		#Parametros a enviar para la creacion de los SubMenus del Menu Superior
	   		#Listas
	   		L_IdsBotones = GI.Id_BtnSubBarMen
	   		L_Imagenes = GI.Img_SubBarMen
	   		L_Mensajes = GI.Mnj_SubBarMen
            
	  		Menu_Superior.CreacionSubBarraMenu(L_IdsBotones,L_Imagenes,L_Mensajes)
	  		Menu_Superior.CFondoSubBars(GI.Fon_BarSu)
	  		self.Menu_Superior = Menu_Superior
			self.Menu_Superior.Insertar()
			#########################################Creacion Panel##########################################################
			self.Panel = MayCPanel(GI.Pos_Surf2, GI.Tam_Surf2)
			self.Panel.CColor(GI.Col_Pan)
			#Parametros a enviar para la creacion de los Botones del Panel
			#Listas
			L_IDs_Botones = GI.Id_Btn_Pan
			L_Imagenes = GI.Img_Pan
			L_Mensajes = GI.Mnj_Pan
			
			#Parametros Botones
			Tam_btnla = GI.TamBtn_Pan
			Pos_btnla = GI.PosBtn_Pan
						
			self.Panel.CreacionBotones(L_IDs_Botones, L_Imagenes, L_Mensajes, p_Posicion = Pos_btnla, p_Tamano = Tam_btnla, p_NoBoton = 3)
			self.lblIngresadas = MayCLabel("Q uts: ", "lblIngresadas", (25, 25), "blanco")
			self.Panel.Adherir(self.lblIngresadas)
			self.TxtPrueba = MayCCuaTexto('TxtPrueba',p_Coordenadas = (50,400),p_Ancho = 200, p_Fuente = 'arial', p_Texto = 'q uts')
			self.TxtPrueba.MensajeAyuda('Pruebitaa')
			self.Panel.Adherir(self.TxtPrueba)
			self.Panel.Insertar()
			
			nombre = self.MayCNucleo.Msj(p_Mensaje = 'Ingresa Tu Nombre...',p_Tipo = 2)
			self.MayCNucleo.Msj(p_Mensaje = 'Bienvenido ' + nombre)
			#Asigna eventos a los Objetos (Botones)
			self.AsignacionEventos()
			pygame.display.update()
			
		except pygame.error, e:
			print "Error al crear la Pantalla"
			exit()
	
	def AsignacionEventos(self):
		#Barra Superior
		self.Menu_Superior.Menus[0].SubBarraMenu.SubMenus[0].evtclick = self.MayCNucleo.Salir
		self.Menu_Superior.Menus[1].SubBarraMenu.SubMenus[0].evtclick = self.AcercaD
		
		#Barra Lateral
		self.Panel.Objetos[0].evtclick = self.Ahorcado
		self.Panel.Objetos[1].evtclick = self.Memoria
	
	def Ahorcado(self):
		self.MayCNucleo.CongObjetos(False)
		Ahorcado = MayCJAhorcado()
		self.MayCNucleo.CongObjetos(True)
		
	def Memoria(self):
		self.MayCNucleo.CongObjetos(False)
		Memoria = MayCJMTablero()
		self.MayCNucleo.CongObjetos(True)
	
	def AcercaD(self):
		self.MayCNucleo.CongObjetos(False)
		AcercaD = MayCAcercaD()
		self.MayCNucleo.CongObjetos(True)
															
	def MayaCiclo(self):
		#Capturador de Eventos
		clock = pygame.time.Clock()
		while True:
			#clock.tick(40)
			evento = pygame.event.wait()
			self.MayCNucleo.MEventos(evento)			
			#Actualiza la Pantalla Completa
			pygame.display.update()	