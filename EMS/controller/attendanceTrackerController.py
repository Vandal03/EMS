from model.attendanceModel import attendance
import json
from utility import getFilePath


def saveAttendance(employee, uuid, type, date, note):
    # Create Record Object to be Saved
    record = attendance(employee, type, date, note)


    with open(getFilePath() + "/employees.json") as file:
        employeesFile = json.load(file)
        employees = employeesFile["employees"]
        for employee in employees:
            if employee["UUID"] == uuid:
                employee["attendanceIssues"].append(record.__dict__)
                with open(getFilePath() + "/employees.json", "w") as file:
                    json.dump(employeesFile, file)
                break
            else:
                continue
        

    
        



