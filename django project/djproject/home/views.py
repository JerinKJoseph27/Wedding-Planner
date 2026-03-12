from django.shortcuts import render
from django.http import HttpResponse
from .forms import Bookingform

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
    form=Bookingform()
    dict_form={
        'form' : form
    }
    return render(request, 'index.html', dict_form)



