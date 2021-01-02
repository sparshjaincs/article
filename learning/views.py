from django.shortcuts import render

# Create your views here.
def learning(request):
    return render(request,'learning/learning.html')
