import json
class filesystem:
    
    # Initialize json instance
    def __init__(self, file):
        self.file = file
    
    # Write json file
    def write(self, data):
        buffer = json.dumps(data, indent=4)
        with open(self.file, 'w') as f:
            f.write(buffer)
    
    # Read json file
    def read(self):
        with open(self.file) as f:
            return json.load(f)