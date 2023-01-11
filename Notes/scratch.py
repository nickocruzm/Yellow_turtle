from datetime import datetime
import sys
sys.path.insert(0,"/Users/nickocruz/Developer/GitHub/Yellow_turtle/Classes")
from Task import Task

a = "word"
b = ""
def func(x: str):
    if(x):
        print(x)
    else:  
        print("else executed")
        
    print("after conditions")


d1 = {"name": "task_z", "deadline":"2023-09-12"}

print(d1)

# print(datetime.today().strftime("%m/%d/%Y"))
# print(datetime.now())
    
# d = "2023-10-14"

# print(datetime.strptime(d,"%Y-%m-%d").strftime("%m-%d-%Y"))





