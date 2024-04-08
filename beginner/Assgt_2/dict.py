# 1. Write a Python program that creates a dictionary containing information about a book (title, author, ISBN).
# 2. Then later Convert the dictionary to JSON format and write it to a new JSON file.

# Part 1
import json

book_dict = {}
# I decided the values to the dictionary be input by user
title = input("Enter Book title: ")
author = input("Enter Book author: ")
isbn = input("Enter book ISBN: ")

book_dict['Title'] = title
book_dict['Author'] = author
book_dict['ISBN'] = isbn

print(book_dict)

# Part 2
path = '/home/pc/Desktop/Projects/JSON.py/beginner/Assgt_2/book.json'
with open(path, 'w') as file:
    data = json.dumps(book_dict)
    file.write(data)