from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404,HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from .models import *
import json

from .jobscrapper import Scrapper

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



def like(request):
    user = request.user
    
    title = request.GET.get('title').replace("_"," ")
   
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

def dislike(request):
    user = request.user
    
    title = request.GET.get('title').replace("_"," ")
  
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

def coding(request):
    return render(request,'coding/coding.html')

def quants(request):
    return render(request,'coding/quants.html')

def logical(request):
    return render(request,'coding/logical.html')

def verbal(request):
    return render(request,'coding/verbal.html')

def interpretation(request):
    return render(request,'coding/quants.html')

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
    questions = Aptitude.objects.filter(category = Categories.objects.get(category_name = method.capitalize()),topic = topic.replace("_"," ")).order_by('-date_Publish','-time')
    context['question'] = questions
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
    
    if request.method == 'POST':
        form = QuestionForm(request.POST,request.FILES)
        categoryform = CategoryForm(request.POST)
        flag = request.GET.get('flag')
        if int(flag) == 1:
            if categoryform.is_valid():
                categoryform.save()
                messages.success(request,"Successfully Added!!")
            else:
                messages.error(request,categoryform.errors)
        else:
            if form.is_valid():
                ins = form.save(commit = False)
                ins.user_name2 = request.user
                ins.question_field = True
                title = ins.title
                title = title.replace(" ","_")
                ins.link = f'/discussion/#{title}'
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
            return HttpResponseRedirect(f'/discussion/#{ques_ins.title.replace(" ","_")}')
        else:
            messages.error(request,form.errors)
    else:
        form = AnwserForm()
    context['form'] = form
    context['data'] = ques_ins
    
    

        

    return render(request,'coding/discussion_anwser.html',context)

def scrapper(request):
    context = {}
    if request.method == 'POST':
        job = request.POST.get('job')
        location = request.POST.get('location')
        instance = Scrapper()
        data = instance.find_jobs('Indeed',job,location)
        context['jobs'] = data
        return render(request,'coding/jobs.html',context)
        
    return render(request,'coding/scrapper.html')