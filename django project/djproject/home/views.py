from django.shortcuts import render
from django.http import HttpResponse
from .forms import Bookingform
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def index(request):
    if request.method == "POST":
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Your enquiry has been submitted. We'll get back to you within 24 hours.")
            return redirect('home')
    else:
        form = Bookingform()
    return render(request, 'index.html', {'form': form})



