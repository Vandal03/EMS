import sys
from PyQt6.QtWidgets import QApplication
from view.mainMenuView import mainMenu



def main():
    emsApp = QApplication([])
    appWindow = mainMenu()
    appWindow.show()
    sys.exit(emsApp.exec())


if __name__ == '__main__':
   main()



### To Do

# Add Active/Inactive to Employee Model
# Filter Employees by Store
# View and Edit Attendance Issues - QListViewWidget
# Ability to update absence types in config
