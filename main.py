import json
from datetime import date, datetime

class Task:
    def __init__(self,name,deadline):
        self.name = name
        self.deadline = deadline
    
    def update_daysLeft(self,days_until):
        self.daysLeft = days_until

class Task_Encoder(json.JSONEncoder):
    def default(self,obj):
        d = {"name":obj.name, "deadline":obj.deadline, "daysLeft": obj.daysLeft}
        return d
        
             
        
class Manager:
    def __init__(self,data):
        self.data = data
        self.Task_list = self.data["Tasks"]
        
        
    def set_data(self,data):
        self.data = data
    
    def add_task(self):
        name = input("Task: ")
        deadline = input("deadline: ")
    
        new_task = Task(name,deadline)
        self.Task_list.append(new_task)
    
    def calc_days_left(self, t):
        now = datetime.today()
        days_left = datetime.strptime(t.deadline, "%Y-%m-%d") - now
        t.update_daysLeft(str(days_left))
    
    def decision(self,choice):
        options = ["add task"]
        if choice == options[0]:
            self.add_task()
        # elif choice == options[1]:
            
        else:
            print("unsupported action")  
        
        
        
if __name__ == '__main__':
    
    with open('usr_data.json') as jFile:
        data = json.load(jFile)
        
    J_Man = Manager(data)
    choice = None
    
    while(choice != 'q'):
        choice = input("-> ")
        J_Man.decision(choice)
    
    
    for t in J_Man.Task_list:
        J_Man.calc_days_left(t)
        
    
    with open('usr_data.json','w') as jFile:
        json.dump(J_Man.Task_list,jFile,cls=Task_Encoder)

        

        
        
    
    
    
        
        
        
        
    
    