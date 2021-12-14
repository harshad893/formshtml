from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def htmlform(request):
    if request.method=='POST':
        name=request.POST['un']
        #return HttpResponse(name)
        Topic.objects.get_or_create(topic_name=name)[0]

    return render(request,'htmlform.html')