from Task import Task, ToDoList
import json

class JSON_Translator:
    def __init__(self,fileName):
        self.fileName = fileName

    def read_in(self):
        with open(self.fileName,'r') as r_jfile:
            self.data = json.load(r_jfile)

    def into_Task(self) -> Task:
        for t in self.data:
            name = t
            d = self.data[t]['deadline']
            j_Tags = list(self.data[t]['tags'])
            new_data = Task(name, d, tags=j_Tags)
            
            yield new_data
    
    def into_ToDoList(self) -> ToDoList:
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
            self.read_in()
            self.json_to_Task(self)

    def into_json(self, todos: ToDoList):
        with open(self.fileName,'r') as rf:
            data = json.load(rf)
            for t in todos:
                task = {
                    t.name:{
                        "id": t.id,
                        "isComplete": False,
                        "completed" : None,
                        "deadline":str(t.deadline),
                        "remainingTime":str(t.remainingTime),
                        "tags": t.tags
                        
                    } 
                }
                if(t.isComplete):
                    task[t.name]['isComplete'] = True
                    task[t.name]['completed'] = t.completed
                
                data.update(task)
        
        with open(self.fileName,'w') as wf:
            json.dump(data,wf,indent=4)