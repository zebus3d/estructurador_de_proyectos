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


yes = {'YES', 'Yes', 'yes','y', 'ye', ''}
no = {'NO', 'No', 'no','n'}

# Desde un archivo externo:
file_json = 'templates/babylon.json'


parents = []


def have_childrens(item):
    hijos = len(item['children'])
    if hijos > 0:
        print("folder: " + item['name'], " have ", hijos, " childrens")
        return True
    else:
        print("folder: " + item['name'], "not have childrens")
        return False

family = []

def readTree(data):
    if have_childrens(data):
        pack = []
        pack = [data['name'], [child['name'] for child in data['children']]]
        family.append(pack)        

        for child in data['children']:
            if have_childrens(child):
                readTree(child)
    else:
        family.append(data['name'])


with open(file_json) as json_file:
    json_data = json.load(json_file)
    # print(json_data)
    readTree(json_data)

# print(family)
for i in family:
    print(i)