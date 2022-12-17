import json
from datetime import date, datetime

class Task:
    def __init__(self,name,deadline):
        self.name = name
        self.deadline = deadline


        


class Manager:
    def __init__(self):
        self.Task_list = list()
        
    
    def create_task(self,name,deadline):
        new_task = Task(name,deadline)
        self.Task_list.append(new_task)
    
    def calc_days_left(self, t):
        now = datetime.today()
        
        days_left = datetime.strptime(self.deadline, %m-%d-%Y)
        
        
        
    
    
    
        
        
        
        
    
    