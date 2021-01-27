import web
import requests
import json

render = web.template.render('mvc/')

class Index:

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        book = form.book
        result = requests.get('https://www.googleapis.com/books/v1/volumes?q='+book)
        books = result.json()
        items = books["items"]
        x = items[3]
        coded = json.dumps(x)
        decoded = json.loads(coded)

        link = "<a target='blank' href='"+decoded["volumeInfo"]["infoLink"]+"'>"+book+"</a>"

        return link
