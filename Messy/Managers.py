from Headers import *

# class PDManager:
#     def read_to_pd(self):
#         self.data = pd.read_json(self.fileName)

class Manager:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def load(self):
        self.convert = JSON_Translator(self.fileName)
        self.todoList = self.convert.into_ToDoList()
        
    
    def evaluate(self,choice: str):
        func = ToDoList.__dict__[choice]
        self.todoList.func()
    
    
    def save(self):
        self.convert.into_json(self.todoList)
        
        