import Task
class TaskList:
    def __init__(self, tasks=list()):
        self.items = list(tasks)

    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i >= len(self.items):
            raise StopIteration
        
        task = self.items[self.i]
        self.i += 1
        return task
    
    def display_all(self):
        for task in self.items:
            print(task)
    
    def getTask(self, taskName: str):
        try:
            for task in self.items:
                if(task.name == taskName):
                    return task
        except:
            print("TaskName Not Found")
            self.create_task(taskName)
    
    def update_tags(self, taskName: str, new_tag: str):
        task = self.getTask(taskName)
        task.add_tag(new_tag)
         
    def create_task(self,taskName: str):
        if(taskName):
            deadline = input("deadline: ")
        else:
            taskName = input("name: ")
            deadline = input("deadline: ")

        new_task = Task(taskName,deadline)
        self.append_task(new_task)

    def task_completed(self, taskName: str):
        t = self.getTask(taskName)
        t.completed()

    def append_task(self, new_task: Task):
        self.items.append(new_task)

    def sort(self):
        Completed_Tasks = list()
        for t in self.items:
            if(t.isComplete):
                Completed_Tasks.append(t)