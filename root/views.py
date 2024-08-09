from django.shortcuts import render
from .models import *

def home(request):
    services = Services.objects.filter(status = True)
    ss = Special_services.objects.filter(status=True)
    questions = Questions.objects.all()
    price = Pricings.objects.filter(status=True)
    trainers = Trainer.objects.filter(status=True)
    attributes = Attributes.objects.all()
    context = {
        "trainers" : trainers,
        "price" : price,
        "services" : services,
        "ss" : ss,
        "questions" : questions,
        "attributes" : attributes,

    }
    return render(request,"root/index.html", context=context)
