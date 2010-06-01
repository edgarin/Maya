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

class MayCLabel(object):
    
    def __init__(self,p_Interface_Padre,p_Texto,p_ID,p_Coordenadas,p_Color):
        #Inicializo SubMódulos de Pygamep_Mensaje
        pygame.init()
        #Propiedades
        self.ID=p_ID
        self.pos_x,self.pos_y=p_Coordenadas
        self.Texto=p_Texto
        self.Interface_Padre = p_Interface_Padre
        self.Color = p_Color
    
    def Insertar(self):
        self.CrearLabel()
        self.Interface_Padre.blit(self.Texto_Final,(self.pos_x,self.pos_y))

    def CrearLabel(self):
        Fuente = pygame.font.SysFont("arial", 16)
        if self.Color == "blanco":
            self.Texto_Final = Fuente.render(self.Texto, True, (255, 255, 255), (0, 0, 0))
        elif self.Color == "rojo":
            self.Texto_Final = Fuente.render(self.Texto, True, (224, 23, 23), (0, 0, 0))
        self.Interface_Padre.blit(self.Texto_Final,(self.pos_x,self.pos_y))
    
    def Append(self, Mensaje):
        self.Texto += Mensaje
        self.CrearLabel()
        self.Insertar()
    
    def Text(self, Mensaje):
        self.Texto = Mensaje
        self.CrearLabel()
        self.Insertar()
    
    def NuevoEstado(self, Mensaje):
        self.Texto = "Estado: " + Mensaje
        self.CrearLabel()
        self.Insertar()    
        
        
    
    
                