from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from .models import *
from .models import Company as cp
import json
from django.forms.models import model_to_dict
from .jobscrapper import Scrapper, Company, Hiring
from .serializers import *
from competitive.models import *
from authority.models import Mock,Test_Series,Test_Given
def frontpage(request):
    if request.user.is_authenticated:
        context = {}
        information = Articles.objects.all().order_by('-date_Publish','-time')
        listing = List.objects.all().order_by('-date','-time')[:8]
        context['information'] = information
        context['list'] = listing
        solutions = []
        question_query = Articles.objects.filter(question_field = True).order_by('-date_Publish','-time')
        for i in question_query:
            if not Anwsers.objects.filter(question = i).exists() and len(solutions) <=10:
                solutions.append(i)
        context['question'] = solutions

        return render(request,"coding/homepage.html",context)
    else:

        return render(request,'coding/frontpage.html')

def details(request,username,title):
    context = {}
    information = get_object_or_404(Articles,title=title.replace("_"," "))

    next_issue = Articles.objects.filter(id=information.id)
    prev_issue = Articles.objects.filter(title=title.replace("_"," "), id__gt=information.id).order_by('-id').first()
    context['information'] = information
    context['next'] = next_issue
    context['prev'] = prev_issue
    post = get_object_or_404(Articles, title = title.replace("_"," "))
    comments = post.my_comments.filter(active=True,parent=None)
    if request.method == 'POST':
       
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None 
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = my_comment.objects.get(id = parent_id)
                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            name = comment_form.cleaned_data['name']
             
           
            new_comment.post.user_name2
    else:
        comment_form = CommentForm()
    context['form'] = comment_form
    context['comments'] = comments
    
    return render(request,"coding/details.html",context)

def create_post(request):
    context = {}
    if request.method == 'POST':
            
            form = Article_form(request.POST,request.FILES)
            if form.is_valid():
                ins = form.save(commit = False)
                ins.user_name2 = request.user
                ins.author = request.user
                title = form.cleaned_data['title'].replace(" ","_")
                ins.link = f'/article/{request.user}/{title}'
                
                ins.save()
                messages.success(request,f'You Article is published.')
                return HttpResponseRedirect('/')
            else:
                context['errors'] = str(form.errors)
    else:
            form = Article_form()



    context['form'] = form
        
    return render(request,'coding/create_post.html',context)



def like(request,title):
    user = request.user
    title = title.replace("_"," ").strip()
    post_obj = Articles.objects.get(title = title)
    dislikes_count = post_obj.disliked.count()
  
    if user in post_obj.liked.all():
        post_obj.liked.remove(user)
        likes = True
        count = post_obj.liked.count()
        

    else:
        post_obj.liked.add(user)
        activity_title=f"You liked Article with title {title} !!"
        activity_icon = 'fa fa-thumbs-up'
        likes = False
        count = post_obj.liked.count()
        

        
        if user in post_obj.disliked.all():
            post_obj.disliked.remove(user)
            dislikes_count = post_obj.disliked.count()
            
      

    
    return HttpResponse(json.dumps([likes,count,dislikes_count]))

def dislike(request,title):
    user = request.user
    
    title = title.replace("_"," ").strip()
  
    post_obj = Articles.objects.get(title = title)
    likes_count = post_obj.liked.count()
    if user in post_obj.disliked.all():
        post_obj.disliked.remove(user)
        dislikes = True
        count = post_obj.disliked.count()
    else:
        post_obj.disliked.add(user)
        activity_title=f"You disliked Article with title {title} !!"
        activity_icon = 'fa fa-thumbs-down'
        act = activity(user_name3 = request.user,user_activity = activity_title,activity_icon=activity_icon)
        act.save()
        dislikes = False
        count = post_obj.disliked.count()
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
            likes_count = post_obj.liked.count()
    
    return HttpResponse(json.dumps([dislikes,count,likes_count]))


def save_fav(request):
    user = request.user
    title = request.GET.get('title').replace("_"," ")
    ids = request.GET.get('id')
    tit_ins = Articles.objects.get(title = title)
    prof_ins = Profile.objects.get(user = user)
      
    if tit_ins in prof_ins.favourities.all():
            prof_ins.favourities.remove(tit_ins)
            key = True
    else:
            prof_ins.favourities.add(tit_ins)
            key = False
        

        
        
    return HttpResponse(json.dumps([key,ids]))

def bookmark(request):

    return render(request,'coding/bookmark.html')

def profile(request):
    return render(request,'coding/profile.html')

def aptitude(request):
    return render(request,'coding/aptitude.html')

def courses(request):
    return render(request,'coding/courses.html')

def ajax_syllabus(request,com,method):
    data = Syllabus.objects.get(name=cp.objects.get(company_name=com))
    context = {}
    context['company'] = com
    
    if method == 'syll':
        
        context['syllabus'] = data.syll
        context['method'] = 'Syllabus'
    else:
        context['syllabus'] = data.experience
        context['method'] = 'Interview Experience'

    return HttpResponse(json.dumps(context))
def quants(request):
    return render(request,'coding/quants.html')

def logical(request):
    return render(request,'coding/logical.html')

def verbal(request):
    return render(request,'coding/verbal.html')

def interpretation(request):
    return render(request,'coding/quants.html')


def interview(request):
    context = {}
    context['companies'] = cp.objects.all().order_by('company_name')
    return render(request,'coding/interview.html',context)


def company_syllabus(request):
    context = {}
    context['companies'] = cp.objects.all().order_by('company_name')
    context['data'] = Syllabus.objects.get(name= cp.objects.all().order_by('company_name').first()).syll
    return render(request,'coding/company_syllabus.html',context)

def mock_test(request):
    context = {}
    context['mock_data'] = Mock.objects.all().order_by('title')
    return render(request,'coding/mock_test.html',context)
def taketest(request,seriesid):
    context = {}
    test_ins = Test_Series.objects.filter(id = seriesid)
    if request.method == "POST":
        score = 0
        l = {}
        for i in test_ins[0].questions.all():
            data = request.POST.get(f'group{i.question_id}')
            l[i.question_id] = data
            if i.correct == data:
                score +=4
        instance = Test_Given(users=request.user,given = test_ins[0],score = score,solution=l)

        instance.save()

        test_ins1 = test_ins[0]
        test_ins1.subscribers.add(request.user)
        test_ins1.save()

        return HttpResponseRedirect(f'/mock_test/{test_ins[0].instance.id}')


    context['test'] = test_ins
    
    return render(request,'coding/taketest.html',context)

def series_solution(request,seriesid):
    context = {}
    instance = Test_Series.objects.get(id = seriesid)
    context['data'] = instance
    context['sol'] = eval(Test_Given.objects.get(users= request.user,given = instance ).solution)
    return render(request,'coding/series_solution.html',context)
def series(request,mockid):
    context = {}
    context['series'] = Test_Series.objects.filter(instance = Mock.objects.get(id = mockid))
    
    return render(request,'coding/test_series.html',context)
def companywise(request):
    context = {}
    context['name'] = cp.objects.all().order_by('company_name')
    return render(request,'coding/companywise.html',context)
def contribute(request):
    context = dict()
    if request.method == 'POST':
        form = Contribute(request.POST)
        if form.is_valid():
            ins = form.save()
            question = ins.question
            topic = ins.topic
            topic = str(topic).replace(" ","_")
            category = ins.category
            ids = ins.question_id
            link = f"/aptitude/{category}/questions/{topic}/#inbox{ids}"
            list_ins = List.objects.create(description = "Aptitude Question",heading = question,link = link)
            list_ins.save()
            messages.success(request,"Successfully Contributed!!")
        else:
            messages.error(request,form.errors)
    else:
        form = Contribute()
    context['form'] = form

    return render(request,'coding/contribute.html',context)

def questions(request,method,topic):
    context = {}
    print(topic)
    questions = Aptitude.objects.filter(category = Categories.objects.get(category_name = method.replace("_"," ").strip()),topic = topic.replace("_"," ").strip()).order_by('-date_Publish','-time')
    context['question'] = questions
    context['topic'] = topic.replace("_"," ")
    return render(request,'coding/questions.html',context)

def validate(request,ids,option):
    instance = get_object_or_404(Aptitude,question_id = ids)
    sol = instance.correct
    if sol == option:
        flag = True
    else:
        flag = False
    return HttpResponse(json.dumps([flag ,sol]))

def listing(request):

    context = dict()
    listing = List.objects.all().order_by('-date','-time')
    context['listing'] = listing
    
    return render(request,'coding/listing.html',context)

def hashtags(request,topic):
    context = {}
    instance = Articles.objects.all().order_by('-date_Publish','-time')
    sol = []
    for i in instance:
        data = [ a.strip(" ").capitalize() for a in i.tags.split(",")]
        if topic.replace("_"," ") in data:
            
            sol.append(i)
    context['sol'] = sol
    context['topic'] = topic


    return render(request,'coding/hashtags.html',context)

def discussion(request):
    context = dict()
    reference = ""
    if request.method == 'POST':
        
        flag = request.GET.get('flag')
        if int(flag) == 1:
            form = QuestionForm()
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                categoryform.save()
                messages.success(request,"Successfully Added!!")
            else:
                messages.error(request,categoryform.errors)
        elif int(flag) == 2:
            form = QuestionForm()
            categoryform = CategoryForm()
            question_id = request.POST.get('commentid')
            body = request.POST.get('commentbody')
            ins = Discussion_comment(post = Anwsers.objects.get(id = int(question_id)),user_discussion = request.user,body = body)
            ins.save()
            reference = f"discussion{question_id}"
            return HttpResponseRedirect(f'/discussion/#{reference}')
        elif int(flag) == 3:
            form = QuestionForm()
            categoryform = CategoryForm()
            question_id = request.POST.get('replyid')
            reply_id = request.POST.get('childid')
            body = request.POST.get('replybody')
            ins = Discussion_comment(post = Anwsers.objects.get(id = int(question_id)),user_discussion = request.user,body = body,
            parent = Discussion_comment.objects.get(id=int(reply_id)) )
            ins.save()
            reference = f"replydiscussion{reply_id}"
            return HttpResponseRedirect(f'/discussion/#{reference}')

        
        else:
            form = QuestionForm(request.POST,request.FILES)
            categoryform = CategoryForm()
            if form.is_valid():
                ins = form.save(commit = False)
                ins.user_name2 = request.user
                ins.question_field = True
                title = ins.title
                title = title.replace(" ","_")
                ins.link = f'/discussion/#{ins.id}'
                ins.save()
               
                messages.success(request,"You Successfully Posted one Question..")
            else:
                messages.error(request,form.errors)
    else:
        form = QuestionForm()
        categoryform = CategoryForm()
    questions = Articles.objects.filter(question_field = True).order_by('-date_Publish','-time')
    context['form'] = form
    context['categoryform'] = categoryform
    context['questions'] = questions
    context['categories'] = Categories.objects.all().order_by("category_name")
    



    return render(request,'coding/discussion.html',context)

def discussion_anwser(request,ques_id):
    context = {}
    ques_ins = Articles.objects.filter(id = int(ques_id))[0]
   
    if request.method == 'POST':

        form = AnwserForm(request.POST,request.FILES)
        if form.is_valid():
            ins = form.save(commit = False)
            ins.user_anwser = request.user
            ins.question = ques_ins
            sol = ins.explanation
            sentence = sol
                
            ques_ins.description = sentence
            ques_ins.save()

            ins.description = sentence
            ins.save()
            messages.success(request,"Successfully Anwsered!!")
            return HttpResponseRedirect(f'/discussion/#question{ques_id}{ins.id}')
        else:
            messages.error(request,form.errors)
    else:
        form = AnwserForm()
    context['form'] = form
    context['data'] = ques_ins
    
    

        

    return render(request,'coding/discussion_anwser.html',context)
def companies(request):
    context = {}
    if request.method == 'POST':
        job = request.POST.get('job')
        instance = Company()
        data = instance.find_information(job)
        context['data'] = data
    return render(request,'coding/companies.html',context)


def company_info(request,name):
    context = {}
    job = name

    if request.method == 'POST':
        job = request.POST.get('job')
    '''
    instance = Company()
    data = instance.find_information(job)
    context['data'] = data
    '''
    return render(request,'coding/companies.html',context)

def scrapper(request):
    context = {}
    
    hp = Hiring()
    context['data'] = hp.extract()
   
        
    return render(request,'coding/scrapper.html',context)

def show_jobs(request):
    context = {}
    company = request.GET.get('company').capitalize()
    city = request.GET.get('city').capitalize()
    if not Job_Search.objects.filter(user = request.user,title=company,location=city).exists():
        instance = Job_Search(user=request.user,title=company,location=city)
        instance.save()

    context['company'] = company
    context['city'] = city

    
    
    scraper = Scrapper()
    data = scraper.find_jobs('Indeed',company,city)
    context['data'] = data
   
    context['recent'] = Job_Search.objects.filter(user = request.user)

    return render(request,'coding/show_jobs.html',context)



def getcompanyinfo(request,company):
    instance = Company()
    data = instance.find_information(company)
    return HttpResponse(json.dumps(data))
def get_company_mcq(request,method,company,cat):
    print(method,company,cat,method.capitalize())
    context = {}
    if cat == 'all':
        questions = Aptitude.objects.filter(category = Categories.objects.get(category_name = str(method).strip()),company = cp.objects.get(company_name = company)).order_by('-date_Publish','-time')[:10]
    else:
        questions = Aptitude.objects.filter(category = Categories.objects.get(category_name = method.strip()),company = cp.objects.get(company_name = company),topic = Topic.objects.get(topic_name=cat)).order_by('-date_Publish','-time')[:10]
    l = []
    for i in questions:
        d = {}
        d['id'] = i.question_id
        d['title'] = i.question
        d['A'] = i.A
        d['B'] = i.B
        d['C'] = i.C
        d['D'] = i.D
        d['sol'] = i.correct
        d['explain'] = i.explanation
        d['topic'] = i.topic.topic_name
        l.append(d)

    
    return HttpResponse(json.dumps([l,method]))
def company(request,name):
    context = {}
    if name=="Tata Consultancy Services":
        val = "TCS"
    else:
        val = name
    context['comp'] = val
    data1 = Syllabus.objects.get(name = cp.objects.get(company_name = name))
    context['name'] = data1
    instance = Company()
    data = instance.find_information(name)
    context['data'] = data
    context['companies'] = cp.objects.all().order_by('company_name')
    sol = []
    
    for i in data1.side_data.split(","):
        sd = []
        sd.append(i)

        data = Topic.objects.filter(choice = i).order_by('topic_name')
        sd.append(data)
        sol.append(sd)
    
    context['topic'] = sol
    context['mock_data'] = Mock.objects.filter(company = cp.objects.get(company_name = name))
    return render(request,"coding/syllabus.html",context)
