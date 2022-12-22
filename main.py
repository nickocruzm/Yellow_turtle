import json
from datetime import date, datetime

class Task:
    def __init__(self,name,deadline,remainingTime = ""):
        self.name = name            # name of task
        self.deadline = deadline    # deadline YYYY-MM-DD
        self.remainingTime = remainingTime # Will be empty if no arg is passed in
    
    def __str__(self):
        return f'name: {self.name}, deadline: {self.deadline}, remaining days: {self.remainingTime}'


class Task_Encoder(json.JSONEncoder):
    
    def default(self,obj):
        d = {"name":obj.name, "deadline":obj.deadline, "Remaing days": obj.remainingTime}
        return d

       
class Manager:
    def __init__(self,jsonStream):
        self.data = jsonStream
        self.Tasks = list()
        
    # Translates data from dict objects into Task objects
    def Translate_Data(self):
        for t in self.data['Tasks']:
            t = Task(t['name'], t['deadline'], t['daysLeft'])
            self.Tasks.append(t)
    
    def display_deadlines(self):
        for t in self.Tasks:
            print(t['deadline'])
        
    def add_task(self):
        name = input("Task: ")
        given_deadline = input("Deadline: ")
        
        if given_deadline == 'today':
            deadline = str(date.today())
        else:
            deadline = given_deadline
        
        new_task = Task(name,deadline)
        self.calculate_RemainingDays(new_task)
        self.Tasks.append(new_task)

    def update_remainingDays(self):
        for t in self.Tasks:
            self.calculate_RemainingDays(t)
            
    def calculate_RemainingDays(self, task):
        now = datetime.today()
        days_left = datetime.strptime(task.deadline,"%Y-%m-%d") - now
        days_remaining = str(days_left).split(',')
        time_remaining = str()
        task.remainingTime = days_remaining[0]
    
    def evaluate(self,choice):
        options = ["add task","disp all", "disp deadlines","update", "q"]
        
        if choice not in options:
            print("unsupported action")

        if choice == options[0]:
            self.add_task()
            
        elif choice == options[1]:
            for t in self.Tasks:
                print(t)
    
        elif choice == options[2]:
            self.display_deadlines()
        
        elif choice == options[3]:
            self.update_remainingDays()
            
        else:
            print("\n")
        
    
        
if __name__ == '__main__':
    
# Load data from usr_data file

    with open('usr_data.json') as savedData:
        data = json.load(savedData) # returns dict
        
# type(data) == <class 'dict'>

    manager = Manager(data)  

# Translate date from dict to Tasks  
    manager.Translate_Data()
    choice = None
            
    while(choice != 'q'):
        choice = input("-> ")
        manager.evaluate(choice)

    
# when choice == q , then data is saved
# While loop must be broken out of else, newly added data will not be saved
    with open('usr_data.json','w') as jFile:
        json.dump(manager.data,jFile,indent=4,cls=Task_Encoder)

        
      
        
    
    