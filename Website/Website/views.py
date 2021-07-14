# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Ayan', 'place': 'India'}
    return render(request,'index.html',params)
    # return HttpResponse("<h1>Home</h1>")
                        # '''<h3><a href="http://127.0.0.1:8000/removepunc">
                        # Remove Punctuation Page</a></h3>'''
                        #
                        # '''<h3><a href="http://127.0.0.1:8000/capitalizefirst">
                        #                         Capitalism Page</a></h3>'''
                        #
                        # '''<h3><a href="http://127.0.0.1:8000/newlineremove">
                        #                 New Line Page</a></h3>'''
                        #
                        # '''<h3><a href="http://127.0.0.1:8000/spaceremove">
                        #                 Space Remover Page</a></h3>'''
                        # '''<h3><a href="http://127.0.0.1:8000/about">
                        #                 About Page</a></h3>'''
                        # )

def removepunc(request):
    return HttpResponse("<h1>Remove punc </h1>"
                        '''<h2><a href="/"> 
                        back</a></h2>''')

def capfirst(request):
    return HttpResponse("<h1> capitalize first </h1>"
                        '''<h2><a href="/"> 
                            back</a></h2>'''
                        )
def newlineremove(request):
    return HttpResponse("New Line Remover")
def spaceremove(request):
    return HttpResponse("Space Remover")

def about(request):
    return HttpResponse('''<h1>Hello Ayan</h1>
    <a href="https://github.com/Codee0101/De-dupe-Engine"> Our Repository</a>''')