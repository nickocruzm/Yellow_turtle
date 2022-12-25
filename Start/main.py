import json
from datetime import datetime, date

options = ["display","add","get","updateAll"]
data = dict()
fileName = "data.json"


def display():
    print(json.dumps(data,indent=4))

# ...In Progress...      
def updateAll():
    with open(fileName) as jsonFile:
        new_data = json.load(jsonFile)
        Task_names = data.keys()
        
        for name_key in Task_names:
            new_data[name_key]['RemainingTime'] = get_remainingTime(data[name_key]['Deadline'])
    
        data.update(new_data)
    
    with open(fileName,'w') as jsonFile:
        json.dump(data,jsonFile,indent=4)
    

# ...In progress...
def get_remainingTime(Deadline: str):
    return str(datetime.strptime(Deadline,"%Y-%m-%d") - datetime.today())
       
def get_task(task_name: str):
    x = json.dumps(data[task_name])
    print(x)
    
def add():
    task_name = input("task: ")
    Deadline = input("Deadline: ")
    time_created = datetime.today()
    
    RemainingTime = get_remainingTime(Deadline)
    time_created = str(time_created)
    
    new_data = {
        task_name:{
            "Deadline"     : Deadline,
            "RemainingTime": RemainingTime,
            "time_created" : time_created
        } 
    }
    
    with open(fileName,'r') as jf:
        data = json.load(jf)
        data.update(new_data)
    
    with open(fileName,'w') as jf:
        json.dump(data,jf,indent=4)


def evaluate(choice: str):
    if choice == options[0]:
        display()
    elif choice == options[1]:
        add()
    elif choice == options[2]:
        task_name = input("get, ")
        get_task(task_name)
    elif choice == options[3]:
        updateAll()
    else:
        quit()
        
    
    

if __name__ == '__main__':
    
    try:
        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
    except:
        print("error")

    
    choice = input("-> ")
    
    while(choice != 'q'):
        evaluate(choice)
        choice = input("-> ")
    
    
        
    
        