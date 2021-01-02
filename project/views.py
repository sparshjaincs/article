from django.shortcuts import render
from .models import *
# Create your views here.
def project(request):
    context = {}
    context['category'] = Category.objects.all()
    return render(request,'project/project.html',context)