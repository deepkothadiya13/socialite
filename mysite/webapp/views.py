from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    # template = loader.get_template('webapp/login.html')
    # return HttpResponse(template)
    return render(request,'webapp/login.html')