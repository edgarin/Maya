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

import pygame
import os.path
from MayCNucleo import MayCNucleo
from MayCObjeto import MayCObjeto

class MayCLabel(MayCObjeto):

    def __init__(self,p_Texto,p_ID,p_Coordenadas,p_Color,p_Habilitado=True):
        #Propiedades
        self.Texto = p_Texto
        self.Color = p_Color
        self.CrearLabel()
        #Tipo de Objeto
        self.T_Objeto = 'Etiqueta'
        
        p_tamano = self.Texto_Final.get_size()
        MayCObjeto.__init__(self,p_ID,p_Coordenadas,p_tamano,p_Habilitado)    
        self.Nucleo = MayCNucleo()
        self.PosenPantalla = self.Nucleo.ObtPosicion((self.pos_x,self.pos_y))
        self.Nucleo.Agregar(self)   

    def ObtInterface(self):
        return self.Texto_Final      
                                                
    def Insertar(self):
        if (self.Contenedor == True):
            self.Interface_Padre.blit(self.Texto_Final,(self.pos_x,self.pos_y))
        else:
            self.Nucleo.Insertar(self)    

    def Negrita(self, p_valor = False):
        """
            Habilita el dibujado de la fuente en Negrita mientras que esta
            lo soporte, en caso contrario pygame emula dicho modo.
        """
        self.Fuente.set_bold(value)
     
        
    def Cursiva(self, p_valor = False):
        """
            Habilita la imitacion que da de texto en cursiva, por ende como en
            el caso de bold() el tipo de fuente tiene que poder soportar el 
            mismo.        
        """
        self.Fuente.set_italic(value)
        
    def CrearLabel(self):
        self.Fuente = pygame.font.SysFont("arial", 16)
        if self.Color == "blanco" or self.Color == "Blanco":
            self.Texto_Final = self.Fuente.render(self.Texto, True, (255, 255, 255), (0, 0, 0))
        elif self.Color == "rojo" or self.Color == "Rojo":
            self.Texto_Final = self.Fuente.render(self.Texto, True, (224, 23, 23), (0, 0, 0))
        self.CTamano(self.Texto_Final.get_size())
    
    def Append(self, Mensaje):
        self.Texto += Mensaje
        self.CrearLabel()
        self.Insertar()
    
    def Text(self, Mensaje):
        self.Texto = Mensaje
        self.CrearLabel()
        self.Insertar()     