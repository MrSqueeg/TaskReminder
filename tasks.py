import menu
import csv
import datetime

task_list = []
tasks_file = "tasks.csv"

class task:
    name = None
    desc = None
    due = None

def list_tasks():
    for task in task_list:
        print(f'Name: {task.name}, Desc: {task.desc}, Due: {task.due}')

def add_task(name, desc, due):
    # Check correct date format
    try:
        datetime.datetime.strptime(due, "%Y-%m-%d-%H")
    except ValueError:
        print("Invalid date format")
        return

    with open(tasks_file, 'r+', newline='') as infile:
        fields = ['name', 'desc', 'due']

        writer = csv.DictWriter(infile, fieldnames=fields)

        # If Empty file write csv header / fields
        csv_dict = [row for row in csv.DictReader(infile)]
        if len(csv_dict) == 0:
            writer.writeheader()
            
        writer.writerow({'name': name, 'desc': desc, 'due': due}) # Add to file

    new_task = task()
    new_task.name = name
    new_task.desc = desc
    new_task.due = due

    task_list.append(new_task) # Add to list / cache

    print(f'Added task: {name}')

def load_tasks():
    with open(tasks_file, newline='') as infile:
        reader = csv.DictReader(infile)
        next(reader, None)
        for row in reader:
            new_task = task()
            new_task.name = row['name']
            new_task.desc = row['desc']
            new_task.due = row['due']

            task_list.append(new_task)   