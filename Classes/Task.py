from datetime import datetime

class Task:
    count = 1
    def __init__(self, name: str, deadline: str, tags=list(), isComplete=False):
        self.name = name
        self.id = Task.count
        Task.count += 1
        
        self.tags = tags

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
        self.completed = str(datetime.today())

            
            
                
            