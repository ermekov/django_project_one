from django.shortcuts import render

def index(request):
    data={
        'title':"Басты Бет"
    }
    return render(request,'main/index.html',data )

def about(request):
    return render(request,'main/about.html')