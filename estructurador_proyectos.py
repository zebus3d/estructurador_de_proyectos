#!/usr/bin/python3
import os, sys


root_proyect = "test"


def create_dir(dir_name):    
    if dir_name.startswith('/'):
        path = root_proyect + dir_name
    else:
        path = root_proyect + "/"+ dir_name

    if not os.path.exists(path):
        print("creado: ", dir_name)
        os.makedirs(path, exist_ok=True)


target_dirs = ["dist/css", "dist/assets", "dist/js/libs", "js/libs", "levels", "sass", "resources/gui", "preloader"]


for dir in target_dirs:
    create_dir(dir)
