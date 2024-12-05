import menu
import csv
import datetime

tasks_file = "tasks.csv"

class Task_node:
    def __init__(self):
        self.name = None
        self.desc = None
        self.due = None
        self.next = None

class Task_list:
    def __init__(self):
        self.head = None

    def add_to_list(self, to_add: Task_node):
        temp = self.head
        self.head = to_add
        self.head.next = temp

    def remove_task(self, name: str):
        curr = self.head
        prev = curr
        while curr:
            if curr.name == name:
                prev.next = curr.next
                del curr
                curr = None
            else:
                prev = curr
                curr = curr.next

task_list = Task_list()

def list_tasks():
    curr = task_list.head
    while curr:
        print(f'Name: {curr.name}, Desc: {curr.desc}, Due: {curr.due}')
        curr = curr.next

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

    new_task = Task_node
    new_task.name = name
    new_task.desc = desc
    new_task.due = due

    task_list.add_to_list(new_task) # Add to list / cache

    print(f'Added task: {name}')

def load_tasks():
    with open(tasks_file, 'a+', newline='') as infile:
        reader = csv.DictReader(infile)
        next(reader, None)
        for row in reader:
            new_task = Task_node()
            new_task.name = row['name']
            new_task.desc = row['desc']
            new_task.due = row['due']

            task_list.add_to_list(new_task)