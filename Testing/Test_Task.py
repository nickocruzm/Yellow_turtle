from Classes.Task import Task

x_tags = ['tag1','tag2','tag3']
x_task = Task("TestTask", "2023-02-14",tags=x_tags)
a_task = Task("a","2023-02-14")

def test_deadline_arg():
    pass
    
def test_tags_arg():
    assert x_task.tags == x_tags

def test_add_tag():
    new_tag = "tag4"
    x_task.add_tag(new_tag)
    assert x_task.tags == ['tag1','tag2','tag3','tag4']

    
    