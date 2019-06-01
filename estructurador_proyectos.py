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
root_project = "test"

# slash segun sistema operativo:
if OS == 'Windows':
    slash = "\\"
else:
    slash = "/"

# directorios deseados:
target_dirs = {
    "type": "folder",
    "name": "root",
    "path": root_project,
    "childrens": [{
        "type": "folder",
        "name": "sass",
        "path": root_project+slash+"sass"
    },{
        "type": "folder",
        "name": "preloader",
        "path": root_project+slash+"preloader"
    },{
        "type": "folder",
        "name": "js",
        "path": root_project+slash+"js",
        "childrens": [{
                "type": "folder",
                "name": "libs",
                "path": root_project+slash+"js"+slash+"libs"
        }]
    },{
        "type": "folder",
        "name": "resources",
        "path": root_project+slash+"resources",
        "childrens": [{
                "type": "folder",
                "name": "libs",
                "path": root_project+slash+"resources"+slash+"gui"
        }]
    },{
        "type": "folder",
        "name": "dist",
        "path": root_project+slash+"dist",
        "childrens": [{
                "type": "folder",
                "name": "css",
                "path": root_project+slash+"dist"+slash+"css"
            },{
                "type": "folder",
                "name": "assets",
                "path": root_project+slash+"dist"+slash+"assets"
            },{
                "type": "folder",
                "name": "js",
                "path": root_project+slash+"dist"+slash+"js",
                "childrens": [{
                    "type": "folder",
                    "name": "libs",
                    "path": root_project+slash+"dist"+slash+"js"+slash+"libs"
                }]
            }]
    }]
}

# visualizar el json si esta embed en una variable:
# jdump = json.dumps(target_dirs, indent=4)
# print(jdump)

# desde un archivo externo:
file_json = 'templates/babylon.json'

with open(file_json, 'r') as handle:
    parsed = json.load(handle)

print(json.dumps(parsed, indent=4))