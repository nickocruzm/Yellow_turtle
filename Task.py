from datetime import datetime
class Task:
    count = 0
    def __init__(self, name: str, deadline: str, tags: list()):
        self.name = name
        self.deadline = datetime.strptime(deadline,"%Y-%m-%d")
        self.remainingTime = self.deadline - datetime.today()
        self.tags = tags
        global count
        count += 1
    
    def __str__(self):
        return f'{self.name}, {self.deadline}, {self.remainingTime}'

 

    

# TaskManager
    # properties are pointing to the appropriate places in memory
    
        # time_attr = Task['Time']['RemainingTime'], Could be used to update the remaining time.
        # many more needed.
    
