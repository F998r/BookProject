from django.shortcuts import render

def index(request):
    context = {
        'course' : 'Web Technology'
    }
    return render(request, 'bookmodule/index.html',context)
