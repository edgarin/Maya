#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       MayCLabel.py
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

import pygame,random,time,codecs,sys
sys.path.append('./MayClases/MayJuegos')
import gui
from gui import *
import defaultStyle

sys.path.append('./MayClases/MayAPI')
from MayCLabel import MayCLabel
  
class MayCJAhorcado():   
            
        def __init__(self):
            pygame.init()
            self.Pantalla_Principal = pygame.display.set_mode((640,480))
            self.run=True
            defaultStyle.init(gui)
            self.desktop = gui.Desktop()
            self.buttonsalir = Button(position = (480,450),parent = self.desktop, text = "Salir")
            self.buttonsalir.onClick = self.buttonsalir_onClick
            self.Imagen = ""
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
            self.AhorcadoCiclo()         
        
        def GUI(self):
            self.lblIngresadas = MayCLabel(self.Pantalla_Principal, "Ingresadas: ","lblIngresadas",(25,25),"blanco")
            self.lblIngresadas.Insertar()
        
            self.lblIncorrectas = MayCLabel(self.Pantalla_Principal, "Letras Incorrectas: ","lblIncorrectas",(25,50),"blanco")
            self.lblIncorrectas.Insertar()

            self.lblEstado = MayCLabel(self.Pantalla_Principal, "Estado: ","lblEstado",(320,25),"blanco")
            self.lblEstado.Insertar()
        
            self.ImprimirImagen(self.ListaImagenes[0])
            
            #lblPregunta = Label(position=(250,95),size=(200,0),text=self.PreSecreta,parent=desktop)
            self.lblPregunta = MayCLabel(self.Pantalla_Principal,self.PreSecreta,"lblPregunta",(220,85),"rojo")
            self.lblPregunta.Insertar()
        
            self.lblCorrectas = MayCLabel(self.Pantalla_Principal,self.ReSecretaImpr(),"lblCorrectas",(250,325),"blanco")        
            self.lblCorrectas.Insertar()
        
            self.txtLetra = TextBox(position=(200,360),size=(200,0),text="",parent=self.desktop)            
                
            self.btn = Button(position = (240,400),parent = self.desktop, text = "Ok")
            self.btn.onClick = self.evt_click          
            #btn = Button("OK", action = self.evt_click)
                                
        def CargadoImagnes(self):
            imagen=None
            Lista=[]
            for a in range(9):
                imagen=pygame.image.load('./MayRecursos/MayJuegos/Ahorcado/'+str(a) + '.jpg')
                imagen= pygame.transform.scale(imagen, (200, 200))            
                Lista.append(imagen)
            return Lista

        def Llenado(self,condicion):
            if (condicion=='R'):
                url="./MayRecursos/MayJuegos/Ahorcado/Respuestas.txt"
            else:
                url="./MayRecursos/MayJuegos/Ahorcado/Preguntas.txt"
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

        def ComprobacionMB(self):    
            if self.CompLetra():
                LIngresada=self.txtLetra.text
            
                if LIngresada in self.ReSecreta:
                    self.LCorrectas += LIngresada
                    self.lblCorrectas.Text(self.ReSecretaImpr())

                    TodasEncontradasL=True
                
                    for i in range(len(self.ReSecreta)):
                        if self.ReSecreta[i] not in self.LCorrectas:
                            TodasEncontradasL = False
                            break
                    if TodasEncontradasL:
                        self.lblEstado.Append('Ha Ganado! La Respuesta Secreta era "' + self.ReSecreta + '"! Felicitaciones!')
                else:
                    self.LIncorrectas += LIngresada
                    self.lblIncorrectas.Text("Letras Incorrectas: " + self.LIncorrectas)
                    self.ImprimirImagen(self.ListaImagenes[len(self.LIncorrectas)])
            
                self.lblIngresadas.Text("Letras Ingresadas: "+self.LCorrectas+self.LIncorrectas)
    
        def LimpiarTxt(self):
            self.txtLetra.text=""

        def CompLetra(self):
            LetraIngre = self.txtLetra.text.lower()
            LeIngresadas=self.LCorrectas+self.LIncorrectas
            #self.lblEstado.text("Estado")
        
            if LetraIngre.strip() == '':
                self.NuevoEstado(' Debe Ingresar una Letra')
            elif len(LetraIngre) > 1:
                self.NuevoEstado(' Ingrese Solamente una Letra')
            elif LetraIngre in LeIngresadas:
                self.NuevoEstado(' Usted ya Ingresado esta letra')
            elif LetraIngre not in 'abcdefghijklmnopqrstuvwxyz':
                self.NuevoEstado(' Ingrese Letras Solamente')
            else:
                return True 

        def ComprobacionPierde(self):
            # Check if player has guessed too many times and lost
            if len(self.LIncorrectas) == 6:
                self.lblEstado.Text('Pisaste! XD')
                self.ImprimirImagen(self.ListaImagenes[6])
                time.sleep(1)
                self.ImprimirImagen(self.ListaImagenes[7])
                time.sleep(1)
                self.ImprimirImagen(self.ListaImagenes[8])

        def getRandomIndex(self,Lmax):
            # This function returns a random string from the passed list of strings.
            Index = random.randint(0, Lmax-1)
            return Index
    
        def buttonsalir_onClick(self,widget): #@NoSelf
            sys.exit()
        
        def ImprimirImagen(self, imagen):
            a = imagen
#            imagen = pygame.transform.scale(imagen, (200,200))
            self.Pantalla_Principal.blit(a,(200,120))
            pygame.display.update()
                        
        def NuevoEstado(self, Mensaje):
            self.lblEstado.Texto = "Estado: " + Mensaje
            self.lblEstado.Insertar()

        def AhorcadoCiclo(self):
            while self.run:
                for e in gui.setEvents(pygame.event.get()):
                    if e.type == pygame.QUIT:
                        self.run = False
                    if self.txtLetra.enter == True:
                        self.evt_click()                        
                    self.desktop.update()
                    self.desktop.draw()
                    pygame.display.update()
#MayCJAhorcado()
