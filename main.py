import json
from datetime import date, datetime

class Task:
    def __init__(self,name,deadline):
        self.name = name
        self.deadline = deadline
        self.daysRemaining = ""
    
    # def daysRemaining(self,days_remaining):
    #     self.days_remaining = days_remaining
    
    def __str__(self):
        return f'name: {self.name}, deadline: {self.deadline}, remaining days: {self.daysRemaining}'

class Task_Encoder(json.JSONEncoder):
    
    def default(self,obj):
        d = {"name":obj.name, "deadline":obj.deadline, "Remaing days": obj.daysRemaining}
        return d
        
             
        
class Manager:
    def __init__(self,jsonStream):
        self.data = jsonStream
        self.Tasks = self.data["Tasks"]
             
    def set_data(self,data):
        self.data = data
    
    def add_task(self):
        name = input("Task: ")
        given_deadline = input("Deadline: ")
        
        if given_deadline == 'today':
            deadline = str(datetime.today())
        else:
            deadline = given_deadline
        
        new_task = Task(name,deadline)
        self.calculate_RemainingDays(new_task)
        self.Tasks.append(new_task)
    
    def calculate_RemainingDays(self, task):
        now = datetime.today()
        days_left = datetime.strptime(task.deadline, "%Y-%m-%d") - now
        task.daysRemaining = str(days_left)
    
    def decision(self,choice):
        options = ["add task","disp all","q"]
        
        if choice not in options:
            print("unsupported action")

        if choice == options[0]:
            self.add_task()
            
        elif choice == options[1]:
            for t in self.Tasks:
                print(t)   
        else:
            print("END")
        
        
        
if __name__ == '__main__':
    
    # Loads data from usr_data file
    
    with open('usr_data.json') as jFile:
        data = json.load(jFile)
    
    J_Man = Manager(data)
    choice = None
            
    while(choice != 'q'):
        choice = input("-> ")
        J_Man.decision(choice)
    
    # Update Tasks.daysLeft
    
    # for t in J_Man.Task_list:
    #     J_Man.calc_days_left(t)
    
    # Saves data, While loop must be broken out of else, newly added data will not be saved
    with open('usr_data.json','w') as jFile:
        json.dump(J_Man.data,jFile,indent=4,cls=Task_Encoder)

        
      
        
    
    