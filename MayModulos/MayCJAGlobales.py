import sys
sys.path.append('./MayModulos')
sys.path.append('./MayModulos/MayAPI')
import pygame,codecs
import os.path
import GlobalesI
from MayCImagen import MayCImagen
class MayCJAGlobales():
	def __init__(self):
		#Modulo de variables y metodos Globales
		#Ubicacion Recursos
		self.Dir_Recursos = './MayRecursos/MayJuegos/Ahorcado/'
		###################################Parametros Pantalla###############################################
		#Fondo y Color de la Pantalla
		self.Col_Pantalla = (0,0,0)
		self.Fon_Pantalla = 'Fon_Ahorcado.jpg'
		###################################Parametros Para las Imagenes######################################
		#Tamano_Imagenes Ahorcado
		self.Tam_Img = (200, 200)
		self.Pos_Img = (200,120)
		#Imagenes a Utilizar (Para el Ahorcado)
		self.Lista_Img = self.CargadoImg()
		print len(self.Lista_Img)
		##################################Parametros Archivos de Texto#######################################
		self.Archivo_Preg = 'Preguntas.txt'
		self.Archivo_Resp = 'Respuestas.txt'
		self.Lista_Resp = self.Llenado('R')
		self.Lista_Preg = self.Llenado('P')

	##################################Metodos y Funciones################################################
	def ObtLPreg(self):
		return self.Lista_Preg
	def ObtLResp(self):
		return self.Lista_Resp
	def ObtLImgs(self):
		return self.Lista_Img
	def ObtDRecu(self):
		return self.Dir_Recursos	
	
	def CargadoImg(self):
		imagen = None
		Lista_Img = []
		for a in range(9):
			imagen = pygame.image.load(os.path.join(self.Dir_Recursos , (str(a) + '.jpg')))
			imagen = pygame.transform.scale(imagen,self.Tam_Img) 
			Lista_Img.append(imagen)
		return Lista_Img 

	def Llenado(self,condicion):
		if (condicion == 'R'):
			url = self.Dir_Recursos + self.Archivo_Resp
		else:
			url = self.Dir_Recursos + self.Archivo_Preg
		Lista = []
		# Primero abrimos el archivo en modo lectura (r)
		archivo = codecs.open(url,encoding = 'utf-8',mode = "r")
		# leemos el archivo, colocamos el contenido en una lista
		for linea in archivo.readlines():
			Lista.append(linea.strip())		
		# Ahora lo cerramos(El Archivo)
		archivo.close()
		#Se Retorna la Lista 
		return Lista