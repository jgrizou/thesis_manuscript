#!/usr/bin/python

import os
import sys
import subprocess

hereFolder = os.path.dirname(os.path.realpath(__file__))
visualsFolder = os.path.join(hereFolder, "visuals")

cnt = 0
for path, subdirs, files in os.walk(visualsFolder):
    for filename in files:
        name, extension = os.path.splitext(filename)
        if extension == ".svg":
            cnt += 1

            infile = os.path.join(path, filename)

            cmd = "inkscape --file=" + infile + " --verb FitCanvasToDrawing --verb FileSave --verb FileClose"

            dispStr = str(cnt) + ": fitting canvas to drawing for " + filename + " ..."
            print dispStr
            
            subprocess.call(cmd, shell=True)