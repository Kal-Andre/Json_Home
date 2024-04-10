# This program is to read the info in the json file
import json

filePath = '/home/pc/Desktop/Projects/JSON.py/beginner/data.json'
with open(filePath, 'r') as file:
    data = json.load(file)
    #print(data)

    #initializing the list where this data is gonna be stored.
    real_data = []
    for person in data['people']:
        name = person['name']
        age = person['age']
        real_data.append((name, age))
        print(real_data)
        for name, age in real_data:
            print(f"Name: {name}, Age: {age}")
        