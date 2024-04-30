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

# for total number of books
total = len(books)
print(total)

# average year of publication
    # we used list comprehension to attain the year values.
years = [book['Year'] for book in books]
print(years)

total_sum = sum(years)
avg = total_sum/total
print(int(avg))