from datetime import datetime

class Task:
    count = 1
    def __init__(self, name: str, deadline: str, tags=list(), isComplete=False):
        self.id = Task.count
        Task.count += 1
        
        self.tags = tags
        self.name = name

        self.isComplete = isComplete
        
        if ':' in deadline:
            d_list = deadline.split(' ')
            deadline = d_list[0]

        self.deadline = datetime.strptime(deadline,"%Y-%m-%d")
        self.remainingTime = self.deadline - datetime.today()
        
    def __iter__(self):
        return self
            
    def __str__(self):
        out_idName= f'id: {self.id}, name: {self.name}'
        out_time = f'deadline: {self.deadline}, remaining: {self.remainingTime}'
        out_tags = [ t for t in self.tags ]
        
        output = f'\n{out_idName}\n\t {out_time}\n\t Tags: {out_tags}\n\n'
        return output

    def add_tag(self, tag: str):
        self.tags.append(tag)
    
    def completed(self):
        self.isComplete = True
        self.completed = datetime.today()

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
    
    def getTask(self, taskName: str):
        try:
            for task in self.Tasks:
                if(task.name == taskName):
                    return task
        except:
            print("TaskName Not Found")
    
    def update_tags(self, taskName: str, new_tag: str):
        task = self.getTask(taskName)
        task.add_tag(new_tag)
         
    def create_task(self):
        task_name = input("task: ")
        Deadline = input("Deadline: ")
        new_task = Task(task_name,Deadline)
        
        self.append_task(new_task)

    def task_completed(self, taskName: str):
        t = self.getTask(taskName)
        t.completed()

    def append_task(self, new_task: Task):
        self.Tasks.append(new_task)

    def sort(self):
        Completed_Tasks = list()
        for t in self.Tasks:
            if(t.isComplete):
                Completed_Tasks.append(t)
            
            
                
            