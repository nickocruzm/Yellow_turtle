import json
from datetime import datetime, date

options = ["display","add","get","update","completed"]
data = dict()
fileName = "data.json"


# ------------------------   BackEnd    -----------------------------------------------------

def evaluate(choice: str):
    if choice == options[0]:
        display()
    elif choice == options[1]:
        add()
    elif choice == options[2]:
        task_name = input("\t ")
        get_task(task_name)
    elif choice == options[3]:
        updateAll()
    elif choice == options[4]:
        pass
    else:
        print(f'{choice} is not supported')
        print('\t',options)
 
def updateAll():
    with open(fileName) as jsonFile:
        new_data = json.load(jsonFile)
        Task_names = data.keys()
        
        
        for name_key in Task_names:
            new_data[name_key]['Remaining'] = calc_remainingTime(data[name_key]['Deadline'])
    
        data.update(new_data)

    with open(fileName,'w') as jsonFile:
        json.dump(data,jsonFile,indent=4)

def calc_remainingTime(Deadline: str):
    return str(datetime.strptime(Deadline,"%Y-%m-%d") - datetime.today() )

#TODO: define
def get_timeCompleted(taskName):
    pass

def format_output(taskName):    
    task = data[taskName]
    line_1 = f" \t {taskName},   Deadline: {task['Deadline']} "
    line_2 = f"\t\t Remaining Time: {task['time']['Remaining']}"
    print(line_1)
    print(line_2)


# ------------------------- users choices --------------------------------------------------

def get_RemainingTime(task_key):
    return str(data[task_key]['Remaining'])

def get_task(task_name: str):
    x = json.dumps(data[task_name],indent=4)
    format_output(task_name)
        
def display():
    for key in data.keys():
        format_output(key)
    
def add():
    task_name = input("task: ")
    Deadline = input("Deadline: ")
    time_created = datetime.today()
    
    Remaining = calc_remainingTime(Deadline)
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
                "Remaining": Remaining,
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
        updateAll()
    except Exception as e:
        print(e)

    
    choice = input("-> ")
    print("\n")
    while(choice != 'q'):
        evaluate(choice)
        choice = input("-> ")
    
    
        
    
