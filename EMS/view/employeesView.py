from PyQt6.QtWidgets import *
from utility import getStoreText, getStores, getEmployees
from controller.employeeController import saveNewEmployee, updateEmployee


class employees(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set mainMenu Window Details
        self.setWindowTitle("EMS: " + getStoreText())
        self.setFixedSize(500, 300)
        self.container = QWidget()
        self.setCentralWidget(self.container)
        
        # Create Grid Layout
        employeesGrid = QGridLayout()
        employeesGrid.setColumnMinimumWidth(2, 25)
        employeesGrid.setColumnStretch(3, 9)
        ## First Name Section
        self.firstNameLabel = QLabel("First Name:")
        employeesGrid.addWidget(self.firstNameLabel, 0, 0)
        self.firstNameInput = QLineEdit()
        self.firstNameInput.setPlaceholderText("Enter First Name")
        employeesGrid.addWidget(self.firstNameInput, 0, 1)
        ## Last Name Section
        self.lastNameLabel = QLabel("Last Name:")
        employeesGrid.addWidget(self.lastNameLabel, 1, 0)
        self.lastNameInput = QLineEdit()
        self.lastNameInput.setPlaceholderText("Enter Last Name")
        employeesGrid.addWidget(self.lastNameInput, 1, 1)
        ## Store Section - May cause problems later on =) 
        self.storesLabel = QLabel("Stores:")
        employeesGrid.addWidget(self.storesLabel, 2, 0)
        stores = getStores()
        i = 3
        for store in stores.values():
            storeCheckBox = QCheckBox()
            storeCheckBox.setText(store)
            employeesGrid.addWidget(storeCheckBox, i, 0)
            i += 1
        ## Add New Button
        self.saveButton = QPushButton("Add New")
        self.saveButton.clicked.connect(lambda: saveNewEmployee(self.firstNameInput.text(), self.lastNameInput.text(), storesWorked = self.getSelectedStores()))
        self.saveButton.clicked.connect(self.formClear)
        self.saveButton.clicked.connect(self.loadEmployeeList)
        employeesGrid.addWidget(self.saveButton, 8, 1)
        ## Add Clear Button
        self.clearButton = QPushButton("Clear Form")
        self.clearButton.clicked.connect(self.formClear)
        employeesGrid.addWidget(self.clearButton, 8, 0)
        ## Update Existing Employee
        self.updateButton = QPushButton("Update Employee")
        self.updateButton.clicked.connect(lambda: updateEmployee(self.empUUID, self.firstNameInput.text(), self.lastNameInput.text(), storesWorked = self.getSelectedStores()))
        self.updateButton.clicked.connect(self.formClear)
        self.updateButton.clicked.connect(self.loadEmployeeList)
        employeesGrid.addWidget(self.updateButton, 9, 1)
        ## Back Button
        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.closeForm)
        employeesGrid.addWidget(self.backButton, 9, 0)
        ## Employee List
        self.employeeList = QListWidget()
        self.employeeList.setMinimumHeight(250)
        self.setMaximumWidth(50)
        employeesGrid.addWidget(self.employeeList, 0, 3)
        self.loadEmployeeList()
        ## Set Layout
        self.container.setLayout(employeesGrid)
        self.empUUID = ""
        self.updateButtonState()

    def closeForm(self):
        self.close()

    def getSelectedStores(self):
        selectedCheckboxes = []
        Checkboxes = self.container.findChildren(QCheckBox)
        for cb in Checkboxes:
            if cb.isChecked():
                selectedCheckboxes.append(cb.text())
        return selectedCheckboxes
    
    def formClear(self):
        self.firstNameInput.clear()
        self.lastNameInput.clear()
        self.empUUID = ""
        self.clearCheckboxes()
        self.updateButtonState()

    def selectEmployee(self):
        self.clearCheckboxes()
        selectedEmployeeIndex = self.employeeList.currentRow()
        self.firstNameInput.setText(self.employeesData[selectedEmployeeIndex]['firstName'])
        self.lastNameInput.setText(self.employeesData[selectedEmployeeIndex]['lastName'])
        for store in self.employeesData[selectedEmployeeIndex]['stores']:
            checkboxes = self.container.findChildren(QCheckBox)
            for cb in checkboxes:
                if cb.text() == store:
                    cb.setChecked(True)
        self.empUUID = self.employeesData[selectedEmployeeIndex]['UUID']
        self.updateButtonState()
        
       
    def clearCheckboxes(self):
        Checkboxes = self.container.findChildren(QCheckBox)
        for cb in Checkboxes:
            if cb.isChecked():
                cb.setChecked(False)


    def loadEmployeeList(self):
        self.employeeList.clear()
        self.employeesData = getEmployees()
        self.employeeList.itemClicked.connect(lambda: self.selectEmployee())
        try:
            for employee in self.employeesData:
               self.employeeList.addItem(employee["firstName"] + " " + employee["lastName"])
        except:
            print("No Employees Found")

    def updateButtonState(self):
        if self.empUUID == "":
            self.updateButton.setDisabled(True)
            self.saveButton.setDisabled(False)
        else:
            self.updateButton.setDisabled(False)
            self.saveButton.setDisabled(True)