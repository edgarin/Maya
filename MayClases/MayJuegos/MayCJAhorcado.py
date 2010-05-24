# encoding: utf-8
from albow.fields import TextField, FloatField
import random,time,pygame
from pygame.locals import *
import codecs 
import 
pygame.init()

#--------------------------------------------------------------------------------
#
#    Text Field
#
#--------------------------------------------------------------------------------

class CamposTexto():

	def __init__(self, p_Superficie,p_Coordenadas):
		
		#Respuestas
		self.ListaRespuesta=self.Llenado('R')
		#Preguntas
		self.ListaPregunta=self.Llenado('P')
		#Imagenes
		self.ListaImagenes=self.CargadoImagnes()
		
		Indice=self.getRandomIndex(len(self.ListaRespuesta))
		#Respuesta Secreta
		self.ReSecreta=self.ListaRespuesta[Indice]
		#Pregunta Secreta
		self.PreSecreta=self.ListaPregunta[Indice]
		#Letras Correctas
		self.LCorrectas=""
		#Letras Incorrectas
		self.LIncorrectas=""		
		self.GUI()
		
	def GUI(self):
		
		lblIngresadas = Label("Letras Ingresadas: ")
		lblIngresadas.rect.width = 400
		lblIngresadas.rect.topleft = (20, 20)
		self.lblIngresadas = lblIngresadas
		self.add(lblIngresadas)
		
		lblIncorrectas = Label("Letras Incorrectas: ")
		lblIncorrectas.rect.width = 400
		lblIncorrectas.rect.topleft = (20, 45)
		self.lblIncorrectas = lblIncorrectas
		self.add(lblIncorrectas)
		
		lblEstado = Label("Estado Juego: ")
		lblEstado.rect.width = 400
		lblEstado.rect.topleft = (400, 20)
		self.lblEstado = lblEstado
		self.add(lblEstado)
		
		Imagen=Image(self.ListaImagenes[0])
		Imagen.rect.topleft=(200, 100)
		self.Imagen=Imagen
		self.add(self.Imagen)
			
		lblPregunta = Label(self.PreSecreta)
		lblPregunta.rect.width = 400
		lblPregunta.rect.topleft = (200, 325)
		self.lblPregunta = lblPregunta
		self.add(lblPregunta)
		
		lblCorrectas = Label(self.ReSecretaImpr())
		lblCorrectas.rect.width = 400
		lblCorrectas.rect.topleft = (200, 370)
		self.lblCorrectas = lblCorrectas
		self.add(lblCorrectas)
		
		self.txtLetra = self.add_field("Letra:",200, 400)
		self.add(self.txtLetra)
			
		btn = Button("OK", action = self.evt_click)
		btn.rect.midtop = (320, 425)
		self.add(btn)
		
		btn = Button("Menu", action = self.go_back)
		btn.rect.midtop = (40, 455)
		self.add(btn)
		
		self.txtLetra.focus()
	
	def add_field(self, label,posx ,posy):
		lbl = Label(label)
		lbl.rect.topleft = (posx, posy)
		self.add(lbl)
		fld = TextField(150)
		fld.rect.topleft = (250, posy)
		fld.enter_action = self.evt_click
		return fld
		
	def CargadoImagnes(self):
		imagen=None
		Lista=[]
		for a in range(9):
			imagen=pygame.image.load(str(a) + '.jpg')
			imagen= pygame.transform.scale(imagen, (200, 200))            
			Lista.append(imagen)
		#Se hace manual porque la última imagen es .gif    
		#~ imagen=pygame.image.load('6.gif')
		#~ imagen= pygame.transform.scale(imagen, (200, 200))            
		#~ Lista.append(imagen)
		#~ print len(Lista)
		return Lista    
                   
	def Llenado(self,condicion):
		if (condicion=='R'):
			url="Respuestas.txt"
		else:
			url="Preguntas.txt"
		
		Lista=[]
        # Primero abrimos el archivo en modo lectura (r)
		archivo = codecs.open(url,encoding='utf-8',mode="r")
        # leemos el archivo, colocamos el contenido en una lista
		for linea in archivo.readlines():
			Lista.append(linea.strip())        
		# Ahora lo cerramos(El Archivo)
		archivo.close()
		#Se Retorna la Lista 
		return Lista
		
	def ReSecretaImpr(self):
		EnBlanco = '_' * len(self.ReSecreta)

		# Reemplaza espacios en blanco con las letras correctas
		for i in range(len(self.ReSecreta)): 
			if self.ReSecreta[i] in self.LCorrectas:
				#EnBlanco[:i]=Todos hasta i,, EnBlanco[i+1:]=Todos los siguientes menos i+1
				EnBlanco = EnBlanco[:i] + self.ReSecreta[i] + EnBlanco[i+1:]

		PalabraFinal=''
		
		for Letra in EnBlanco: # show the secret word with spaces in between each letter
			PalabraFinal+= Letra + ' '
		
		return PalabraFinal	
        
	def evt_click(self):
		self.ComprobacionMB()	
		self.ComprobacionPierde()
		self.LimpiarTxt()
		#self.MessageBox("Titulo","Como estas")
		
	def ComprobacionMB(self):	
		if self.CompLetra():
			LIngresada=self.txtLetra.text
			
			if LIngresada in self.ReSecreta:
				self.LCorrectas += LIngresada
				self.lblCorrectas.text=self.ReSecretaImpr()
				
				TodasEncontradasL=True
				
				for i in range(len(self.ReSecreta)):
					if self.ReSecreta[i] not in self.LCorrectas:
						TodasEncontradasL = False
						break
				if TodasEncontradasL:
					self.lblEstado.text+='Ha Ganado! La Respuesta Secreta era "' + self.ReSecreta + '"! Felicitaciones!'
			else:
				self.LIncorrectas += LIngresada
				self.lblIncorrectas.text="Letras Incorrectas: " + self.LIncorrectas
				self.Imagen.image=self.ListaImagenes[len(self.LIncorrectas)]
			
			self.lblIngresadas.text="Letras Ingresadas: "+self.LCorrectas+self.LIncorrectas
				
	def LimpiarTxt(self):
		self.txtLetra.text=""
		self.txtLetra.focus()
			
	def CompLetra(self):
		LetraIngre = self.txtLetra.text.lower()
		LeIngresadas=self.LCorrectas+self.LIncorrectas
		self.lblEstado.text="Estado:"
		
		if LetraIngre.strip() == '':
			self.lblEstado.text+=' Debe Ingresar una Letra'
		elif len(LetraIngre) > 1:
			self.lblEstado.text+=' Ingrese Solamente una Letra'
		elif LetraIngre in LeIngresadas:
			self.lblEstado.text+=' Usted ya Ingresado esta letra'
		elif LetraIngre not in 'abcdefghijklmnopqrstuvwxyz':
			self.lblEstado.text+=' Ingrese Letras Solamente'
		else:
			return True 
			
	def ComprobacionPierde(self):
		# Check if player has guessed too many times and lost
		if len(self.LIncorrectas) == 6:
			self.lblEstado.text+='Pisaste! XD'
			self.Imagen.image=self.ListaImagenes[6]
			time.sleep(1)
			self.Imagen.image=self.ListaImagenes[7]
			time.sleep(1)
			self.Imagen.image=self.ListaImagenes[8]
																								           
	def getRandomIndex(self,Lmax):
		# This function returns a random string from the passed list of strings.
		Index = random.randint(0, Lmax-1)
		return Index
	
	def MessageBox(self,title, message):
		try:
			import os
			import pygame, pygame.font
			
			pygame.quit() #clean out anything running
			pygame.display.init()
			pygame.font.init()
			screen = pygame.display.set_mode((460, 140))
			pygame.display.set_caption(title)
			font = pygame.font.Font(None, 18)
			foreg = 0, 0, 0
			backg = 200, 200, 200
			liteg = 255, 255, 255
			ok = font.render('Ok', 1, foreg)
			screen.fill(backg)
			okbox = ok.get_rect().inflate(20, 10)
			okbox.centerx = screen.get_rect().centerx
			okbox.bottom = screen.get_rect().bottom - 10
			screen.fill(liteg, okbox)
			screen.blit(ok, okbox.inflate(-20, -10))
			pos = [20, 20]
			for text in message.split('\n'):
				msg = font.render(text, 1, foreg)
				screen.blit(msg, pos)
				pos[1] += font.get_height()
			
			pygame.display.flip()
			while 1:
				e = pygame.event.wait()
				if e.type == QUIT or e.type == MOUSEBUTTONDOWN or \
						   (e.type == KEYDOWN and e.key in (K_ESCAPE, K_SPACE, K_RETURN)):
					break
			pygame.quit()
		except pygame.error:
			raise ImportError	
	
	def go_back(self):
		self.parent.show_menu()
		#self.parent.create_demo_screens()
