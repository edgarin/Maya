#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
#       
#       Copyleft 
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
import os.path

from MayCNucleo import MayCNucleo
from MayCObjeto import MayCObjeto

class MayCImagen(MayCObjeto):
    
    def __init__(self,p_ID,p_Imagen_Nombre,p_Coordenadas = (0,0),p_Tamano = (30,30),p_direccionico = None,p_Habilitado = True):
        MayCObjeto.__init__(self,p_ID,p_Coordenadas,p_Tamano,p_Habilitado)
        self.Nucleo = MayCNucleo()
        #Propiedades
        if(p_direccionico == None):
            self.Directorio_Imagenes = self.Nucleo.ObtDirRecursos()
        else:
            self.Directorio_Imagenes = p_direccionico
        
        self.Imagen_Nombre = p_Imagen_Nombre
        #Tipo de Objeto
        self.T_Objeto = 'Imagen'
        #Se asigna la Imagen
        self.PosenPantalla = self.Nucleo.ObtPosicion((self.pos_x,self.pos_y))    
        self.CInterface()
        self.Nucleo.Agregar(self)
    
    def Insertar(self,p_Interface = None):
        if (p_Interface == None):
            if(self.Contenedor != True):
                self.Nucleo.Insertar(self)
            else:
                self.Interface_Padre.blit(self.Interface,(self.pos_x,self.pos_y))
        else:
            p_Interface.blit(self.Interface,(self.pos_x,self.pos_y))
    
    def ObtInterface(self):
        return self.Interface
    def CInterface(self,p_img = None):
        if(self.Directorio_Imagenes != None and self.Imagen_Nombre != None):
            self.Interface = pygame.image.load(os.path.join(self.Directorio_Imagenes,self.Imagen_Nombre))
            self.Interface = pygame.transform.scale(self.Interface,( self.Ancho , self.Alto ))            
        elif(p_img != None):
            self.Interface = p_img
            self.Interface = pygame.transform.scale(self.Interface,( self.Ancho , self.Alto ))
        else:
            self.Interface = None
                        
    def Habilitar(self,p_Si_No):
        self.Habilitado = p_Si_No  
    def ObtHabilitado(self):
        return self.Habilitado      