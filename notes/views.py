from django.shortcuts import render
from .forms import *
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
def notebook(request):

    context = {}
    if request.method == 'POST':
        form = Notes_form(request.POST)
        if form.is_valid():
            ins = form.save(commit= False)
            ins.username = request.user
            ins.save()
            messages.success(request,"Created Successfully")
        else:
            messages.error(request,form.errors)
    else:
        form = Notes_form()
    context['form'] = form

    return render(request,'notes/notebook.html',context)

def delete(request,id):
    ins = Note.objects.get(id = id)
    ins.delete()
    return HttpResponseRedirect("/notebook/")

def edit(request,id):
    context = {}
    if request.method == 'POST':
        form = Notes_form(request.POST)
        if form.is_valid():
            data = Note.objects.get(id = id)
            data.delete()
            ins = form.save(commit= False)
            ins.username = request.user
            ins.save()
            messages.success(request,"Created Successfully")
            return HttpResponseRedirect("/notebook/")
        else:
            messages.error(request,form.errors)
    else:
        data = Note.objects.get(id = id)
        dictionary = {
            'heading' : data.heading,
            'text': data.text
        }
        form = Notes_form(initial = dictionary)
    context['form'] = form
    context['edit'] = True

    return render(request,'notes/notebook.html',context)
