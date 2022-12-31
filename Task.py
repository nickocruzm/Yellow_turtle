from datetime import date,datetime
class Task:
    def __init__(self, name: str, deadline: str):
        self.name = name
        self.deadline = datetime.strptime(deadline,"%Y-%m-%d")
        self.remainingTime = self.deadline - datetime.today()
        
        
    
    ##  METHODs
    
        # update method is_completed attribute 
            # record the time of completion
        
        # 




# TaskManager 
    # properties are pointing to the appropriate places in memory
    
        # time_attr = Task['Time']['RemainingTime'], Could be used to update the remaining time.
        # many more needed.
    
    # load json into a Task List
    
    # save json inot a json file