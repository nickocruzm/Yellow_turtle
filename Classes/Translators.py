from Task import Task
from TaskList import TaskList
import json

class JSON_Decoder:
    def json_to_TaskList(self,fileName: str) -> TaskList:
        
        with open(fileName, 'r') as readFile:
            data = json.load(readFile)
        
        tasks = list()
        try:
            for t in data:
                name = t
                d = data[t]['deadline'] # change, need to get keys dynamically.
                j_Tags = list(data[t]['tags'])
                new_data = Task(name, d, tags=j_Tags) 
                tasks.append(new_data)   
            return TaskList(tasks)
        
        except:
            print("exception raised")
            self.read_in()
            self.json_to_Task(self)
    
    def into_Task(self) -> Task:
        for t in self.data:
            name = t
            d = self.data[t]['deadline']
            j_Tags = list(self.data[t]['tags'])
            new_data = Task(name, d, tags=j_Tags)
            
            yield new_data
    

class JSON_Encoder:
    def Tasks_to_json(self, fileName: str, taskList: TaskList):
        with open(fileName,'r') as rf:
            data = json.load(rf)
            for t in taskList:
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



