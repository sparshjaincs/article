from django.shortcuts import render
from coding.models import *
# Create your views here.
def blogs(request):
    context = {}
    context['category'] = Categories.objects.get(category_name="Blogs")
    return render(request,'blog.html',context)