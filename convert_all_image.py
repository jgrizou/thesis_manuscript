#!/usr/bin/python

import os
import sys
import subprocess

dpi = sys.argv[1]

hereFolder = os.path.dirname(os.path.realpath(__file__))
visualsFolder = os.path.join(hereFolder, "visuals")
visualsForThesisFolder = os.path.join(hereFolder, "visuals"+str(dpi))

if not os.path.exists(visualsForThesisFolder):
    os.makedirs(visualsForThesisFolder)

cnt = 0
for path, subdirs, files in os.walk(visualsFolder):
    for filename in files:
        extension = os.path.splitext(filename)[1]
        if extension == ".png":
            cnt += 1

            cmd = "convert "
            cmd += os.path.join(path, filename)
            cmd += " -units PixelsPerInch -resample "
            cmd += str(dpi)
            cmd += " "

            newFolder =  path.replace(visualsFolder, visualsForThesisFolder)
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)

            newFilename = os.path.join(newFolder, filename)
            cmd += newFilename

            dispStr = str(cnt) + ": converting " + filename + " ..."
            print dispStr
            
            subprocess.call(cmd, shell=True)




