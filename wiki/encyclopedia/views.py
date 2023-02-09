from django.shortcuts import render

from . import util
from markdown2 import Markdown

def mdTohtml(title):
    contents = util.get_entry(title)
    markdowner = Markdown()
    if contents == None:
        return None
    else:
        return markdowner.convert(contents)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    html = mdTohtml(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            "message": f"{title} does not exist in the entry."
        })
    else:
        return render(request, "encyclopedia/contents.html", {
            "contents": html,
            "title": title
        })

def search(request):
    if request.method == 'POST':
        title = request.POST['q']
        html = mdTohtml(title)
        if html == None:
            return render(request, "encyclopedia/error.html", {
                "message": f"{title} does not exist in the entry."
            })
        else:
            return render(request, "encyclopedia/contents.html", {
                "contents": html,
                "title": title
            })
    else:
        return ("encyclopedia/index.html")