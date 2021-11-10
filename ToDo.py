from datetime import datetime
import json
import os
from paths_and_data import *

task_dict = {
    'task': '',
    'priority': '',
    'date': '',
    'done': ''
}


def dict_to_file(file, dict):
    with open(file, 'w') as file:
        file.write(json.dumps(dict))


def get_tasks():
    with open(tasks_file, 'r') as file:
        tasks = json.loads(file.read())
    return tasks

command = input('Yes, Sir?')

if command == 'in':
    #task_data = input('(task <prio>) pls')
    #task, prio = task_data.split(" ")
    task, prio = "kübel", "3"

    task_dict['task'] = task
    task_dict['priority'] = prio
    task_dict['date'] = datetime.now().__str__()
    dict_to_file(task_dict)

elif command == 'out':
    print(get_tasks())








