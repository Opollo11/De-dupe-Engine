# I have created this file
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Hello Ayan</h1> 
    <a href="https://github.com/Codee0101/De-dupe-Engine"> Our Repository</a>''')

def about(request):
    return HttpResponse("About Ayan")