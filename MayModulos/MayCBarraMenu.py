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
from MayCBoton import MayCBoton
from MayCSubBarraMenu import MayCSubBarraMenu
from MayCNucleo import MayCNucleo
from MayMColores import *

class MayCBarraMenu(object):
	def __init__(self,p_SubMenu = False,p_Tamano = (0,50),p_direccionico = None,p_Habilitado = True):
		self.Nucleo = MayCNucleo()
		#Propiedades
		#Interface en la cual la BarraMenu sera Insertada
		self.Interface_Padre = pygame.display.get_surface()
		wp,hp = self.Interface_Padre.get_size()
		w,h = p_Tamano
		
		if(w == 0):
			self.Tamano = (wp,h)
		else:
			self.Tamano = p_Tamano	

		self.Posicion_Actual = (0,0)
		self.Interface = pygame.Surface(self.Tamano,0,32)
		#self.Tipo=p_Tipo
		#Tipo de Objeto
		self.T_Objeto = 'BarraMenu'	
		#Indica si posee o  no un SubMenu la Barra de Menu
		self.SubMenu = p_SubMenu
		#Creacion Items Menu Bar
		self.Menus = []
		#Boton en Juego (Que esta Interactuando con los eventos =>MOUSEMOTION)
		self.Boton_NJuego = None
		#Variables de Eventos de Raton
		self.Raton_Dentro = False
		self.Raton_Fuera = True
		self.Raton_Click = False
		self.Habilitado = p_Habilitado
		self.Fondo = None
		self.Color = (BLANCO)
		#Tamano de Cada Menu
		self.TamanoxMenu = None
		self.EnFrente = False
		if(p_direccionico == None):
			self.Directorio_Imagenes = self.Nucleo.ObtDirRecursos()
		else:
			self.Directorio_Imagenes = p_direccionico
		#Manejado por el Nucleo
		self.MNucleo = True	
		self.Nucleo.Agregar(self)
	
	def CEnFrente(self, valor):
		self.EnFrente = valor
	def ObtEnFrente(self):
		return self.EnFrente
	
	def CMNucleo(self,valor):
		#Manejado por el Nucleo
		self.MNucleo = valor
	def ObtMNucleo(self):
		#Manejado por el Nucleo
		return self.MNucleo		
	def ObtInterface(self):
		return self.Interface
		
	def CColor(self,p_Color):
		self.Color = p_Color
		self.Fondo = None
		self.ReIniciar()
		
	def ObtColor(self):
		return self.Color

	def CFondo(self,p_Fondo):
		p_Fondo = pygame.transform.scale(p_Fondo,self.Tamano)
		self.Fondo = p_Fondo
		self.ReIniciar()
		
	def ObtFondo(self):
		return self.Fondo
			
	def Habilitar(self,p_Si_No):
		self.Habilitado = p_Si_No
	def ObtHabilitado(self):
		return self.Habilitado
	
	def ReIniciar(self,p_QM = False):
		if(self.Fondo == None):
			self.Interface.fill(self.Color)
		else:
			self.Interface.blit(self.Fondo,(0,0))
		
		for contador in range(len(self.Menus)):
			self.Menus[contador].Insertar()	
		
		if (p_QM == False):
			self.Raton_Click = False
			self.Nucleo.Imprimir()	
	
	def CPosicion(self,p_Posicion):
		self.Posicion_Actual = p_Posicion
		self.ReIniciar()
		
	def ObtPosicion(self):
		return self.Posicion_Actual

	def CTamano(self,p_Tamano):
		self.Interface = None
		self.Interface = pygame.Surface(p_Tamano,0,32)
		self.Tamano = p_Tamano		
			
	def ObtTamano(self):
		return self.Tamano		
	
	def CreacionMenus(self,p_IDs,p_Imagenes,p_Mensajes_Ayuda,p_Posicion = (0,0),p_Tamano = (20,10)):
		posx,posy = p_Posicion
		ancho,alto = p_Tamano
		self.TamanoxMenu = p_Tamano
		condicion = len(p_IDs)
		for contador in range(condicion):
			nombre = p_IDs[contador]
			Nombre_Imagen = p_Imagenes[contador]
			Mensaje = p_Mensajes_Ayuda[contador]
			
#			if (self.Tipo=='H'):
			Boton_de_Menu = MayCBoton(nombre,Nombre_Imagen,(posx+((ancho+10)*contador),posy),(ancho,alto),p_direccionico = self.Directorio_Imagenes)
#			elif (self.Tipo=='V'):
#				Boton_de_Menu=MayCBoton(nombre,Nombre_Imagen,(posx,posy+((alto+10)*contador)),(ancho,alto),p_direccionico=None,p_Barra=True)
			
			#Indico que la Interface Padre es la de la Barra de Menu	
			Boton_de_Menu.CInterfacePadre(self.Interface)	
			Boton_de_Menu.MensajeAyuda(Mensaje)
			#Agregar Boton a la Interface
			Boton_de_Menu.Insertar()
			self.Menus.append(Boton_de_Menu)		
	
	def CreacionSubBarraMenu(self,p_Ids_Botones,p_Imagenes_Botones,p_Mensajes_Botones):
			Lista = [p_Ids_Botones,p_Imagenes_Botones,p_Mensajes_Botones]
			a = 0
			b = 0
			#Comprueba si el Numero de los objetos en Listas en las Listas que se envian coincide=>Cada Objeto se Refiere a un Submenu
			while (a <= 2):
				b = a+1
				while(b <= 2):
					if(len(Lista[a]) != len(Lista[b])):
						print "Las Listas de la Creacion de SubBarraMenu deben de tener el mismo Numero de Listas"
						return
					b += 1
				a += 1	
			
			condicion = len(Lista[0]) - 1	
			a = 0
			n = 0
			b = 0 
			#Comprueba si el Numero de objetos en las Listas que se envian coinciden entre si
			while (a <= condicion):
				n = 0
				while(n <= condicion):
					b = a+1
					while(b <= condicion):
						if(len(Lista[a][n]) != len(Lista[b][n])):
							print "El numero de datos en las Sublistas de las Listas debe de Coincidir con los de su mismo Objeto"
							return
						b += 1					
					n += 1
				a += 1	
				
			for contador in range(len(self.Menus)):
				#Listas para el SubMenu a Crear
				L_IdsBotones = p_Ids_Botones[contador]
				L_Imagenes = p_Imagenes_Botones[contador]
				L_Mensajes = p_Mensajes_Botones[contador]	
													
				posx1,posy1 = self.Posicion_Actual
				w,h = self.Tamano
				#La posicion del Submenu sera la posicion en x del boton y la posicion en y
				#de la barra de menu q lo posea mas su alto 
				posx = self.Menus[contador].pos_x-10
				posy = posy1+h
		
				wbtn,hbtn = self.TamanoxMenu
				NoSubMenus = len(L_IdsBotones)
				#El Tamano de la Subarra sera 10*2(se dejan 10 de espacio al principio y al final) mas el ancho de los SubMenus  
				#mas 10(que es el espacio que se tienen entre si) por el numero de estos, y el alto sera el mismo que el de la BarraMenu
				wsubar = (10 * 2) + ((wbtn + 10) * NoSubMenus)
				hsubar = h
				SubBarraMenu = MayCSubBarraMenu((posx,posy),(wsubar,hsubar),p_direccionico = self.Directorio_Imagenes)
				self.Menus[contador].CreacionSubBarraMenu(SubBarraMenu,L_IdsBotones,L_Imagenes,L_Mensajes,self.TamanoxMenu)	
		
	def CColorSubBars(self,p_Color,p_Indice = -1):
		if(p_Indice >= 0):
			self.Menus[p_Indice].SubBarraMenu.CColor(p_Color)
			return
		
		for Menu in self.Menus:
			Menu.SubBarraMenu.CColor(p_Color)
		
	def ObtColorSubBars(self,p_Indice = -1):
		if(p_Indice >= 0):
			return self.Menus[p_Indice].SubBarraMenu.ObtColor()
		
		return self.Menu.SubBarraMenu.ObtColor()

	def CFondoSubBars(self,p_Fondo,p_Indice = -1):
		if(p_Indice >= 0):
			self.Menus[p_Indice].SubBarraMenu.CFondo(p_Fondo)
			return
		
		for Menu in self.Menus:
			Menu.SubBarraMenu.CFondo(p_Fondo)
		
	def ObtFondoSubBars(self,p_Indice = -1):
		if(p_Indice >= 0):
			return self.Menus[p_Indice].SubBarraMenu.ObtFondo()
		
		return self.Menu.SubBarraMenu.ObtFondo()
				
	def Insertar(self):
		self.Interface_Padre.blit(self.Interface,self.Posicion_Actual)					
		self.InsertarSubMenu()
		self.InsertarMensajesAyuda()
		
	def InsertarSubMenu(self):
		#Solo se Insertara el Submenu Cuando se haya dado click a la Barra de Menu
		#y Solo cuando sea un Boton que pertenezca a un Menu Superior 
		#ya que solo ellos pueden poseer SubMenu, sino se cumplen estas condiciones se sale del Metodo
		if(self.Boton_NJuego == None or self.Raton_Click == False or self.SubMenu == False):
			return

		#Se Imprime el SubMenu solo si se dio Click en un Boton que lo posea
		self.Boton_NJuego.SubBarraMenu.InsertarInterface()
	
	def InsertarMensajesAyuda(self):
		if(self.Raton_Dentro == True):
			self.AgregarMensaje()
		elif(self.Raton_Fuera == True):
			self.QuitarMensaje()

	def AgregarMensaje(self,p_posicion_mensaje = None):
		if (p_posicion_mensaje == None):
			#Agrego Mensaje tooltip
			self.Boton_NJuego.AgregarMensaje()		
		
	def QuitarMensaje(self):
		self.ReIniciar(p_QM = True)
										
	def MovimientoDRaton(self,p_Evento):
		if(self.VerificaEvento(p_Evento) == True):
			Boton=self.BusquedaBoton(p_Evento)
		
			if(self.Raton_Dentro == False and Boton != None):
				self.EntraRaton()
				self.Boton_NJuego.Pos_Mensaje = p_Evento.pos
				return True
			elif(self.Raton_Fuera == False and Boton == None):
				#Si el Raton estaba adentro se enviara true para 
				#que se reimprima sin los tooltips
				if (self.Raton_Dentro == True):
					self.SaleRaton()
					return True
				else:		
					return False
		else:
			#Prueba si se ha hecho este evento en la Subbarra de Menu
			if(self.SubMenu == True and self.Raton_Click == True):
				if(self.Boton_NJuego.SubBarraMenu.MovimientoDRaton(p_Evento)):
					return True				
	
	def EntraRaton(self):
		self.Raton_Dentro = True
		self.Raton_Fuera = False
				
	def SaleRaton(self):
		self.Raton_Fuera = True
		self.Raton_Dentro = False
								
	def PresionDRaton(self,p_Evento):
		if(self.VerificaEvento(p_Evento) == True):
			Boton=self.BusquedaBoton(p_Evento)
			if(Boton != None):
				self.EvtClick()
			else:
				self.ReIniciar()
			return True	
		else:
			#Prueba si se ha hecho este evento en la Subbarra de Menu
			if(self.SubMenu == True and self.Raton_Click == True):
				if (self.Boton_NJuego.SubBarraMenu.PresionDRaton(p_Evento)):
					self.ReIniciar()
					return True
			self.ReIniciar()
	
	def EvtClick(self):
		#Cuando el Boton es presionado dos veces Raton_Click sera falso y ya no se imprimira el submenu del Boton presionado
		if(self.Raton_Click == False):
			self.Raton_Click = True
			if (self.SubMenu == False):
				self.Boton_NJuego.Click()
		else:	
			self.Raton_Click = False
											
	#Busca si se concentra un Posible evento en la Interface
	def VerificaEvento(self,p_evento):
		pos_x2,pos_y2 = p_evento.pos
		
		pos_x,pos_y = self.ObtPosicion()
		Ancho,Alto = self.ObtTamano()
	
		if ((pos_x2 >= pos_x and pos_x2 <= (pos_x + Ancho)) and (pos_y2 >= pos_y and pos_y2 <= (pos_y + Alto))):
			return True
		else:
			return False

	def BusquedaBoton(self,evento):
		for contador in range(len(self.Menus)):
			if (self.Menus[contador].Busqueda(evento.pos,p_posInterPadre = self.Posicion_Actual)):
				#Boton en Juego
				self.Boton_NJuego = self.Menus[contador]
				return self.Menus[contador]			