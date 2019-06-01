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


# desde un archivo externo:
file_json = 'templates/babylon.json'


# manual:
# white_spaces = "  "
# with open(file_json, 'r') as handle:
#     data = json.load(handle)

#     if data['path'] == 'root':
#         print(data['path'])
#         data['path'] = root_project
#         for children_level0 in data['childrens']:
#             print("└─"+children_level0['path'])
#             if 'childrens' in children_level0:
#                 for children_level1 in children_level0['childrens']:
#                     print(white_spaces+"└─"+children_level1['path'])
#                     if 'childrens' in children_level1:
#                         for children_level2 in children_level1['childrens']:
#                             print(white_spaces+white_spaces+"└─"+children_level2['path'])

# ver el json tal cual:
# print(json.dumps(data, indent=4))


# print("\n\n\n\n")


# con recursividad:
white_spaces = "|"
level = 0

def detect(level, white_spaces, data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                detect(level, white_spaces, value)
                level += 1
            else:
                # se imprime root:
                print(value)
    elif isinstance(data, list):
        # print(level)
        white_spaces = white_spaces + white_spaces[0:len(white_spaces)*abs(level)]
        # white_spaces = white_spaces[0:-level]
        for item in data:
            for key, value in item.items():
                if isinstance(value, list):
                    detect(level, white_spaces, value)
                else:
                    print(white_spaces+"└─"+value)
                
                level = level + 1


with open(file_json, 'r') as handle:
    data = json.load(handle)
    detect(level, white_spaces, data)
