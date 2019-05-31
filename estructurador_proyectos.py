#!/usr/bin/env python3


'''
    Copyright (c) 2019
    
    Jorge Hernández - Meléndez Saiz
    zebus3dream@gmail.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''


import os, sys


# nombre del proyecto o carpeta base/raiz:
root_proyect = "test"


def create_dir(dir_name):    
    if dir_name.startswith('/'):
        path = root_proyect + dir_name
    else:
        path = root_proyect + "/" + dir_name

    if not os.path.exists(path):
        print("creado: ", dir_name)
        # equivalente a un mkdir -p de linux:
        os.makedirs(path, exist_ok=True)


# directorios deseados:
target_dirs = ["dist/css", "dist/assets", "dist/js/libs", "js/libs", "levels", "sass", "resources/gui", "preloader"]


# creando los directorios deseados:
for dir in target_dirs:
    create_dir(dir)
