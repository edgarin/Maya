#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
#       MayCLabel.py
#       
#       Copyleft 2010 InformÃ¡tica al Alcance de Todos (CA)
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
import pygame,random,time
import gui
import defaultStyle
from MayCJAGlobales import MayCJAGlobales
from gui import *
from MayCLabel import MayCLabel
from MayCBoton import MayCBoton
from MayCImagen import MayCImagen
from MayCReloj import MayCReloj
from MayCNucleo import MayCNucleo

class MayCJAhorcado():   
            
        def __init__(self):
            self.run = True
            self.Pantalla_Principal = pygame.display.get_surface()
            self.MayCJAGlobales = MayCJAGlobales()
            self.MayCNucleo = MayCNucleo()
            self.MayCNucleo.CDirRecursos(self.MayCJAGlobales.ObtDRecu())
            defaultStyle.init(gui)
            self.desktop = gui.Desktop()
            self.MayCNucleo.CSPGDesk(self.desktop)
            #Indices Jugados
            self.IndJ = []
            self.CargarDatos()     
            self.GUI()
            self.Reloj.Comenzar()
            self.AhorcadoCiclo()         
        
        def CargarDatos(self):
            MG = self.MayCJAGlobales
            self.Imagen = ""
            #Respuestas
            self.ListaRespuesta = MG.ObtLResp()
            #Preguntas
            self.ListaPregunta = MG.ObtLPreg()
            #Imagenes
            self.ListaImagenes = MG.ObtLImgs()
            #Numero aleatorio que se genera para seleccionar
            #la pregunta y la respuesta
            Indice = self.getRandomIndex(len(self.ListaRespuesta))
            #Respuesta Secreta
            self.ReSecreta = self.ListaRespuesta[Indice]
            #Pregunta Secreta
            self.Pregunta = self.ListaPregunta[Indice]
            #Respuesta Sin Espacios
            self.ReSinEspacios = self.ResSinEspacios()
            #Letras Correctas
            self.LCorrectas = ""
            #Letras Incorrectas
            self.LIncorrectas = ""
            self.seg = 0
            self.min = 0
            self.PregJugar = False
            
        def GUI(self):
            MG = self.MayCJAGlobales
            MCN = self.MayCNucleo
            self.Fondo = MayCImagen('AFondo',MG.Fon_Pantalla,p_Coordenadas = (0,0),p_Tamano = self.Pantalla_Principal.get_size())
            self.Fondo.Insertar()
            MCN.CFondo(self.Fondo)
            
            self.lblIngresadas = MayCLabel("Ingresadas: ","lblIngresadas",(25,25),"blanco")
            self.lblIngresadas.Insertar()
        
            self.lblIncorrectas = MayCLabel( "Letras Incorrectas: ","lblIncorrectas",(25,50),"blanco")
            self.lblIncorrectas.Insertar()

            self.lblEstado = MayCLabel("Estado: ","lblEstado",(320,25),"blanco")
            self.lblEstado.Insertar()
        
            self.ImgAhorcado = MayCImagen('ImgAhorcado',None,p_Coordenadas = MG.Pos_Img, p_Tamano = MG.Tam_Img)
            self.ImgAhorcado.Centrar("X")
            self.ImgAhorcado.CInterface(p_img = self.ListaImagenes[0])
            self.ImgAhorcado.Insertar()

            self.lblPregunta = MayCLabel(self.Pregunta,"lblPregunta",(100,85),"rojo")
            self.lblPregunta.Centrar("X")
            self.lblPregunta.Insertar()
        
            self.lblRespuesta = MayCLabel(self.ReSecretaImpr(),"lblRespuesta",(50,325),"blanco")    
            self.lblRespuesta.Centrar("X")    
            self.lblRespuesta.Insertar()
            
            self.lblTiempo = MayCLabel('Tiempo = 00:00',"lblTiempo",(320,50),"blanco")        
            self.lblTiempo.Insertar()
            
            self.Reloj = MayCReloj(tick = 1, metodo = self.Tick)
            #Volver a Jugar
            self.lblVJugar = MayCLabel(' ','lblM',(250,220),"Blanco")
            self.lblVJugar.Habilitar(False)
            self.btnSi = MayCBoton('btnSi','Si.png',p_Coordenadas = (280,250),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
            self.btnSi.MensajeAyuda("Volver a Jugar")
            self.btnSi.Habilitar(False)
            self.btnSi.evtclick = self.VolveraJugar
            self.btnNo = MayCBoton('btnNo','No.png',p_Coordenadas = (330,250),p_Tamano = (30,30),p_direccionico = './MayRecursos/MayIconos')
            self.btnNo.MensajeAyuda("Salir del Juego")
            self.btnNo.Habilitar(False)
            self.btnNo.evtclick = self.IrMenu
            
            self.btn = Button(position = MCN.ObtPosicion((240,400)),parent = self.desktop, text = "Ok")
            self.btn.onClick = self.evt_click
            
            self.buttonsalir = Button(position = MCN.ObtPosicion((480,450)),parent = self.desktop, text = "Menú Principal")
            self.buttonsalir.onClick = self.buttonsalir_onClick                      

            self.txtLetra = TextBox(position = MCN.ObtPosicion((200,360)),size = (200,0),text = "",parent = self.desktop)            
        
        def ResSinEspacios(self):
            SinEspacios = ''
            # Arma la Respuesta sin Espacios
            for Letra in self.ReSecreta:
                if(Letra != ' '):
                    SinEspacios += Letra
                                                        
            return SinEspacios
        
        def ReSecretaImpr(self):
            EnBlanco = '_' * len(self.ReSecreta)

            # Reemplaza espacios en blanco con las letras correctas
            for i in range(len(self.ReSecreta)): 
                if self.ReSecreta[i].lower() in self.LCorrectas:
                    #EnBlanco[:i]=Todos hasta i, EnBlanco[i+1:]=Todos los siguientes comenzando desde i+1
                    EnBlanco = EnBlanco[:i] + self.ReSecreta[i] + EnBlanco[i+1:]

            PalabraFinal = ''
            
            a = 0
            for Letra in EnBlanco: # show the secret word with spaces in between each letter
                #Se Buscan los Espacios para dejarlos en la palabra del label
                if (self.ReSecreta[a] == ' '):
                    PalabraFinal += '  '
                else:    
                    PalabraFinal += Letra + ' '
                a +=1             
                
            return PalabraFinal    
        
        def evt_click(self,widget):
            self.evtVerificar()

        def buttonsalir_onClick(self,widget): 
            self.IrMenu()
        
        def IrMenu(self):
            self.MayCNucleo.RemObjetos()
            self.run = False    
            
        def evtVerificar(self):
            self.ComprobacionMB()    
            self.ComprobacionPierde()
            self.Imprimir()
            
        def LimpiarTxt(self):
            self.txtLetra.text=""
        
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
                       
        def ComprobacionMB(self):
            if self.CompLetra():
                LIngresada = self.txtLetra.text
                LIngresada = LIngresada.lower()

                if LIngresada in self.ReSinEspacios.lower():
                    self.LCorrectas += LIngresada
                    self.lblRespuesta.Text(self.ReSecretaImpr())
                    self.lblEstado.Text ("Estado: Letra Correcta :)")
                    
                    TodasEncontradasL=True
                
                    for i in range(len(self.ReSinEspacios)):
                        if self.ReSinEspacios[i].lower() not in self.LCorrectas:
                            TodasEncontradasL = False
                            break
                    if TodasEncontradasL:
                        self.Reloj.Terminar()
                        self.lblEstado.Text('Has Ganado Felicitaciones!')
                        self.VolveraJugar()
                else:
                    self.LIncorrectas += LIngresada
                    self.lblIncorrectas.Text("Letras Incorrectas: " + self.LIncorrectas)
                    self.lblEstado.Text ("Estado: Letra Incorrecta :(")
                    n = len(self.LIncorrectas)
                    self.ImgAhorcado.CInterface(p_img = self.ListaImagenes[n]) 
                    self.ImgAhorcado.Insertar()
            
                self.lblIngresadas.Text("Letras Ingresadas: " + self.LCorrectas+self.LIncorrectas)

        def CompLetra(self):
            LetraIngre = self.txtLetra.text.lower()
            LeIngresadas = self.LCorrectas + self.LIncorrectas

            if LetraIngre.strip() == '':
                self.lblEstado.Text ("Estado: Debe Ingresar una Letra")
            elif len(LetraIngre) > 1:
                self.lblEstado.Text ("Estado: Ingrese Solamente una Letra")
            elif LetraIngre in LeIngresadas:
                self.lblEstado.Text ("Estado: Usted ya Ingresado esta letra")
            elif LetraIngre not in 'abcdefghijklmnopqrstuvwxyz':
                self.lblEstado.Text ("Estado: Ingrese Letras Solamente")
            else:                        
                return True 

        def ComprobacionPierde(self):
            # Check if player has guessed too many times and lost
            if len(self.LIncorrectas) == 6:
                self.lblEstado.Text ("Estado: Pisaste Chaval(a)! XD")
                #La Animacion es una imagen por segundo
                self.ImgAhorcado.CInterface(p_img = self.ListaImagenes[6])
                self.ImgAhorcado.Insertar()
                pygame.display.update()
                time.sleep(1)
                self.ImgAhorcado.CInterface(p_img = self.ListaImagenes[7])
                self.ImgAhorcado.Insertar()
                pygame.display.update()
                time.sleep(1)
                self.ImgAhorcado.CInterface(p_img = self.ListaImagenes[8])
                self.ImgAhorcado.Insertar()
                pygame.display.update()
                time.sleep(1)
                self.Reloj.Terminar()
                self.PerJug(False,True)
                
        #Se pone en Perspectiva de Jugar de Nuevo
        def PerJug(self,perJ,perNuevoJ):
            #perNuevoJ => Perspectiva Juego
            self.lblIngresadas.Habilitar(perJ)
            self.lblIncorrectas.Habilitar(perJ)
            self.lblEstado.Habilitar(perJ)
            self.ImgAhorcado.Habilitar(perJ)
            self.lblPregunta.Habilitar(perJ)
            self.lblRespuesta.Habilitar(perJ)
            self.lblTiempo.Habilitar(perJ)
            #perNuevoJ => Perspectiva Nuevo Juego
            self.lblVJugar.Text('La Respuesta era "' + self.ReSecreta + '", Desea Volver a Jugar?')
            self.lblVJugar.Habilitar(perNuevoJ)
            self.btnSi.Habilitar(perNuevoJ)
            self.btnNo.Habilitar(perNuevoJ)
            self.PregJugar = perNuevoJ
                
        def Imprimir(self):
            self.MayCNucleo.Imprimir()
            self.LimpiarTxt()
                
        def getRandomIndex(self,Lmax):
            con = True
            while(con):
                if(len(self.IndJ) == (len(self.ListaRespuesta) - 1)):
                    self.IndJ = []
                # This function returns a random string from the passed list of strings.
                Index = random.randint(1, Lmax-1)
                if (Index not in self.IndJ):
                    self.IndJ.append(Index)
                    con = False
            return Index
        
        def VolveraJugar(self):
            self.CargarDatos()     
            self.lblIngresadas.Text("Ingresadas: ")        
            self.lblIncorrectas.Text("Letras Incorrectas: ")
            self.lblEstado.Text("Estado: ")
            self.lblTiempo.Text("Tiempo = 00:00 ")
            self.ImgAhorcado.CInterface(p_img = self.ListaImagenes[0])
            self.ImgAhorcado.Insertar()
            self.lblPregunta.Text(self.Pregunta)
            self.lblRespuesta.Text(self.ReSecretaImpr())                             
            self.LimpiarTxt()
            self.PerJug(True,False)
            self.Reloj.Comenzar()
            self.Imprimir()
                
        def AhorcadoCiclo(self):
            clock = pygame.time.Clock()
            while self.run:
                clock.tick(20)
                for e in gui.setEvents(pygame.event.get()):
                    self.MayCNucleo.MEventos(e)
                    if (self.txtLetra.enter == True and self.PregJugar == False):
                        self.evtVerificar()       
                        self.txtLetra.CEnter(False)    
                    if(self.PregJugar==False):                  
                        self.desktop.update()
                        self.desktop.draw()
                    
                pygame.display.update()