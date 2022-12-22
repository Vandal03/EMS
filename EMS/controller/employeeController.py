import json
import os
from utility import getFilePath
from model.employeeModel import employee
from model.employeesModel import employees as empList




def saveNewEmployee(firstName, lastName, storesWorked):
    if os.path.isfile(getFilePath() + "/employees.json"):
        newEmployee = employee(firstName, lastName, storesWorked)
        
        with open(getFilePath() + "/employees.json") as file:
            employeesList = json.load(file)
            employeesList["employees"].append(newEmployee.__dict__)
        with open(getFilePath() + "/employees.json", "w") as file:
            json.dump(employeesList, file)
    else:
        employees = empList()
        employeesStr = json.dumps(employees.__dict__)
        jsonFile = open(getFilePath() + "/employees.json", "w+")
        jsonFile.write(employeesStr)
        jsonFile.close()
        
        newEmployee = employee(firstName, lastName, storesWorked)
        

        with open(getFilePath() + "/employees.json") as file:
            employeesList = json.load(file)
            employeesList["employees"].append(newEmployee.__dict__)
        with open(getFilePath() + "/employees.json", "w") as file:
            json.dump(employeesList, file)


def updateEmployee(UUID, firstName, lastName, storesWorked):

    with open(getFilePath() + "/employees.json") as file:
        employees = json.load(file)
        for employee in employees["employees"]:
            if employee["UUID"] == UUID:
                employee["firstName"] = firstName
                employee["lastName"] = lastName
                employee["stores"].clear()
                employee["stores"] = storesWorked
                break
            else:
                continue
    with open(getFilePath() + "/employees.json", "w") as file:
        json.dump(employees, file)

   