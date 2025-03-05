import json
def add(name: str, status: str):
    list_check =[]
    new_dictionary = {'task_name:': name, 'status': status}
    with open('file.json', 'r') as doc:
        read_dict = json.load(doc)
    task=read_dict['task']

    for i in task:
        semi_dict = list(i.values())
        for i in semi_dict:
            list_check.append(i)
    if name in list_check:
        print('found')
    print(list_check)    
       

add('name','hi')