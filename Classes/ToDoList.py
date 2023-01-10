import Task
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