import json
class db:
    
    data = {}
    
    def __init__(self, filesystem, database = './database/database.json'):
        self.Filesystem = filesystem(database)
        self.read()
        
    # Helper Method

    # Persist the change into database
    def persist(self):
        self.Filesystem.write(self.data)
        pass

    # Read the Database, it will create the database if it's doesn't exist
    def read(self):
        try:
            self.data = self.Filesystem.read()
        except:
            print("Database file not found!")
            print("Creating new Database file!")
            self.Filesystem.write(self.data)

    # Check the key is exist inside the database
    def exist(self, name: str):
        if name in self.data: return True
        return False

    # Database Command

    # Retrieve all data inside the database
    def all(self):
        return json.dumps(self.data, indent=4)

    # Find specific key inside database
    def find(self, name: str):
        if self.exist(name):
            return self.data.get(name)

        return False

    def update(self, name:str, data: dict):
        self.read()
        if self.exist(name):
            self.data[name] = data
            self.persist()
            return True
        else:
            return False

    def insert(self, name, data = {}):
        self.read()
        if self.exist(name):
            return False
        else:
            self.data[name] = data
            self.persist()
            return True

    def delete(self, name: str):
        self.read()
        if self.exist(name):
            del self.data[name]
            self.persist()
            return True
        else:
            return False