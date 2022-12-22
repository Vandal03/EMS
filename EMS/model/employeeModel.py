import uuid

class employee():
    def __init__(self, firstName, lastName, stores):
        self.firstName = firstName
        self.lastName = lastName
        rand = uuid.uuid1()
        self.UUID = str(rand)
        self.stores = stores
        self.attendanceIssues = []
        self.writeUps = []

    
   

    
