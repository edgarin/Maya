#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
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
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See thel
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
import pygame,os,sys
from MayModulos.MayCPrincipal import MayCPrincipal
import MayModulos.GlobalesI
from MayModulos.MayCNucleo import MayCNucleo
import thread
#Inicializo los Submódulos de Pygame
pygame.init()
#thread.start_new_thread(Globales.CicloEventos, ())
clock = pygame.time.Clock()

if __name__ == '__main__':
	GI=MayModulos.GlobalesI
	path_recursos_Ico = GI.path_recursosico
	#dt = clock.tick(20)
	pygame.display.set_icon(pygame.image.load(os.path.join(path_recursos_Ico, "MayI01.png")))
	pygame.display.set_caption("Juegos Para el Desarrollo Maya")
	Pantalla = pygame.display.set_mode(GI.Tamano_Pantalla, 0, 32)
	Nucleo=MayCNucleo()
	Nucleo.CDirRecursos(path_recursos_Ico)
	MayCPrincipal()
	