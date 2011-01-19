import pygame
import os.path
#Direccion de Iconos
path_recursosico = "./MayRecursos/MayIconos"
#Tamano_Pantalla = (640, 500)
Tamano_Pantalla = (800, 700)

####################################################Dimensiones#########################################################################        
#Tamano_Surface2
Tam_Surf2 = (800,700)
#Posicion_Surface2
#Pos_Surf2=(0,50)
Pos_Surf2 = (0,0)
####################################################Colores##################################################################3
#Barra Superior
#Color_Barra_Superior
Col_BarSu = (90,90,90)
#Color_SubBarras
Col_SubBar = (150,150,150)
#Color_Panel
Col_Pan = (245,25,190)


################################################Parametros Barra Superior############################################################
#Fondo Barra Superior
Fon_BarSu = pygame.image.load(os.path.join(path_recursosico,"Fon_SubBar.jpg"))
#Imagenes_Barra_Superior=>Por cada Menu(Boton)python
Img_BarSu = ['MayI01.png','MayI02.png']
#Mensajes_Barra_Superior=>Por cada Menu(Boton)
Mnj_BarSu = ['Mensaje Ayuda 1','Mensaje Ayuda 2']
#Ids_Botones_Barra_Superior=>Por cada Menu(Boton)
Id_Btn_BarSu = ['btnArchivo','btnAcerca_de']
#Tamano_Botones_Barra_Superior
TamBtn_BarSu = (50,40)
#Posiciones_Botones_Barra_Superior=>Desde Comienzan los Botones
PosBtn_BarSu = (10,5)

#Parametros Menus Barra Superior
#Ids_Botones_SubBarraMenus
Id_BtnSubBarMen = [['Salir'],['Acerca De..']]
#Imagenes_SubBarraMenus
Img_SubBarMen = [['MayINavegar.png'],['MayITools.png']]
#Mensajes_SubBarMenus
Mnj_SubBarMen = [['Salir'],['Acerca D']]
        
##################################################Parametros Panel######################################################################
#Imagenes_Panel
Img_Pan = ['Ahorcado.png','Atras.jpg','MayIPrint.png']
#Mensajes_Panel
Mnj_Pan = ['Juego Ahorcado Teorico','Memoria','Mensaje Late 3']
#Ids_Botones_Panel
Id_Btn_Pan = ['btnAhorcado','btnMemoria','btnIncognito']
TamBtn_Pan = (70,90)
PosBtn_Pan = (100,50)