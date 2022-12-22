from PyQt6.QtWidgets import *
from controller.configureController import saveFilePath, saveStore
import configparser
import os
from utility import getStoreText
import sys

class configure(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creating Window Details
        self.setWindowTitle("EMS: " + getStoreText())
        self.setFixedSize(400, 150)
        self.container = QWidget()
        self.setCentralWidget(self.container)

        # Creating Layout & Widgets

        ## Creating File Path Related Widgets
        self.filePathLabel = QLabel("Google Drive Path:")
        self.filePathInput = QLineEdit()
        self.filePathInput.setPlaceholderText("Input Google Drive Path")
        self.loadFilePath()
        ## Creating File Path Layout
        hFilePathLayout = QHBoxLayout()
        hFilePathLayout.addWidget(self.filePathLabel)
        hFilePathLayout.addWidget(self.filePathInput)

        ## Creating Store Related Widgets
        self.storeLabel = QLabel("Store:")
        self.store = QComboBox()
        stores = self.loadStores()
        for store in stores:
            self.store.addItem(store)
        self.loadStore()
        ## Creating Store Layout
        hStoreLayout = QHBoxLayout()
        hStoreLayout.addWidget(self.storeLabel)
        hStoreLayout.addWidget(self.store)
        hStoreLayout.addStretch(1)

        ## Creating Save Button
        self.saveButton = QPushButton("Save")
        self.saveButton.setFixedSize(150, 30)
        self.saveButton.clicked.connect(lambda: saveFilePath(self.filePathInput.text()))
        self.saveButton.clicked.connect(lambda: saveStore(self.store.currentText()))
        self.saveButton.clicked.connect(self.restart)
        ## Creating Save Button Layout
        hSaveButtonLayout = QHBoxLayout()
        hSaveButtonLayout.addWidget(self.saveButton)

        ## Creating Back Button
        self.backButton = QPushButton("Back")
        self.backButton.setFixedSize(150, 30)
        self.backButton.clicked.connect(self.closeForm)
        ## Creating Back Button Layout
        hBackButtonLayout = QHBoxLayout()
        hBackButtonLayout.addWidget(self.backButton)
        
        
        ##Layout Creation
        vConfigureLayout = QVBoxLayout()
        vConfigureLayout.addLayout(hFilePathLayout)
        vConfigureLayout.addLayout(hStoreLayout)
        vConfigureLayout.addLayout(hSaveButtonLayout)
        vConfigureLayout.addLayout(hBackButtonLayout)
        self.container.setLayout(vConfigureLayout)

    # View Functions
    def closeForm(self):
        self.close()

    def loadFilePath(self):
        try:
            readConfig = configparser.ConfigParser()
            readConfig.read(os.getcwd() + "/configfile.ini")
            paths = readConfig["paths"]
            currentPath = paths["gdpath"]
            self.filePathInput.setText(currentPath)
        except:
            print("File Not Found.")

    def loadStores(self):
        loadConfig = configparser.ConfigParser()
        loadConfig.read(os.getcwd() + "/configfile.ini")
        stores = loadConfig["stores"]
        options = [stores["lagro"], stores["hoosier_point"], stores["south_whitley"], stores["silver_lake"], stores["fast_mart"]]
        return options

    def loadStore(self):
        try:
            readConfig = configparser.ConfigParser()
            readConfig.read(os.getcwd() + "/configfile.ini")
            selected = readConfig["selected"]
            currentStore = selected["store"]
            self.store.setCurrentText(currentStore)
        except:
            print("File Not Found.")

    def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)