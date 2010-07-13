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
from MayCJNivel import MayCJMNivel
from MayCLabel import MayCLabel
from MayCJGlobalesI import MayCJMGlobalesI
from MayCJGlobalesII import MayCJMGlobalesII

class MayCJMTablero():

	def __init__(self):
		#Inicializacion de los modulos de pygame
		pygame.init()
		self.run=True
		self.GlobalesI=MayCJMGlobalesI()
		self.GlobalesI.TableroCargar=self.Cargar	
		self.GlobalesII=MayCJMGlobalesII()
		self.Pantalla = pygame.display.set_mode(self.GlobalesI.Tamano_Pantalla)
		self.estadoX, self.estadoY=(0,0) 
		#Imagen del cursor
		self.seleccionador = self.CrearCursor() 
		self.ContaCoincide = 0
		self.ManejoxTeclado=False
		self.Mostrarseleccionador = False
		self.lblEstado=MayCLabel(self.Pantalla,'Estado:',1,(50,620),"Blanco")
		#self.NUECErrado As Boolean
		self.Cargar()
		self.Fondo=self.CFondo()
		self.MemoriaCiclo()

	def Cargar(self):
		self.REValores()
		self.Nivelf = MayCJMNivel(self.GlobalesI,self.GlobalesII)
		self.Fondo=self.CFondo()
		self.AsignaTarjetas()
		self.Imprimir()
		#Me.Panel2.Update()

	def REValores(self):
		self.estadoX = 0
		self.estadoY = 0
		#Guarda las Coordenadas de la primera carta seleccionada
		#para que no se vuelva a seleccionar por segunda vez
		self.CompEnter = (0,0)
		self.enEspera = False
		self.ContaCoincide = 0
		self.VeriVEsPR = False
		self.timermin = 0
		self.timerseg = 0
		self.ConEnter = 0
		self.lblEstado.Text('Estado:')
		
	def CrearCursor(self):
		seleccionador = pygame.image.load('./MayRecursos/cursor.png')
		seleccionador = pygame.transform.scale(seleccionador, (30, 30))
		return seleccionador
	
	def CFondo(self):
		ClaseImagen=self.GlobalesII.ClaseImagen
		
		if(ClaseImagen==1):
			Fondo = pygame.image.load('./MayRecursos/FDragones.jpg')
		elif(ClaseImagen==2):
			Fondo = pygame.image.load('./MayRecursos/FSimpson.jpg')
		elif(ClaseImagen==3):
			Fondo = pygame.image.load('./MayRecursos/FYugi.jpg')
		elif(ClaseImagen==4):
			Fondo = pygame.image.load('./MayRecursos/FCarros.jpg')
		Fondo = pygame.transform.scale(Fondo, self.GlobalesI.Tamano_Pantalla)	
		return Fondo		

	def AsignaTarjetas(self):
		try:
			a = self.Nivelf.entableroX
			b = self.Nivelf.entableroY
			conindex = 0
			coorx =0
			coory =0
			for y in range ((self.Nivelf.CoorY + 1 )):
				for x in range ((self.Nivelf.CoorX + 1 )):
					coorx = a + (self.Nivelf.PicTamX * x)
					coory = b + (self.Nivelf.PicTamY * y)

					#Los Indices indican la posicion en relacion a las lista a la que pertenece cada Tarjeta
					self.Nivelf.Tarjetas[y][x].CIndices((y,x))
					self.Nivelf.Tarjetas[y][x].BtnTarjeta.CCoordenadas((coorx, coory))
					self.Nivelf.Tarjetas[y][x].BtnTarjeta.CID(("Pic" + str(conindex)))
					self.Nivelf.Tarjetas[y][x].BtnTarjeta.CTamano((self.Nivelf.ObtPicTamX(),self.Nivelf.ObtPicTamY()))
					#Se pone la tarjeta boca abajo
					self.Nivelf.Tarjetas[y][x].RegresoVolteoTarjeta()
					a += 15
					conindex += 1
				
				a = self.Nivelf.ObtentableroX()
				b += 20
		except (NameError,ValueError):
			print ("Ocurrio un Error en AsignaTarjetas")

	def Tablero_Tiempo(self):
#		lbTiempot.Text = "" & timermin & ":" & timerseg
#		If (timerseg = 60) Then
#			timermin += 1
#			timerseg = 0
#		Else
#			timerseg += 1
#		End If
	#	self.Imprimir()
		#Proceso Con diferente Proposito que el anterior
		#Las tarjetas seleccionadas se quedan mostradas 2 segundos para que se puedan Apreciar
		if (self.GlobalesI.enEspera == False) :
			return
		#Se queda pausado el tiempo establecido por la Variable self.GlobalesI.TMPEVeri
		time.sleep(self.GlobalesI.TMPEVeri)
		py,px = self.GlobalesI.CoorSelecTar1
		self.Nivelf.VeriTarjetas(self.Nivelf.Tarjetas[py][px], self.Nivelf.Tarjetas[self.estadoY][self.estadoX],self.Nivelf,self.lblEstado)
		self.GlobalesI.enEspera = False
		if(self.ManejoxTeclado==True):
			self.Mostrarseleccionador = True
		self.Imprimir()

	def PresionTarjeta(self):
		if (self.GlobalesI.VeriVEsPR == True):
			return
		if (self.GlobalesI.ConEnter == 0):
			self.CompEnter = (self.estadoY,self.estadoX)
		elif (self.CompEnter == (self.estadoY,self.estadoX)):			
			return
		
		self.Nivelf.Tarjetas[self.estadoY][self.estadoX].VolteoTarjeta()
		#Si es ConEnter > 0 es porque se ha presionado 2 veces enter o space
		if (self.GlobalesI.ConEnter > 0):
			#Se pone enEspera =true para que se quede 2 seg la imagen mostrada					
			self.GlobalesI.enEspera = True
			self.GlobalesI.ConEnter = 0
			self.CompEnter = (0,0)
			if (self.ManejoxTeclado==True):
				self.Mostrarseleccionador = False			
		else:
			self.GlobalesI.CoorSelecTar1 = (self.estadoY,self.estadoX)
			self.GlobalesI.ConEnter += 1
								
	def Tablero_KeyDown(self,p_Evento):
		if self.GlobalesI.enEspera == True: 
			return

		if p_Evento.key ==pygame.K_LCTRL or p_Evento.key ==pygame.K_RCTRL:
			self.Mostrarseleccionador = False
			if (self.ManejoxTeclado==False):
				self.ManejoxTeclado=True
				self.Mostrarseleccionador = True
			else:
				self.ManejoxTeclado=False
				
		if (self.ManejoxTeclado==False):
			return
																
		if p_Evento.key ==pygame.K_KP_ENTER or p_Evento.key ==pygame.K_SPACE or p_Evento.key ==pygame.K_RETURN:
			self.PresionTarjeta()
							
		elif p_Evento.key ==pygame.K_UP:

			self.GlobalesI.VeriVEsPR = False
			#If (estadoY = 0) Then
			#	If (estadoX = 0) Then estadoX = Nivelf.pcoorX Else estadoX -= 1
			#	estadoY = Nivelf.pcoorY
			#Else
			#	estadoY -= 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil	
			self.estadoY, self.estadoX=self.NCoorde(self.estadoY, self.estadoX, 0, 0, self.Nivelf.CoorX, self.Nivelf.CoorY, "R")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True):  
				self.Tablero_KeyDown(p_Evento)
			
		elif p_Evento.key ==pygame.K_DOWN:
			
			self.GlobalesI.VeriVEsPR = False
			#If (estadoY = Nivelf.pcoorY) Then
			#	If (estadoX = Nivelf.pcoorX) Then estadoX = 0 Else estadoX += 1
			#	estadoY = 0
			#Else
			#	estadoY += 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil  
			self.estadoY, self.estadoX=self.NCoorde(self.estadoY, self.estadoX, self.Nivelf.CoorY, self.Nivelf.CoorX, 0, 0, "S")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True):
				self.Tablero_KeyDown(p_Evento)
			
		elif p_Evento.key ==pygame.K_RIGHT:
			
			self.GlobalesI.VeriVEsPR = False
			#If (estadoX = Nivelf.pcoorX) Then
			#	If (estadoY = Nivelf.pcoorY) Then estadoY = 0 Else estadoY += 1
			#	estadoX = 0
			#Else
			#	estadoX += 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil 
			self.estadoX, self.estadoY=self.NCoorde(self.estadoX, self.estadoY, self.Nivelf.CoorX, self.Nivelf.CoorY, 0, 0, "S")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True):
				self.Tablero_KeyDown(p_Evento)

		elif p_Evento.key ==pygame.K_LEFT:
									
			self.GlobalesI.VeriVEsPR = False
			#If (estadoX = 0) Then
			#	If (estadoY = 0) Then estadoY = Nivelf.pcoorY Else estadoY -= 1
			#	estadoX = Nivelf.pcoorX
			#Else
			#	estadoX -= 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil 
			self.estadoX, self.estadoY=self.NCoorde(self.estadoX, self.estadoY, 0, 0, self.Nivelf.CoorY, self.Nivelf.CoorX, "R")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True): 
				self.Tablero_KeyDown(p_Evento)
	
	def NCoorde(self,estadoA,estadoB,condiEstA,condiEstB,ValorESB, ValorESA,TOpe):
		if (estadoA == condiEstA):
			if (estadoB == condiEstB):  
				estadoB = ValorESB 
			else: 
				if(TOpe == "R"):
					estadoB = estadoB - 1
				else:
					estadoB = estadoB + 1
			estadoA = ValorESA
		else:
			if(TOpe == "R"):
				estadoA = estadoA - 1
			else:
				estadoA = estadoA + 1
		
		return estadoA,estadoB

	def Tablero_MovDRaton(self,p_Evento):
		if self.GlobalesI.enEspera == True or self.ManejoxTeclado==True: 
			return False

		for y in range ((self.Nivelf.CoorY + 1 )):
			for x in range ((self.Nivelf.CoorX + 1 )):
				if(self.Nivelf.Tarjetas[y][x].Estado == False and self.Nivelf.Tarjetas[y][x].MovimientoDRaton(p_Evento)):
					self.GlobalesI.VeriVEsPR = False
					self.estadoY, self.estadoX=self.Nivelf.Tarjetas[y][x].ObtIndices()
					
	def Tablero_PresDRaton(self,p_Evento):
		if self.GlobalesI.enEspera == True or self.ManejoxTeclado==True: 
			return 
		for y in range ((self.Nivelf.CoorY + 1 )):
			for x in range ((self.Nivelf.CoorX + 1 )):
				if(self.Nivelf.Tarjetas[y][x].Estado == False and self.Nivelf.Tarjetas[y][x].PresionDRaton(p_Evento)): 
					self.PresionTarjeta()

	
	def BusquedaTarjeta(self,p_Evento,p_indices=False):
		for y in range ((self.Nivelf.CoorY + 1 )):
			for x in range ((self.Nivelf.CoorX + 1 )):
				if(self.Nivelf.Tarjetas[y][x].Estado == False and self.Nivelf.Tarjetas[y][x].PresionDRaton(p_Evento)):
					if(p_indices==True):
						return (y,x) 
					else:	 
						return True
		if(p_indices==True):
			return False
		
	#El siguiente Procedimiento cálcula la locación del cursor en cada movimiento que se realice
	def cursor_NLoca(self):
		if(self.Mostrarseleccionador==False):
			return
		locpicX,locpicY = self.Nivelf.Tarjetas[self.estadoY][self.estadoX].BtnTarjeta.ObtCoordenadas()
		sizepicX,sizepicY = self.Nivelf.Tarjetas[self.estadoY][self.estadoX].BtnTarjeta.ObtTamano()
			

		#Por el momento el pic del cursor sera cuadrado cosa por la cual no importa si jalo el height o width del size
		#La MATEMATICA ES FACIL!!!!!!!!!!!!!!
		sizecur = self.seleccionador.get_height()

		nueva_locaX = ((sizepicX - sizecur) / 2) + locpicX
		nueva_locaY = ((sizepicY - sizecur) / 2) + locpicY

		self.Pantalla.blit(self.seleccionador,(nueva_locaX, nueva_locaY))
				
	def ImprTarjetas(self):
		try:
			for y in range ((self.Nivelf.CoorY + 1 )):
				for x in range ((self.Nivelf.CoorX + 1 )):
					if(self.Nivelf.Tarjetas[y][x].ObtEstado()==False):
						self.Nivelf.Tarjetas[y][x].Insertar(self.Pantalla)
		except (NameError,ValueError):
			print ("Ocurrio un Error en ImprTarjetas")		
									
	def Imprimir(self):
		#Insertar  Fondo
		self.Pantalla.blit(self.Fondo,(0,0))
		self.ImprTarjetas()
		#Insertar  Cursor
		self.cursor_NLoca()
		#Insertar Etiqueta de Estado
		self.lblEstado.Insertar()
		pygame.display.update()
			
	def MemoriaCiclo(self):
			clock = pygame.time.Clock()
			while self.run:
				clock.tick(20)
				#pygame.event.wait() hace que el while se quede dormido hasta que ocurra un evento
				evento=pygame.event.wait()
				if evento.type == pygame.QUIT:
					self.run = False
				if evento.type==pygame.MOUSEMOTION:	
					self.Tablero_MovDRaton(evento)
					self.Imprimir()
				if evento.type==pygame.MOUSEBUTTONDOWN:
					self.Tablero_PresDRaton(evento)
					self.Imprimir()
				if evento.type == pygame.KEYDOWN:
					self.Tablero_KeyDown(evento)																		
					self.Imprimir()			
				if(self.GlobalesI.enEspera==True):
					self.Tablero_Tiempo()
				
def main():
	MayCJMTablero()

if __name__ == '__main__':
	main()
