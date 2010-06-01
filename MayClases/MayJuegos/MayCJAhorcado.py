# encoding: utf-8
import pygame,random,time,codecs,sys
#import gui
#from gui import *
pygame.init()
#import defaultStyle

#run = True
#screen = pygame.display.set_mode((640,480))
#defaultStyle.init(gui)
#desktop = gui.Desktop()
  
class MayCJAhorcado():   
            
        def __init__(self,p_Interface,p_Desktop):
            self.screen=p_Interface
            desktop = p_Desktop
            self.screen.fill((0,0,0))
            self.buttonsalir = Button(position = (480,450),parent = desktop, text = "Salir")
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
        
        def GUI(self):
            lblIngresadas = Label(position=(50,25),text="Letras Ingresadas: ",parent=desktop)
            self.lblIngresadas = lblIngresadas
            #self.add(lblIngresadas)
        
            lblIncorrectas = Label(position=(50,50),text="Letras Incorrectas: ",parent=desktop)
            self.lblIncorrectas = lblIncorrectas
                    
            lblEstado = Label(position=(260,25),size=(200,0),text="Estado Juego: ",parent=desktop)
            self.lblEstado = lblEstado
        
            self.ImprimirImagen(self.ListaImagenes[0])
            
            lblPregunta = Label(position=(250,95),size=(200,0),text=self.PreSecreta,parent=desktop)
            self.lblPregunta = lblPregunta
        
            lblCorrectas = Label(position=(250,325),size=(200,0),text=self.ReSecretaImpr(),parent=desktop)            
            self.lblCorrectas = lblCorrectas
        
            self.txtLetra = TextBox(position=(200,360),size=(200,0),text="Letra: ",parent=desktop)            
                
            self.btn = Button(position = (240,400),parent = desktop, text = "Ok")
            self.btn.onClick = self.evt_click          
            #btn = Button("OK", action = self.evt_click)
        
        def CargadoImagnes(self):
            imagen=None
            Lista=[]
            for a in range(9):
                imagen=pygame.image.load(str(a) + '.jpg')
                imagen= pygame.transform.scale(imagen, (200, 200))            
                Lista.append(imagen)
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
        
        def evt_click(self,widget):
            self.ComprobacionMB()    
            self.ComprobacionPierde()
            self.LimpiarTxt()

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
                    self.ImprimirImagen(self.ListaImagenes[len(self.LIncorrectas)])
            
                self.lblIngresadas.text="Letras Ingresadas: "+self.LCorrectas+self.LIncorrectas
    
        def LimpiarTxt(self):
            self.txtLetra.text=""

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
                self.ImprimirImagen(self.ListaImagenes[6])
                time.sleep(1)
                self.ImprimirImagen(self.ListaImagenes[7])
                time.sleep(1)
                self.ImprimirImagen(self.ListaImagenes[0])

        def getRandomIndex(self,Lmax):
            # This function returns a random string from the passed list of strings.
            Index = random.randint(0, Lmax-1)
            return Index
    
        def buttonsalir_onClick(self,widget): #@NoSelf
            sys.exit()
        
        def ImprimirImagen(self, imagen):
            a = imagen
#            imagen = pygame.transform.scale(imagen, (200,200))
            self.screen.blit(a,(200,120))
            
            
#
#MayCJAhorcado()
#
#while run:
#    for e in gui.setEvents(pygame.event.get()):
#        if e.type == pygame.QUIT:
#            run = False
#    desktop.update()
#    desktop.draw()
#    pygame.display.update()