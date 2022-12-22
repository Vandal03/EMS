from PyQt6.QtWidgets import QWidget, QMenu, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout
from view.attendanceTrackerView import attendanceTracker
from view.configureView import configure
from utility import getStoreText
from view.employeesView import employees


class mainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set mainMenu Window Details
        self.setWindowTitle("EMS: " + getStoreText())
        self.setFixedSize(300, 100)
        self._createMenuBar()
        self.container = QWidget()
        self.setCentralWidget(self.container)

        # Layout & Button Creation

        ## Attendance Tracker Button Set Up
        self.attendanceTrackerButton = QPushButton("Attendance Tracking")
        self.attendanceTrackerButton.setFixedSize(150, 30)
        self.attendanceTrackerButton.clicked.connect(self.openAttendanceTracker)
        ## Attendance Tracker Button Layout
        hAttendanceTrackerButtonLayout = QHBoxLayout()
        hAttendanceTrackerButtonLayout.addStretch(1)
        hAttendanceTrackerButtonLayout.addWidget(self.attendanceTrackerButton)
        hAttendanceTrackerButtonLayout.addStretch(1)

        ## Layout Creation
        vButtonLayout = QVBoxLayout()
        vButtonLayout.addLayout(hAttendanceTrackerButtonLayout)
        vButtonLayout.addStretch(1)
        self.container.setLayout(vButtonLayout)
        

    # Function to Open Attendance Tracking Form
    def openAttendanceTracker(self):
        self.appWindow = attendanceTracker()
        self.appWindow.show()
        
    # Function to Create MenuBar
    def _createMenuBar(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        optionMenu = QMenu("&Options", self)
        menuBar.addMenu(optionMenu)
    
        optionMenu.addAction("Configure", self.openConfigure)
        optionMenu.addAction("Employees", self.openEmployees)
        
    # Function to Open File Path Options
    def openConfigure(self):
        self.appWindow = configure()
        self.appWindow.show()

    def openEmployees(self):
        self.appWindow = employees()
        self.appWindow.show()