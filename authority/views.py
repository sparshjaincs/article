from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import HttpResponse,HttpResponseRedirect
# Create your views here.
def overview(request):
    return render(request,'authority/admin.html')

def create_mock(request):
    context = {}
    if request.method == 'POST':
        form = Mock_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(request,form.errors)
    form = Mock_Form()
    context['form'] = form
    context['mock_data'] = Mock.objects.all().order_by('title')
    return render(request,'authority/create_mock.html',context)

def add_questions(request,id,company):
    context = {}
    
    #Test_Series.objects.filter(instance = Mock.objects.get(id = id))
    
    if request.method == 'POST':
        form = Series_Form(request.POST,request.FILES)
        selected_values = request.POST.getlist('list')
        
        if form.is_valid():
            ins = form.save(commit = False)
            ins.instance = Mock.objects.get(id = id)
            
            ins.save()
            ids = ins.id
            myins = Test_Series.objects.get(id = ids)
            for i in selected_values:
                myins.questions.add(Aptitude.objects.get(question_id = int(i)))
            myins.save()
        else:
            pass
    form = Series_Form()
    context['form'] = form
    apt_ins =  Aptitude.objects.filter(company = Company.objects.get(company_name = company))
    test_ins = Test_Series.objects.filter(instance = Mock.objects.get(id = id))
    dat = test_ins.values('questions')
    l = []
    for i in dat:
        if i:
            if i['questions'] not in l:
                l.append(i['questions'])

    data = []
    for i in apt_ins:
        if i.question_id not in l:
            data.append(i)

    context['data'] = data
    context['series'] = test_ins
    context['id'] = id
    context['company'] = company
    return render(request,'authority/add_questions.html',context)

def delete_series(request,id,company,series):
    ins = Test_Series.objects.get(id= int(series))
    ins.delete()
    return HttpResponseRedirect(f'/superuser/create_mock/{id}/{company}/')