#!/usr/bin/python

import os
import sys
import subprocess

hereFolder = os.path.dirname(os.path.realpath(__file__))
visualsFolder = os.path.join(hereFolder, "visuals")
visualsForThesisFolder = os.path.join(hereFolder, "visualspdf")

if not os.path.exists(visualsForThesisFolder):
    os.makedirs(visualsForThesisFolder)

cnt = 0
for path, subdirs, files in os.walk(visualsFolder):
    for filename in files:
        name, extension = os.path.splitext(filename)
        if extension == ".svg":
            cnt += 1

            infile = os.path.join(path, filename)

            newFolder =  path.replace(visualsFolder, visualsForThesisFolder)
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)

            outfile = os.path.join(newFolder, name+".pdf")

            cmd = "inkscape --file=" + infile + " --export-pdf=" + outfile

            dispStr = str(cnt) + ": converting " + filename + " to pdf ..."
            print dispStr
            
            subprocess.call(cmd, shell=True)




