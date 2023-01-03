from datetime import datetime

class Task:
    count = 1
    def __init__(self, name: str, deadline: str, tags=list()):
        self.id = Task.count
        self.name = name
        self.deadline = datetime.strptime(deadline,"%Y-%m-%d")
        self.remainingTime = self.deadline - datetime.today()
        self.tags = tags
        
        Task.count += 1
    
    def __str__(self):
        return f'id: {self.id}, name: {self.name}, deadline: {self.deadline}, remaining: {self.remainingTime}'
    
    
class ToDoList:
    def __init__(self, tasks=list()):
        self.Tasks = list(tasks)
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i >= len(self.Tasks):
            raise StopIteration
        
        task = self.Tasks[self.i]
        self.i += 1
        return task
    
    def display_all(self):
        for task in self.Tasks:
            print(task)
    
    def get_task(self,taskName: str):
        try:
            index = self.Tasks.index(taskName)
            return self.Tasks[index]
        except:
            print("TaskName Not Found")
        
            
            
            
        
        
    
    def create_task(self):
        task_name = input("task: ")
        Deadline = input("Deadline: ")
        new_task = Task(task_name,Deadline)
        
        self.append_task(new_task)
    
    
    def append_task(self, new_task: Task):
        self.Tasks.append(new_task)
        
        
        
    
    
