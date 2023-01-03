import pytest
import sys
sys.path.append('..')
from Task import Task, Todo_list

# dumby data
t1 = Task("task_1", "2023-10-11")
t2 = Task("task_2", "2023-11-11")
t3 = Task("task_3", "2022-09-11")

tasks = [t1,t2,t3]


def test_iteration():
    todo_list = Todo_list(tasks)
    for t in todo_list:
        print(t)


test_iteration()






