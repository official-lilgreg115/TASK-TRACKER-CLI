import json
import typer


app = typer.Typer()

# TODO:
# add duplicate check in add task function - if a task already exists do not allow users to add it
# when deleting a task, seek from confirmatio from users - e.g. Do you really want to delete - sweep task?
# error handling - when adding a task if the file does not exist, create it
# general error handling
# update function, delete function, task done function - if a user enters a task name that does not exist, give feedback to the user


@app.command()
def add(name: str, status: str):
    list_check = []
    new_dictionary = {'task_name:': name, 'status': status}
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task = read_dict['task']
    for i in task:
        semi_dict = list(i.values())
        for i in semi_dict:
            list_check.append(i)
    if name in list_check:
        print('Task already exist')
    else:
        read_dict['task'].append(new_dictionary)
        print('Task added successfully')
    with open('file.json', 'w') as doc:
        json.dump(read_dict, doc)


@app.command()
def delete(name: str):
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
    for i in task_list:
        if i['task_name:'] == name:
            task_list.remove(i)
    with open('file.json', 'w') as doc:
        json.dump(read_dict, doc)


@app.command()
def update(name: str, update: str):
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
    for task in task_list:
        if task['task_name:'] == name:
            task['task_name:'] = update
    with open('file.json', 'w') as doc:
        json.dump(read_dict, doc)


@app.command()
def task_done(name: str):
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
    for i in task_list:
        if i['task_name:'] == name:
            i['status'] = 'done'
    with open('file.json', 'w') as doc:
        json.dump(read_dict, doc)


@app.command()
def list_all():
    empty_list = []
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
        for i in task_list:
            empty_list.append(i['task_name:'])
        for i in empty_list:
            print(i)


@app.command()
def list_all_done():
    empty_list = []
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
        for i in task_list:
            if i['status'] == 'done':
                empty_list.append(i['task_name:'])
        for i in empty_list:
            print(i)


@app.command()
def list_all_undone():
    empty_list = []
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
        for i in task_list:
            if i['status'] != 'done':
                empty_list.append(i['task_name:'])
        for i in empty_list:
            print(i)


@app.command()
def list_all_inprogress():
    empty_list = []
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
        task_list = read_dict['task']
        for i in task_list:
            if i['status'] == 'inprogress':
                empty_list.append(i['task_name:'])
        for i in empty_list:
            print(i)


if __name__ == "__main__":
    app()
