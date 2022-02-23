from app.app import app
from app.db import db
from app.filesystem import filesystem

def run():
    print("Welcome to Student Management CLI")
    program = app(db, filesystem)
    program.run()
    
if __name__ == '__main__':
    run()