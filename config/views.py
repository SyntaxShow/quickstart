from django.http import HttpResponse
def home(request):
    return HttpResponse('hello to my site')