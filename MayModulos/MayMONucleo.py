'''
Created on 22/08/2010

@author: danielz360
'''
from MayCLabel import MayCLabel
from MayCBoton import MayCBoton
from MayCPanel import MayCPanel
from MayCImagen import MayCImagen
from MayCCuaTexto import MayCCuaTexto
from MayCBarraMenu import MayCBarraMenu

def MLabel(p_Texto,p_ID,p_Coordenadas,p_Color,p_Habilitado=True):
    habilitado = p_Habilitado
    Label = MayCLabel(p_Texto,p_ID,p_Coordenadas,p_Color,p_Habilitado = habilitado)
    return Label

def MBoton(p_ID,p_Imagen_Nombre,p_Coordenadas = (0,0),p_Tamano = (30,30),p_direccionico = None,p_Habilitado = True):
    coordenadas = p_Coordenadas
    tamano = p_Tamano
    direccion = p_direccionico
    habilitado = p_Habilitado
    
    Boton = MayCBoton(p_ID,p_Imagen_Nombre,p_Coordenadas = coordenadas,p_Tamano = tamano,p_direccionico = direccion,p_Habilitado = habilitado)
    return Boton

def MPanel(p_Posicion,p_Tamano,p_direccionico =  None,p_Habilitado = True):
    direccion = p_direccionico
    habilitado = p_Habilitado
    
    Panel = MayCPanel(p_Posicion,p_Tamano,p_direccionico =  p_direccionico,p_Habilitado = p_Habilitado)
    return Panel

def MImagen(p_ID,p_Imagen_Nombre,p_Coordenadas = (0,0),p_Tamano = (30,30),p_direccionico = None,p_Habilitado = True):
    coordenadas = p_Coordenadas
    tamano = p_Tamano
    direccion = p_direccionico
    habilitado = p_Habilitado
    
    Imagen = MayCImagen(p_ID,p_Imagen_Nombre,p_Coordenadas = coordenadas,p_Tamano = tamano,p_direccionico = direccion,p_Habilitado = habilitado)
    return Imagen

def MCuaTexto(p_ID,p_Coordenadas = (0,0),p_Ancho = 200, p_Fuente = 'arial', p_Texto = '' ,p_Habilitado = True):
    id = p_ID
    coordenadas = p_Coordenadas
    ancho = p_Ancho
    fuente = p_Fuente
    texto = p_Texto
    habilitado = p_Habilitado
    
    CuadroTexto = MayCCuaTexto(id,p_Coordenadas = coordenadas,p_Ancho = ancho, p_Fuente = fuente, p_Texto = texto ,p_Habilitado = habilitado)
    return CuadroTexto

def MBarraMenu(p_SubMenu = False,p_Tamano = (0,50),p_direccionico = None,p_Habilitado = True):
    tamano = p_Tamano
    direccion = p_direccionico
    habilitado = p_Habilitado
     
    BarraMenu = MayCBarraMenu(p_SubMenu = False,p_Tamano = tamano,p_direccionico = direccion,p_Habilitado = habilitado)
    return BarraMenu