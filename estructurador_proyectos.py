#!/usr/bin/env python3
import os, sys, platform, json


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
file_json = 'templates/babylon.json'


# parents = []

# def readTree(data):
#     if isinstance(data, dict):
#         padre = data['name']
#         if isinstance(data['children'], list): 
#             if len(data['children']) > 0 :
#                 for c in data['children']:
#                     parents.append([padre, c['name']])
#                     readTree(c)
#             else:
#                 parents.append([padre , ""])

# with open(file_json) as json_file:
#     data = json.load(json_file)
#     readTree(data)

# for i in parents:
#     # obviando los directorios vacios:
#     if len(i[1]) > 0:
#         print(i)


# usando objetos:
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
            raise ValueError( 'the name {} is not a string type'.format(name) )
        self._name = name

    @property
    def childrens(self):
        return self._childrens

    @childrens.setter
    def set_childrens(self, childrens):
        if not isinstance(childrens, list):
            raise ValueError( 'the name {} is not a list type'.format(childrens) )
        self._childrens = childrens

    # metodos:
    def have_childs(self):
        if len(self.childrens) > 0:
            return True
        else:
            return False

    def get_childs(self):
        return [child for child in self.childrens]


# parseando:
def procesando(data):
    for key, value in data.items():
        if isinstance(value, str):
            # si value es string es un padre:
            fo = Folder(value, [])
            folders.append(fo)
        elif isinstance(value, list):
            # si es un listado de hijos:
            if fo in folders:
                childrens = value
                for child in childrens:
                    # print(fo.name)
                    fo.childrens.append(child['name'])
                    # print(" "+"└─"+child['name'])
                    procesando(child)

with open(file_json) as json_file:
    data = json.load(json_file)
    # print(data)
    # readTree(data)
    procesando(data)

# fin parseando

# referencia babylon.json:
# root_dir
#  └──sass
#  └──preloader
#  └──js1
#      └──libs1
#  └──resources
#      └──gui
#  └──dist
#      └──css
#      └──assets
#          └──agui
#              └──buttons
#      └──js2
#          └──libs2

# referencia babylon2.json:
# root_dir
#   └─index.html
#   └─css
#   └─js
#     └─SceneManager.js
#     └─main.js
#     └─sceneSubjects
#     └─libs
#       └─opt
#         └─jeje


# lectura:
name_folders = []
name_child_folders = []



last_childs = []

for obj in folders:
    space = ""
    target = obj.name

    if obj.have_childs():
        print(target)
        space += " "
        
        childrens = obj.get_childs()
        for child in childrens:
            print(space+"└─"+child)
