'''JSON Data Processing.
This is a program that reads JSON Data from the file, BookData.json containing information about books
(title, author, year & ISBN) and prints a summary, such as total number of books, the average publication year.'''

import json

path2json = "/home/pc/Desktop/Projects/JSON.py/beginner/Assignment3/BookData.json"

# Loading the reading the json data
with open(path2json, "r") as file:
    bookInfo = json.load(file)

# JSON key 'Books' represented in a list.
books = bookInfo['Books']

for book in books:
    print(book)