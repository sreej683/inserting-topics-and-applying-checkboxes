from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.


def htmlforms(request):
    if request.method=='POST':
        return HttpResponse('Post is created')
    return render(request,'htmlforms.html')




def insert_topic(request):
    if request.method=='POST':
        topic_name=request.POST['topic']
        to=Topic.objects.get_or_create(topic_name=topic_name)[0]
        to.save()
        return HttpResponse('Topic is created')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        topic_name=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        tn=Topic.objects.get(topic_name=topic_name)
        wo=WebPage.objects.get_or_create(topic_name=tn,name=name,url=url,email=email)[0]
        wo.save()
        return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    WTO=WebPage.objects.all()
    d={'WTO':WTO}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        w=WebPage.objects.get(id=name)
        ato=AccessRecord.objects.get_or_create(name=w,author=author,date=date)[0]
        ato.save()
        return HttpResponse("AccessRecord is created")
    return render(request,'insert_accessrecord.html',d)




def select_topic(request):
    wo=Topic.objects.all()
    d={'wo':wo}
    if request.method=='POST':
        topics=request.POST.getlist('topics')
        webpages=WebPage.objects.none()
        for tn in topics:
            webpages=webpages|WebPage.objects.filter(topic_name=tn)
        d1={'webpages':webpages}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_topic.html',d)



def checkbox(request):
    wo=Topic.objects.all()
    d={'wo':wo}
    return render(request,'checkbox.html',d)



def update_webpage(request):
    WebPage.objects.filter(name='yash').update(email='yashjai@gmail.com')
    WebPage.objects.filter(topic_name='volleyball').update(email='lasyashree@gmail.com')
    WebPage.objects.update_or_create(name='vansh',defaults={'url':'https://vansh.com'})
    WebPage.objects.update_or_create(name='vansh',defaults={'email':'valeriya@gmail.com'})
    CTO=Topic.objects.get(topic_name='football')
    WebPage.objects.update_or_create(name='yash',defaults={'topic_name':CTO})
    WebPage.objects.update_or_create(name='shree',defaults={'url':'https://shree.com','topic_name':CTO})
    return HttpResponse('updated successfully')


'''webpages=WebPage.objects.all()
d1={'webpages':webpages}
return render(request,'display_webpage.html',d1)'''


def delete_webpage(request):
    WebPage.objects.filter(name='shree').delete()
    WebPage.objects.all().delete()
    webpages=WebPage.objects.all()
    d1={'webpages':webpages}
    return render(request,'display_webpage.html',d1)