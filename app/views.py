from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def htmlform(request):
    if request.method=='POST':
        name=request.POST['un']
        return HttpResponse(name)
        #Topic.objects.get_or_create(topic_name=name)[0]

    return render(request,'htmlform.html')

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST.get('topic')
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        t.save()
        return HttpResponse('topic is inserted successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST.get('url')
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        return HttpResponse('Webpage is inserted ')
    return render(request,'insert_webpage.html',d)

def select_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        select_topic=request.POST.getlist('selected_topic')
        #print(select_topic)
        webpages=Webpage.objects.none()
        for i in select_topic:
            webpages=webpages|Webpage.objects.filter(topic_name=i)

        d1={'webpages':webpages}
        return render(request,'display_webpage.html',d1)
    
    return render(request,'select_webpage.html',d)

def checkbox(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'checkbox.html',d)