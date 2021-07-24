# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    params = {'name': 'Ayan', 'place': 'India'}
    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    params = {'analyzed_text': ''}
    if removepunc == "off":
        params['analyzed_text'] = djtext
    else:
        params['analyzed_text'] = re.sub(r'[^\w\s]', '', djtext)
    print(djtext)

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("<h1> capitalize first </h1>"
#                         '''<h2><a href="/">
#                             back</a></h2>'''
#                         )
# def newlineremove(request):
#     return HttpResponse("New Line Remover")
# def spaceremove(request):
#     return HttpResponse("Space Remover")
#
# def about(request):
#     return HttpResponse('''<h1>Hello Ayan</h1>
#     <a href="https://github.com/Codee0101/De-dupe-Engine"> Our Repository</a>''')
