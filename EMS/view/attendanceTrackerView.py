from controller.attendanceTrackerController import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QDate
from utility import getStoreText, getFilePath, getTypes
import json


class attendanceTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set Up Window Details
        self.setWindowTitle("EMS: " + getStoreText())
        self.setFixedSize(300, 400)
        self.container = QWidget()
        self.setCentralWidget(self.container)

        # Create Layout and Widgets

        ## Create Employee Related Widgets
        self.employeeLabel = QLabel("Employee:")
        self.employee = QComboBox()
        self.employee.setPlaceholderText("Select an Employee")
        ## Create Employee Layouts
        hEmployeeLayout = QHBoxLayout()
        hEmployeeLayout.addWidget(self.employeeLabel)
        hEmployeeLayout.addWidget(self.employee)
        hEmployeeLayout.stretch(1)

        ## Create Reason Related Widgets
        self.typeLabel = QLabel("Type:")
        self.type = QComboBox()
        self.type.setPlaceholderText("Select a Type")
        ## Create Reason Layout
        hTypeLayout = QHBoxLayout()
        hTypeLayout.addWidget(self.typeLabel)
        hTypeLayout.addWidget(self.type)
        hTypeLayout.stretch(1)

        ## Create Date Related Widgets
        self.dateLabel = QLabel("Date:")
        self.date = QDateEdit(calendarPopup = True)
        self.date.setDate(QDate.currentDate())
        ## Create Date Layout
        hDateLayout = QHBoxLayout()
        hDateLayout.addWidget(self.dateLabel)
        hDateLayout.addWidget(self.date)
        hDateLayout.stretch(1)

        ## Create Note Related Widgets
        self.notesLabel = QLabel("Notes:")
        self.note = QPlainTextEdit()
        ## Create Note Layout
        vNoteLayout = QVBoxLayout()
        vNoteLayout.addWidget(self.notesLabel)
        vNoteLayout.addWidget(self.note)
        

        ## Create Save Button Widget
        self.saveButton = QPushButton("Save")
        self.saveButton.setFixedSize(150, 30)
        self.saveButton.clicked.connect(lambda: saveAttendance(self.employee.currentText(), self.employee.currentData(), self.type.currentText(), self.date.text(), self.note.toPlainText()))
        ## Create Save Button Layout
        hSaveButtonLayout = QHBoxLayout()
        hSaveButtonLayout.addWidget(self.saveButton)

        ## Create Back Button Widget
        self.backButton = QPushButton("Back")
        self.backButton.setFixedSize(150, 30)
        self.backButton.clicked.connect(self.closeForm)
        ## Create Back Button Layout
        hBackButtonLayout = QHBoxLayout()
        hBackButtonLayout.addWidget(self.backButton)
        

        ## Create Layout
        vLayout = QVBoxLayout()
        vLayout.addLayout(hEmployeeLayout)
        vLayout.addLayout(hTypeLayout)
        vLayout.addLayout(hDateLayout)
        vLayout.addLayout(vNoteLayout)
        vLayout.addLayout(hSaveButtonLayout)
        vLayout.addLayout(hBackButtonLayout)
        self.container.setLayout(vLayout)

        self.loadEmployees()
        self.loadTypes()

    def closeForm(self):
        self.close()

    def loadEmployees(self):
        employeeJSON = open(getFilePath() + "/employees.json")
        employeeData = json.loads(employeeJSON.read())
        employees = employeeData["employees"]

        for employee in employees:
            self.employee.addItem(employee["firstName"] + " " + employee["lastName"], employee["UUID"])
            
    def loadTypes(self):
        types = getTypes()
        for type in types:
            self.type.addItem(type)