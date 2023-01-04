import sys
from datetime import datetime
import pandas as pd
from Task import Task



class Manager:
    def __init__(self,fileName):
        self.fileName = fileName
    
    def read(self):
        self.data = pd.read_json(self.fileName)
        type(self.data)
        
        
    def data_to_Task(self) -> Task:
        for t in self.data:
            name = t
            d = self.data[t]['deadline']
            j_Tags = list(self.data[t]['tags'])
            new_data = Task(name, d, tags=j_Tags)
            
            yield new_data
            




    



