import requests
import json

result = requests.get('https://www.googleapis.com/books/v1/volumes?q=harry+potter')
print(result.status_code)
# print(result.text)

books = result.json()
print(type(books))

items = books["items"]

x = items[3]

coded = json.dumps(x)
decoded = json.loads(coded)

print(decoded["volumeInfo"]["infoLink"])

