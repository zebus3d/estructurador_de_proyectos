#!/usr/bin/env python3
import os
import sys
import platform
import json


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

# variables:
OS = platform.system()

# nombre de la carpeta base/raiz (nombre del proyecto):
root_project = "AwesomeProject"

# slash segun sistema operativo:
if OS == 'Windows':
    slash = "\\"
else:
    slash = "/"

# Desde un archivo externo:
file_json = 'templates/test1.json'
# file_json = 'templates/babylon.json'
# # file_json = 'templates/babylon2.json'


# Con objetos:
# list of objects folders:
folders = []


class Folder():
    def __init__(self, name="", childrens=[]):
        self._name = name
        self._childrens = childrens

    @property
    def name(self):
        return self._name

    @name.setter
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError('the name {} is not a string type'.format(name))
        self._name = name

    @property
    def childrens(self):
        return self._childrens

    @childrens.setter
    def set_childrens(self, childrens):
        if not isinstance(childrens, list):
            raise ValueError(
                'the name {} is not a list type'.format(childrens))
        self._childrens = childrens

    # metodos:
    def have_childs(self):
        if len(self.childrens) > 0:
            return True
        else:
            return False

    def get_childs(self):
        return [child for child in self.childrens]


# referencia test1.json:
# root_dir
#  └─index.html
#  └─css
#  ¦  └─style.css
#  └─sass
#  ¦  └─style.sass
#  └─js
#  ¦  └─libs
#  └─resources
#  ¦  └─img
#  ¦  └─gui

# referencia test2.json:
# root_dir
#  └─index.html
#  └─css
#  └─js
#  ¦  └─SceneManager.js
#  ¦  └─main.js
#  ¦  └─sceneSubjects
#  ¦  └─libs
#  ¦  ¦  └─opt
#  ¦  ¦  ¦  └─jeje

# parseando y dibujando:
last_childs = []
space = ""


def procesando(space, data):
    for key, value in data.items():
        if isinstance(value, str):
            # si value es string es un padre:
            padre = value
            fo = Folder(value, [])
            folders.append(fo)

            # print(padre, last_childs)
            if padre not in last_childs:
                print(space+padre)
            else:
                space += "¦ "

        elif isinstance(value, list):
            childrens = value
            space += " "
            for child in childrens:
                last_childs.append(child['name'])

                print(space+"└─"+child['name'])

                fo.childrens.append(child['name'])
                procesando(space, child)

            space = ""


with open(file_json) as json_file:
    data = json.load(json_file)
    # print(data)
    # readTree(data)
    procesando(space, data)

# fin parseando
