import sys
sys.path.insert(0,"/Users/nickocruz/Developer/GitHub/Yellow_turtle/Classes")
print(sys.path)
from Task import Task
from TaskList import TaskList


# dumby data
t1 = Task("task_1", "2023-10-11")
t2 = Task("task_2", "2023-11-11")
t3 = Task("task_3", "2022-09-11")

tasks = [t1,t2,t3]
todoList = TaskList(tasks)

def test_display():
    todoList.display_all()

def test_updateTags():
    todoList.update_tags("task_3", "TestData")
    

def test_Simplereading():
    man = jsonConverter("../test.json")
    man.read()
    task_list = list( man.json_to_Task() )
    
    for t in task_list:
        print(t)

def test_readingToList():
    man = jsonConverter("../test.json")
    man.read_to_pd()
    task_list = man.json_to_ToDoList()
    
    for t in task_list:
        print(t)

def test_list_to_json():
    man = jsonConverter("test.json")
    man.read_in()
    task_list = man.json_to_ToDoList()

    for t in task_list:
        print(t) 
        
    man.list_to_json(task_list)







