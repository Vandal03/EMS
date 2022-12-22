import configparser
import os
import json

def getStoreText():
    try:
        readConfig = configparser.ConfigParser()
        readConfig.read(os.getcwd() + "/configfile.ini")
        selected = readConfig["selected"]
        currentStore = selected["store"]
        return currentStore
    except:
        print("File Not Found.")

def getStores():
    try:
        readConfig = configparser.ConfigParser()
        readConfig.read(os.getcwd() + "/configfile.ini")
        stores = readConfig["stores"]
        return stores
    except:
        print("File Not Found.")

def getFilePath():
    try:
        readConfig = configparser.ConfigParser()
        readConfig.read(os.getcwd() + "/configfile.ini")
        paths = readConfig["paths"]
        gdFilePath = paths["gdpath"]
        return gdFilePath
    except:
        print("File Not Found.")

def getTypes():
    try:
        readConfig = configparser.ConfigParser()
        readConfig.read(os.getcwd() + "/configfile.ini")
        types = readConfig["absent_types"]
        options = [types["ncns"], types["lt"], types["co"]]
        return options
    except:
        print("File Not Found.")

def getEmployees():
    try:
        with open(getFilePath() + "/employees.json", "r") as file:
            employeesFile = json.load(file)
            employees = employeesFile["employees"]
            return employees
    except:
        print("file not found")