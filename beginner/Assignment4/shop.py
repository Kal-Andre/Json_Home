'''JSON Data Searcher. 
This is a Python program that reads a JSON file containing a list of products (name, price, category, etc.) 
and allows the user to search for products by name or category.'''

import json
# Path
path2json = "/home/pc/Desktop/Projects/JSON.py/beginner/Assignment4/product.json"

# Load JSON to Python
with open(path2json, "r") as file:
    prodInfo = json.load(file)

products = prodInfo['products']

#print(products)

# The search: We Will most definitely use the linear search
def lin_search(myList, target):
    for i in range(len(myList)):
        if myList[i]['name'] == target:
            return i
    return -1
search_term = input("Search by name: ")

index = lin_search(products, search_term)
print(index)

if index != -1:
    print(f"Product '{search_term}' found at index {index}")
    print("Product Details:")
    print(products[index])
else:
    print(f"Product '{search_term}' not found.")