class Task:
    def __init__(self, title, description, status: bool = False):
        self.title = title # Unique
        self.description = description
        self.status = status  # True for complete, False for incomplete

    def setStatus(self, status):
        self.status = status

    def __repr__(self) -> str:
        string = f"Task title: {self.title} \n Description: {self.description} \n Status: {self.status}"
        return string
     
    

class TaskManager:
    def __init__(self):
        self.tasks = {}
    
    def addTask(self, task: Task) -> bool:
        if self.tasks.get(task.title, None) != None:
            return False # Task already exists
        self.tasks[task.title] = task
        return True
    

    def removeTask(self, task_title) -> bool:
        if self.tasks.get(task_title, None) == None:
            return False #Task DNE
        
        del self.tasks[task_title]
        return True
    
    def listTasks(self):
        for _, task in self.tasks.items():
            print(task)
    
    def completeTask(self, task_title) -> bool:
        if self.tasks.get(task_title, None) == None:
            return False # Task DNE
        task = self.tasks[task_title]
        task.status = True
        return True
        