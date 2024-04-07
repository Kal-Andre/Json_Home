import json

filePath = '/home/pc/Desktop/Projects/JSON.py/beginner/data.json'
with open(filePath, 'r') as file:
    data = json.load(file)
    #print(data)

    real_data = []
    for person in data['people']:
        name = person['name']
        age = person['age']
        real_data.append((name, age))

        for name, age in real_data:
            print(f"Name: {name}, Age: {age}")
        