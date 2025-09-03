import pytest
from TaskManager import TaskManager, Task

## Task Tests
def test_init():
    task = Task("title", "description")
    assert task.status == False

def test_setStatus():
    task = Task("title", "description")
    task.setStatus(True)
    assert task.status == True


## TaskManager tests
def test_add():
    taskManager = TaskManager()
    task = Task("title", "description", False)
    taskManager.addTask(task)
    assert taskManager.tasks[task.title] == "title"

def test_remove():
    taskManager = TaskManager()
    task = Task("title", "description", False)

    taskManager.addTask(task)
    taskManager.removeTask(task.title)
    assert taskManager.tasks == {}

def test_complete():
    taskManager = TaskManager()
    task = Task("title", "description", False)
    taskManager.addTask(task)

    taskManager.completeTask(task.title)
    assert taskManager[task.title].status == True 

def add_duplicate():
    taskManager = TaskManager()
    task = Task("title", "description", False)
    taskManager.addTask(task)

    assert taskManager.addTask(task) == False

def remove_nonexistent():
    taskManager = TaskManager()
    task = Task("title", "description", False)
    taskManager.addTask(task)
    task2 = Task("title2", "description")
    assert taskManager.removeTask(task2) == False





