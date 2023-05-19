from django.shortcuts import render
from website.models import Contact
from website.forms import ConatctForm, NewsLetterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ConatctForm(request.POST)
        if form.is_valid():
           form.save()
           messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'Your ticket didnt submit correctly')
    form = ConatctForm()
    return render(request, 'website/contact.html',{'form':form})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
           form.save()
    form = ConatctForm()
    return render(request, 'website/index.html')

def test(request):
    if request.method == 'POST':
        form = ConatctForm(request.POST)
        if form.is_valid():
           form.save()
    form = ConatctForm()
    return render(request, 'test.html',{'form':form})