from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    data={
        'title':'Home Page'
    }
    return render(request,"index.html",data)


from django.http import HttpResponse
def aboutus(request):
    return HttpResponse("welcome to django")
def course(request):
    return HttpResponse("welcome to python")
def courseDetails(request,courseid):
    return HttpResponse(courseid)