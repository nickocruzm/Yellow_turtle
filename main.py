import json
from datetime import datetime, date

options = ["displayAll","add","get task"]
data = dict()
fileName = "Yellow_turtle/data.json"


# ------------------------   BackEnd    -----------------------------------------------------



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
 
def updateAll():
    with open(fileName) as jsonFile:
        new_data = json.load(jsonFile)
        Task_names = data.keys()
        
        for name_key in Task_names:
            new_data[name_key]['time']['Remaining'] = calc_remainingTime(data[name_key]['Deadline'])
    
        data.update(new_data)
    
    with open(fileName,'w') as jsonFile:
        json.dump(data,jsonFile,indent=4)

def calc_remainingTime(Deadline: str):
    return str( datetime.strptime(Deadline,"%Y-%m-%d") - datetime.today() )

def get_timeCompleted(taskName):
    pass

# in progress
def format_output(taskName):
    if(data[taskName]["time"]["completed"]):
        completed_time = get_timeCompleted(taskName)
    else:
        completed_time = "not yet complete"
    
    
    task = data[taskName]
    print(taskName, ": ")
    print("\t Deadline:", task['Deadline'])
    print("\t Remaining Time:", task["time"]['Remaining'], " days")

# ------------------------- users choices --------------------------------------------------

def get_RemainingTime(task_key):
    return str(data[task_key]['Remaining']) + " days"

def get_task(task_name: str):
    x = json.dumps(data[task_name],indent=4)
    format_output(task_name)
        
def display():
    print(json.dumps(data,indent=4))
    
def add():
    task_name = input("task: ")
    Deadline = input("Deadline: ")
    time_created = datetime.today()
    
    Remaining = calc_remainingTime(Deadline).split()
    created = str(time_created)
    print(created)
    
    new_data = {
        task_name:{
            
            "Deadline" : Deadline,
            
            "time": { 
                "created"  : {
                    'Year' : time_created.year,
                    'Month': time_created.month,
                    'Day'  : time_created.day,
                    'Hours': time_created.hour,
                    'Minutes': time_created.minute
                },
                "Remaining": Remaining[0], 
                "completed": 0
            }
        }
    }
    
    
    with open(fileName,'r') as jf:
        data = json.load(jf)
        data.update(new_data)
    
    with open(fileName,'w') as jf:
        json.dump(data,jf,indent=4)


#--------------------------interface --------------------------------------------------------

if __name__ == '__main__':
    
    try:
        with open('data.json') as jsonFile:
            data = json.load(jsonFile)
    except Exception as e:
        print(e)

    
    choice = input("-> ")
    
    while(choice != 'q'):
        evaluate(choice)
        choice = input("-> ")
    
    
        
    
        