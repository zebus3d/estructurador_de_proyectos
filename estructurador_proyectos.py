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

# root_dir
#  └──sass
#  └──preloader
#  └──js1
#  ·   └──libs1
#  └──resources
#  ·   └──gui
#  └──dist
#  ·   └──css
#  ·   └──assets
#  ·   ·   └──agui
#  ·   ·   ·   └──buttons
#  ·   └──js2
#  ·   ·   └──libs2

parents = []

def readTree(data):
    if isinstance(data, dict):
        padre = data['name']
        if isinstance(data['children'], list): 
            if len(data['children']) > 0 :
                for c in data['children']:
                    parents.append([padre, c['name']])
                    readTree(c)
            else:
                parents.append([padre , ""])

with open(file_json) as json_file:
    data = json.load(json_file)
    readTree(data)

for i in parents:
    # obviando los directorios vacios:
    if len(i[1]) > 0:
        print(i)
