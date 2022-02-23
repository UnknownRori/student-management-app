from datetime import datetime
import json
import sys

class app:
    
    list_command = {
        "0": "Exit",
        "1": "Help",
        "2": "Add Student",
        "3": "Edit Student",
        "4": "Delete Student",
        "5": "View Student",
        "6": "Show All"
    }
    
    edit_student_command = {
        "0": "Back",
        "1": "Help",
        "2": "Edit Name",
        "3": "Add Score",
        "4": "Edit Score",
        "5": "Delete Score",
        "6": "Exit",
    }
    
    cache = {}
    command_buffer = ''
    
    # Initialize App Instance
    def __init__(self, db, filesystem):
        self.db = db(filesystem)
        
    def run(self):
        while True:
            self.command()
        
            if self.check_command(0):
                self.exit()
            elif self.check_command(1):
                print(json.dumps(self.list_command, indent=4))
            elif self.check_command(2):
                self.command('Enter Student Name')
                self.db.insert(self.command_buffer)
            elif self.check_command(3):
                print("Which Student you want to edit?")
                self.command("Name")
                self.edit_student()
            elif self.check_command(4):
                print("Which student data you want to delete?")
                self.command("Name")
                self.db.delete(self.command_buffer)
            elif self.check_command(5):
                print("Which student data you want to view?")
                self.command("Name")
                buffer = self.db.find(self.command_buffer)
                print(json.dumps(buffer, indent=4))
            elif self.check_command(6):
                print(json.dumps(self.db.all()))
    
    def edit_student(self):
        student = self.command_buffer
        self.cache = self.db.find(student)
        
        if(not self.db.find(student)): self.run()
        
        def score(note):
            print(f"What score do you want to {note}?")
            self.command(f"{student} | Score Name")
            score_name = self.command_buffer
            self.command(f"{student} | Score")
            score = self.command_buffer
            try:
                data['score'][score_name] = int(score)
                self.db.update(student, self.cache)
                self.cache = self.db.find(student)
            except:
                print("Please use Number!")
        
        while True:
            self.command(f"Edit {student}")
            if self.check_edit_student_command(0):
                print("Going Back to Main Menu")
                break
            elif self.check_edit_student_command(1):
                print(json.dumps(self.edit_student_command, indent=4))
            elif self.check_edit_student_command(2):
                print("Change name to?")
                self.command(f"{student} | Name")
                self.db.insert(self.command_buffer)
                self.db.update(self.command_buffer, self.cache)
                self.db.delete(student)
                break
            elif self.check_edit_student_command(3):
                score("add")
            elif self.check_edit_student_command(4):
                score("edit")
            elif self.check_edit_student_command(5):
                print("Which score do you want to delete?")
                self.command("Score")
                score_delete = self.command_buffer
                self.cache['score'].pop(score_delete)
                self.db.update(student, self.cache)
                self.cache = self.db.find(student)
            elif self.check_edit_student_command(6):
                self.exit()
    
    def command(self, text = ''):
        time = datetime.now()
        time = time.strftime("%H:%M:%S")
        self.command_buffer = str(input(f"{time} {text} >> ")).title()
    
    def exit(self):
        self.db.persist()
        print("Good Bye!")
        sys.exit() 
    
    def check_command(self, key):
        return str(self.list_command[str(key)]) == str(self.command_buffer) or str(self.command_buffer) == str(key)
        pass
    
    def check_edit_student_command(self, key):
        return str(self.edit_student_command[str(key)]) == str(self.command_buffer) or str(self.command_buffer) == str(key)
        pass