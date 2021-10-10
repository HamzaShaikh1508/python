# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:45:46 2021

@author: hamza_sk
"""
myDict = {"AIFF" : "Audio Interchange File Format" ,
          "AU" : "basic Audio" ,
          "AVI" : "Multimedia Audio/Video" ,
          "BAT" : "PC batch file" ,
          "BMP" : " Windows BitMap" ,
          "JAVA" : "java files" ,
          "CSV" : "Comma separated, variable length file",
          "CVS" : "Canvas",
          "DBF" : " dbase II, III, IV data",
          "DIF" : " Data Interchange format",
          "DOCX" : "Microsoft Word for Windows/Word97" ,
          "EPS" : " Encapsulated PostScript",
          "EXE" : "PC Application",
          "GIF" : " Graphics Interchange Format",
          "HQX" : "Macintosh BinHex",
          "HTML" : "web page source text",
          "JPEG" : "jpeg graphic",
          "MAC" : "mac paint",
          "MAP" : "Web page imagemap",
          "PDF" : "Acrobat -Portable document format",
          "PNG " : "Portable Network Graphics",
          "PPTX" : "PowerPoint",
          "TXT" : "ASCII text",
          "XLSX" : "Excel spreadsheet",
          "ZIP " : "PC Zip Compressed Archive",
          "PY" : "python"}
filename = input("Input the Filename: ")
f_extns = filename.split(".")
File_extension = f_extns[1]
print (myDict.get(File_extension))


    
        

    
    
