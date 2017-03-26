#!/usr/bin/env python
from cgi import parse_header
import logging, os, sys, json

logging.basicConfig(level=logging.INFO)

def sendDictAsJSON(dict):
 jsonData = json.dumps(dict)
 output = "Content-Type: application/json;"
 output += "charset=utf-8" + "\n"
 output += "\n"
 output += str(jsonData) + "\n"
 print(output)
 logging.info("data send: " + output)

def getJsonDataAsDict():
 logging.info("start reading request")
 cl, _ = parse_header(os.environ['CONTENT_LENGTH'])
 dictData = json.loads(sys.stdin.read(int(cl)))
 logging.info("src data:" + str(dictData))
 return dictData

def voegContactToe(contact):
 # Hier moet straks code komen om het contact naar
 # file weg te schrijven.
 # Deze methode dient een 0 te retourneren als dat
 # wegschrijven goed is gelukt,
 # en anders een -1.
 return 0; # dit moet je dus ook straks aanpassen
# Hoofdprogramma

contact = getJsonDataAsDict()
logging.info(
 "Contact - naam: "
 + str(contact['naam'])
 + " - telnr: "
 + str(contact['telnr'])
)

errorCode = voegContactToe(contact)
responseDict = {"errorCode": errorCode}
sendDictAsJSON(responseDict)
