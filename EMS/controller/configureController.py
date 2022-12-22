import configparser
from model.configureModel import filePath
import os

def saveFilePath(gdFilePath):
    edit = configparser.ConfigParser()
    edit.read(os.getcwd() + "/configfile.ini")
    paths = edit["paths"]
    filePathObj = filePath(gdFilePath)
    paths["gdpath"] = filePathObj.gdFilePath
    with open(os.getcwd() + "/configfile.ini", 'w') as configfile:
        edit.write(configfile)

def saveStore(store):
    edit = configparser.ConfigParser()
    edit.read(os.getcwd() + "/configfile.ini")
    selected = edit["selected"]
    selected["store"] = store
    with open(os.getcwd() + "/configfile.ini", 'w') as configfile:
        edit.write(configfile)