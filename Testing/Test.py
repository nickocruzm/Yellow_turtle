import sys
sys.path.append('..')
from Task import Task, ToDoList
from DataManager import Manager

# dumby data
t1 = Task("task_1", "2023-10-11")
t2 = Task("task_2", "2023-11-11")
t3 = Task("task_3", "2022-09-11")

tasks = [t1,t2,t3]
todoList = ToDoList(tasks)

def test_display():
    todoList.display_all()

def test_get():
    taskName = "task_1"
    todoList.get_task(taskName)

def test_updateTags():
    todoList.update_tags("task_3", "TestData")
    

def test_Simplereading():
    man = Manager("../test.json")
    man.read()
    task_list = list( man.json_to_Task() )
    
    for t in task_list:
        print(t)

def test_readingToList():
    man = Manager("../test.json")
    man.read_to_pd()
    task_list = man.json_to_ToDoList()
    
    for t in task_list:
        print(t)









