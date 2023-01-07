from Translators import JSON_Translator
from Task import ToDoList

class Program:
    def __init__(self,fileName):
        self.fileName = fileName
        self.JTran = JSON_Translator(self.fileName)
        
    def load(self):
        self.JTran.read_in()
        self.todo = self.JTran.into_ToDoList()
        
    def display(self):
        self.todo.display_all()
    
    def create(self):
        self.todo.create_task()
    
    def completedTask(self):
        taskName = input('taskName: ')
        self.todo.task_completed(taskName)
     
    def updateTags(self):
        taskName = input('taskName: ')
        new_tag = input('new_tag: ')
        
        self.todo.update_tags(taskName, new_tag)
    
    def evaluate(self, usr_choice: str):
        if usr_choice == 'q':
            self.end_program = True
            return
        
        getattr(self,usr_choice)()
        
    def start(self):
        self.end_program = False
        
        while(not self.end_program):
            usr_choice = input('-> ')
            self.evaluate(usr_choice)
        
        return
            
     
    def save(self):
        self.JTran.into_json(self.todo)
        quit()
    
    
    