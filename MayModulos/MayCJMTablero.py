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
from MayCNucleo import MayCNucleo
from MayCJMNivel import MayCJMNivel
from MayCLabel import MayCLabel
from MayCJMGlobalesI import MayCJMGlobalesI
from MayCJMGlobalesII import MayCJMGlobalesII
from MayCBoton import MayCBoton
from MayCImagen import MayCImagen
from MayCReloj import MayCReloj
class MayCJMTablero():

	def __init__(self):
		self.run=True
		self.Pantalla = pygame.display.get_surface()
		self.MayCNucleo = MayCNucleo()
		self.MayCNucleo.CDirRecursos('./MayRecursos/MayJuegos/Memoria/')
		self.MayCNucleo.NKeyDown = self.Tablero_KeyDown
		self.MayCNucleo.NMBUTTONDOWN = self.Tablero_PresDRaton
		self.MayCNucleo.NMOUSEMOTION = self.Tablero_MovDRaton
		self.GlobalesI = MayCJMGlobalesI()
		self.GlobalesI.TableroCargar = self.Cargar	
		self.GlobalesII = MayCJMGlobalesII()
		self.NivelEmpiezo = self.GlobalesI.nivel_actual
		self.Fondo = self.CFondo()
		self.MayCNucleo.Fondo = self.Fondo
		self.estadoX, self.estadoY = (0,0) 
		#Imagen del cursor
		self.seleccionador = MayCImagen('ImgSelec','cursor.png',p_Coordenadas = (0,0),p_Tamano = self.GlobalesI.TamanoCursor) 
		#Habilitar(False) lo vuelve invisible
		self.seleccionador.Habilitar(False)
		self.seleccionador.CEnFrente(True)
		self.ManejoxTeclado = False
		self.lblEstado = MayCLabel('Estado:',1,(50,620),"Blanco")
		
		self.lblTiempo = MayCLabel('Tiempo = 00:00',"lblTiempo",(540,620),"blanco")			
		self.Reloj = MayCReloj(tick = 1, metodo = self.Tick)
		
		self.PregJugar = False	
		self.Cargar()
		self.MemoriaCiclo()

	def Cargar(self,volvjuagar = False):
		if(volvjuagar == True):
			self.lblEstado.Habilitar(False)
			self.seleccionador.Habilitar(False)
			self.lblTiempo.Habilitar(False)
			self.PregJugar = True
			self.Reloj.Terminar()
			self.Imprimir()
			respuesta = self.MayCNucleo.Msj('Desea Volver a Jugar?',p_Tipo = 1)
			
			if (respuesta == 1):
				self.VolveraJugar()
			else:
				self.Salir()
				
			return
		
		self.REValores()
		self.Nivelf = MayCJMNivel(self.GlobalesI,self.GlobalesII)
		self.AsignaTarjetas()
		self.Imprimir()
		if(self.NivelEmpiezo == self.GlobalesI.nivel_actual):
			self.Reloj.Comenzar()

	def REValores(self):
		self.estadoX, self.estadoY = (0,0)
		#Guarda las Coordenadas de la primera carta seleccionada
		#para que no se vuelva a seleccionar por segunda vez
		self.CompEnter = (0,0)
		self.GlobalesI.enEspera = False
		self.GlobalesI.VeriVEsPR = False
		self.GlobalesI.ConEnter = 0
		self.lblEstado.Text('Estado:')
		if(self.NivelEmpiezo == self.GlobalesI.nivel_actual):
			self.seg = 0
			self.min = 0
	
	def CFondo(self):
		ClaseImagen = self.GlobalesII.ClaseImagen
		TamanoF = self.Pantalla.get_size()
		NombreImg = ''
		
		if(ClaseImagen == 1):
			NombreImg = 'FDragones.jpg'
		elif(ClaseImagen == 2):
			NombreImg = 'FSimpson.jpg'
		elif(ClaseImagen == 3):
			NombreImg = 'FYugi.jpg'
		elif(ClaseImagen == 4):
			NombreImg = 'FCarros.jpg'
			
		Fondo = MayCImagen("FondoM",NombreImg,p_Coordenadas = (0,0),p_Tamano = TamanoF)	
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

	def Tick(self):
		if (self.seg == 60):
			self.seg = 0
			self.min += 1
			
		self.seg += 1
			
		seg = ''
		min = ''
			
		if(len(str (self.seg)) == 1):
			seg = '0' + str(self.seg)
		else:		 
			seg = str(self.seg)
			
		if(len(str (self.min)) == 1):
			min = '0' + str(self.min)
		else:		 
			min = str(self.min)
					
		self.lblTiempo.Text('Tiempo = ' + min + ':' + seg)
		pygame.display.update()
			
	def Tablero_Tiempo(self):
		GI = self.GlobalesI
		
		#Se queda pausado el tiempo establecido por la Variable self.GlobalesI.TMPEVeri
		time.sleep(GI.TMPEVeri)
		py,px = GI.CoorSelecTar1
		self.Nivelf.VeriTarjetas(self.Nivelf.Tarjetas[py][px], self.Nivelf.Tarjetas[self.estadoY][self.estadoX],self.Nivelf,self.lblEstado)
		GI.enEspera = False
		if(self.ManejoxTeclado == True):
			self.seleccionador.Habilitar(True)
		self.Imprimir()	

	def PresionTarjeta(self):
		GI = self.GlobalesI
		
		if (GI.VeriVEsPR == True):
			return
		if (GI.ConEnter == 0):
			self.CompEnter = (self.estadoY,self.estadoX)
		elif (self.CompEnter == (self.estadoY,self.estadoX)):			
			return
		
		self.Nivelf.Tarjetas[self.estadoY][self.estadoX].VolteoTarjeta()
		#Si es ConEnter > 0 es porque se ha presionado 2 veces enter o space
		if (GI.ConEnter > 0):
			#Se pone enEspera =true para que se quede 2 seg la imagen mostrada					
			GI.enEspera = True
			GI.ConEnter = 0
			self.CompEnter = (0,0)
			if (self.ManejoxTeclado == True):
				self.seleccionador.Habilitar(False)
			self.Imprimir()	
			self.Tablero_Tiempo()				
		else:
			GI.CoorSelecTar1 = (self.estadoY,self.estadoX)
			GI.ConEnter += 1
			self.Imprimir()
								
	def Tablero_KeyDown(self,p_Evento):
		
		GI = self.GlobalesI
		if p_Evento.key == pygame.K_LCTRL or p_Evento.key == pygame.K_RCTRL:
			self.seleccionador.Habilitar(False)
			if (self.ManejoxTeclado == False):
				self.ManejoxTeclado = True
				self.seleccionador.Habilitar(True)
			else:
				self.ManejoxTeclado = False
			
			self.Imprimir()
				
		if (self.ManejoxTeclado == False):
			return
																
		if p_Evento.key == pygame.K_KP_ENTER or p_Evento.key == pygame.K_SPACE or p_Evento.key == pygame.K_RETURN:
			self.PresionTarjeta()
							
		elif p_Evento.key == pygame.K_UP:

			GI.VeriVEsPR = False
			#If (estadoY = 0) Then
			#	If (estadoX = 0) Then estadoX = Nivelf.pcoorX Else estadoX -= 1
			#	estadoY = Nivelf.pcoorY
			#Else
			#	estadoY -= 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil	
			self.estadoY, self.estadoX = self.NCoorde(self.estadoY, self.estadoX, 0, 0, self.Nivelf.CoorX, self.Nivelf.CoorY, "R")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True):  
				self.Tablero_KeyDown(p_Evento)
			self.Imprimir()
			
		elif p_Evento.key == pygame.K_DOWN:
			
			GI.VeriVEsPR = False
			#If (estadoY = Nivelf.pcoorY) Then
			#	If (estadoX = Nivelf.pcoorX) Then estadoX = 0 Else estadoX += 1
			#	estadoY = 0
			#Else
			#	estadoY += 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil  
			self.estadoY, self.estadoX = self.NCoorde(self.estadoY, self.estadoX, self.Nivelf.CoorY, self.Nivelf.CoorX, 0, 0, "S")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True):
				self.Tablero_KeyDown(p_Evento)
			self.Imprimir()
			
		elif p_Evento.key == pygame.K_RIGHT:
			
			GI.VeriVEsPR = False
			#If (estadoX = Nivelf.pcoorX) Then
			#	If (estadoY = Nivelf.pcoorY) Then estadoY = 0 Else estadoY += 1
			#	estadoX = 0
			#Else
			#	estadoX += 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil 
			self.estadoX, self.estadoY = self.NCoorde(self.estadoX, self.estadoY, self.Nivelf.CoorX, self.Nivelf.CoorY, 0, 0, "S")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True):
				self.Tablero_KeyDown(p_Evento)
			self.Imprimir()	
			
		elif p_Evento.key == pygame.K_LEFT:
									
			GI.VeriVEsPR = False
			#If (estadoX = 0) Then
			#	If (estadoY = 0) Then estadoY = Nivelf.pcoorY Else estadoY -= 1
			#	estadoX = Nivelf.pcoorX
			#Else
			#	estadoX -= 1
			#End If
			#El Call siguiente hace lo mismo que el codigo comentado anterior, lo hice asi para ahorra líneas
			#Dejo el comentario de codigo debido a que el método esta algo complejo de entender a la primera
			#Nada del Otro mundo, Fácil 
			self.estadoX, self.estadoY = self.NCoorde(self.estadoX, self.estadoY, 0, 0, self.Nivelf.CoorY, self.Nivelf.CoorX, "R")
			if (self.Nivelf.Tarjetas[self.estadoY][self.estadoX].Estado == True): 
				self.Tablero_KeyDown(p_Evento)
			self.Imprimir()	
			
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
		GI = self.GlobalesI
				
		if GI.enEspera == True or self.ManejoxTeclado == True: 
			return False
		
		for y in range ((self.Nivelf.CoorY + 1 )):
			for x in range ((self.Nivelf.CoorX + 1 )):
				if(self.Nivelf.Tarjetas[y][x].Estado == False and self.Nivelf.Tarjetas[y][x].MovimientoDRaton(p_Evento)):
					GI.VeriVEsPR = False
					return
	
	def Salir(self):
		self.MayCNucleo.RemObjetos()
		self.run = False
								
	def Tablero_PresDRaton(self,p_Evento):
		if self.GlobalesI.enEspera == True or self.ManejoxTeclado == True: 
			return 
		for y in range ((self.Nivelf.CoorY + 1 )):
			for x in range ((self.Nivelf.CoorX + 1 )):
				if(self.Nivelf.Tarjetas[y][x].Estado == False and self.Nivelf.Tarjetas[y][x].PresionDRaton(p_Evento)): 
					self.estadoY, self.estadoX = self.Nivelf.Tarjetas[y][x].ObtIndices()
					self.PresionTarjeta()
					return
						
	def VolveraJugar(self):
		self.PregJugar = False
		if (self.ManejoxTeclado == True):
			self.seleccionador.Habilitar(True)
		self.lblEstado.Habilitar(True)
		self.lblTiempo.Text('Tiempo = 00:00')
		self.lblTiempo.Habilitar(True)
		self.GlobalesI.nivel_actual = 1
		self.Cargar()
		
	#El siguiente Procedimiento cálcula la locación del cursor en cada movimiento que se realice
	def cursor_NLoca(self):
		if(self.seleccionador.ObtHabilitado() == False or self.PregJugar == True):
			return
		locpicX,locpicY = self.Nivelf.Tarjetas[self.estadoY][self.estadoX].BtnTarjeta.ObtCoordenadas()
		sizepicX,sizepicY = self.Nivelf.Tarjetas[self.estadoY][self.estadoX].BtnTarjeta.ObtTamano()
			

		#Por el momento el pic del cursor sera cuadrado cosa por la cual no importa si jalo el height o width del size
		#La MATEMATICA ES FACIL!!!!!!!!!!!!!!
		sizecur = self.seleccionador.ObtInterface().get_height()

		nueva_locaX = ((sizepicX - sizecur) / 2) + locpicX
		nueva_locaY = ((sizepicY - sizecur) / 2) + locpicY

		self.seleccionador.CCoordenadas((nueva_locaX, nueva_locaY))
														
	def Imprimir(self):
		#Insertar  Cursor
		self.cursor_NLoca()
		self.MayCNucleo.Imprimir()
		pygame.display.update()
			
	def MemoriaCiclo(self):
			while self.run:
				evento = pygame.event.wait()
				if evento.type == pygame.QUIT:
					self.Salir()
					continue
				self.MayCNucleo.MEventos(evento)
				pygame.display.update()		