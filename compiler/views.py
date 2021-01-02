from django.shortcuts import render
from .solve import compile
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import *
# Create your views here.
def compiler(request,file_name = 'Untitled'):
    context = {}
    context['language'] = Language.objects.all()
    if PlayGround.objects.filter(user = request.user,lang =Language.objects.all().first(),title = file_name).exists():
        ins = PlayGround.objects.get(user = request.user,lang =Language.objects.all().first(),title = file_name)
        context['instance'] = ins.code
    else:

        instance = Language.objects.all().first()
        context['instance'] = instance.template
    return render(request,'compiler/compiler.html',context)

def test(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.get('description')
        lang = request.POST.get('title')
        cp = compile()
        sol = cp.execute(data,lang)
        context['output'] = sol
    return HttpResponse(json.dumps(context))

def temp(request,id):
    context = {}
    lang = request.GET.get('lang')
    if ExtendPlay.objects.filter(instance = PlayGround.objects.get(id = id),lang = Language.objects.get(lang = lang)).exists():
        ins = ExtendPlay.objects.get(instance = PlayGround.objects.get(id = id),lang = Language.objects.get(lang = lang))
        context['instance'] = ins.code
    else:

        instance = Language.objects.get(lang = lang)
        context['instance'] = instance.template
    return HttpResponse(json.dumps(context))

def save(request,id):
    if request.method == 'POST':
        data = request.POST.get('description')
        lang = request.POST.get('title')
        if ExtendPlay.objects.filter(instance = PlayGround.objects.get(id = id),lang = Language.objects.get(lang = lang)).exists():
            ins = ExtendPlay.objects.get(instance = PlayGround.objects.get(id = id),lang = Language.objects.get(lang = lang))
            ins.code = data
            ins.save()
        else:
            instance = ExtendPlay(instance = PlayGround.objects.get(id = id),lang = Language.objects.get(lang = lang),code = data)
            instance.save()
    return HttpResponse(json.dumps('Auto Saved'))

def savefile(request,id):
    ins = PlayGround.objects.get(id = id)
    ins.title = request.GET.get('file_name')
    ins.save()
    return HttpResponse(json.dumps('Saved'))

def playground(request):
    context = {}
    context['play'] = PlayGround.objects.filter(user = request.user)
    return render(request,'compiler/playground.html',context)

def emptyplay(request,var):
    context = {}
    context['language'] = Language.objects.all()
    if var == 'empty':
        file_name = 'Untitled'
        ins = PlayGround(user = request.user,title=file_name)
        ins.save()
        context['id'] = ins.id
        instance = Language.objects.all().first()
        context['instance'] = instance.template
        context['file_name'] = 'Untitled'
    else:
        var = int(var)
        if ExtendPlay.objects.filter(instance = PlayGround.objects.get(id = var),lang = Language.objects.all().first()).exists():
            ins  =ExtendPlay.objects.get(instance = PlayGround.objects.get(id = var),lang = Language.objects.all().first())
            context['instance'] = ins.code
        else:
            instance = Language.objects.all().first()
            context['instance'] = instance.template
        context['id'] = var
        context['file_name'] = PlayGround.objects.get(id = var).title


    return render(request,'compiler/compiler.html',context)

def delete(request,id):
    ins = PlayGround.objects.get(id = id)
    ins.delete()
    return HttpResponseRedirect('/compiler/playground/')
def edit(request,id):
    if request.method == 'POST':
        ins = PlayGround.objects.get(id = id)
        val = request.POST.get('rename')
        ins.title = val
        ins.save()
    return HttpResponseRedirect('/compiler/playground/')

def html(request):
    return render(request,'compiler/frontend.html') 
def editor(request):
    return render(request,'compiler/htmleditor.html')

