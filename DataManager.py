import sys
from datetime import datetime
import pandas as pd
import json
from Task import Task,ToDoList



class Manager:
    def __init__(self,fileName):
        self.fileName = fileName
    
    # Managing the Load process 
    def read_to_default(self):
        with open(self.fileName,'r') as r_jfile:
            self.data = json.load(r_jfile)
            
    def read_to_pd(self):
        self.data = pd.read_json(self.fileName)
        
        
    def json_to_Task(self) -> Task:
        for t in self.data:
            name = t
            d = self.data[t]['deadline']
            j_Tags = list(self.data[t]['tags'])
            new_data = Task(name, d, tags=j_Tags)
            
            yield new_data
            
    def json_to_ToDoList(self) -> ToDoList:
        tasks = list()
        try:
            for t in self.data:
                name = t
                d = self.data[t]['deadline']
                j_Tags = list(self.data[t]['tags'])
                new_data = Task(name, d, tags=j_Tags)
                
                tasks.append(new_data)
            
            return ToDoList(tasks)
        
        except NameError:
            self.read()
            self.json_to_Task(self)
    
    
    def list_to_json(self, todos: ToDoList):
        with open(self.fileName,'r') as rf:
            data = json.load(rf)
            for t in todos:
                task = {
                    t.name:{
                        "id": t.id,
                        "isComplete": t.isComplete,
                        "deadline":str(t.deadline),
                        "RemainingTime":str(t.remainingTime),
                        "tags": t.tags
                    } 
                }
                data.update(task)
        
        with open(self.fileName,'w') as wf:
            json.dump(data,wf,indent=4)
        
    
        
man = Manager("test.json")
man.read_to_default()
task_list = man.json_to_ToDoList()

for t in task_list:
    print(t) 
    
man.list_to_json(task_list)
            




