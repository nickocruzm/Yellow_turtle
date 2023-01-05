import sys
sys.path.append('..')
from Task import Task,ToDoList

t1 = Task("task_1", "2023-10-11")
t2 = Task("task_2", "2023-11-11")
t3 = Task("task_3", "2022-09-11")

tasks = [t1,t2,t3]
todoList = ToDoList(tasks)

def test_getTask():
    assert todoList.getTask('task_2') == t2