from Headers import *

fileName = 'test.json'
data = dict()

def evaluate(choice: str):
    func = globals()[choice]
    func()
 
def update():
    with open(fileName) as jsonFile:
        new_data = json.load(jsonFile)
        Task_names = data.keys()
        
        for name_key in Task_names:
            new_data[name_key]['time']['Remaining'] = calc_remainingTime(data[name_key]['Deadline'])
    
        data.update(new_data)

    with open(fileName,'w') as jsonFile:
        json.dump(data,jsonFile,indent=4)

def calc_remainingTime(Deadline: str):
    return str(datetime.strptime(Deadline,"%Y-%m-%d") - datetime.today() )

def format_output(taskName):    
    task = data[taskName]
    line_1 = f" \t {taskName},   Deadline: {task['Deadline']} "
    line_2 = f"\t\t Remaining Time: {task['time']['Remaining']}"
    print(line_1)
    print(line_2)

def get_RemainingTime(task_key):
    return str(data[task_key]['Remaining'])

def get_task(task_name: str):
    # x = json.dumps(data[task_name],indent=4)
    format_output(task_name)

def display(data):
    for t in data:
        print(t)
    
def add():
    task_name = input("task: ")
    Deadline = input("Deadline: ")
    time_created = datetime.today()
    
    Remaining = calc_remainingTime(Deadline)
    created = str(time_created)
    
    new_data = {
        task_name:{
            "is_complete": 0,
            "Deadline": Deadline,
            "RemainingTime": Remaining,
            "Tags": []
        }
    }    
    with open(fileName,'r') as jf:
        data = json.load(jf)
        data.update(new_data)
    
    with open(fileName,'w') as jf:
        json.dump(data,jf,indent=4)

