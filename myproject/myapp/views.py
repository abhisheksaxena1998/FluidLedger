from os import stat
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.serializers import serialize
import json

# Create your views here.

def error_404_view(request, exception):
    return render(request,'404.html')

def server(request):
    return HttpResponse("Server has started")

def index(request):
    mydictionary = {
        "posts" : Post.objects.all(),
        "message" : "Welcome To The Homepage"
    }
    return render(request,'index.html',context=mydictionary)

def search(request):
    query = request.GET['query']
    mydictionary = {
        "posts" : Post.objects.all().filter(Q(title__icontains=query)
        ).order_by('-date'),
        "message" : "Search Results"
    }
    return render(request,'index.html',context=mydictionary)

def about(request):
    return render(request,'about.html')

def userfeedbackform(request):
    return render(request,'userfeedbackform.html')
    

@login_required
def addtofavourite(request,username,pid):
    obj = Favourite()
    obj.username = username
    obj.pid = pid
    obj.posttitle = Post.objects.get(id=pid).title
    obj.save()
    mydictionary ={
        "add" : True,
        "favourites" : Favourite.objects.filter(username=username)
    }
    return render(request,'favourite.html',context=mydictionary)
   
@login_required
def getfavourite(request,username):
    mydictionary ={
        "favourites" : Favourite.objects.filter(username=username)
    }
    return render(request,'favourite.html',context=mydictionary)

def submituserfeedbackform(request):
    if request.method == 'GET':
        obj = UserFeedback()
        obj.subject = request.GET['title']
        obj.feedback = request.GET['subject']
        obj.save()
    mydictionary = {
        "feedback" : True
    }
    return render(request,'userfeedbackform.html',context=mydictionary)


def groupmembers(request):
    return render(request,'groupmembers.html')


def emergency(request):
    return render(request,'emergency.html')

def detaileduser(request):
    return render(request,'detailregister.html')

def submitdetaileduser(request):
    user = DetailedUser()
    user.name = request.POST["name"]
    user.age = request.POST["age"]
    user.country = request.POST["country"]
    user.whatsapp = request.POST["phone"]
    user.gender = request.POST["gender"]
    user.role = request.POST["role"]
    user.recent = request.POST["recent"]
    user.frequent = request.POST["frequent"]
    user.monetary = request.POST["monetary"]
    user.time =  request.POST["time"]
    user.latitude = request.POST["latitude"]
    user.longitude = request.POST["longitude"]
    user.bloodgroup = request.POST["bloodgroup"]
    user.save()
    return render(request,'detailregister.html',{
        "message" : "Registered Successfully"
        })

def canBeDonatedByMethod(bloodgroup):
    d = {
    "A" : ["A+","A-","O+","O-"],
    "A-" : ["A-","O-"],
    "B+" : ["B+","B-","O+","O-"],
    "B-" : ["B-","O-"],
    "O+" : ["O+","O-"],
    "O-" : ["O-"],
    "AB+" : ["A+","A-","B+","B-","AB+","AB-","O+","O-"] ,
    "AB-" : ["AB-","A-","B-","O-"]
    }
    return d[bloodgroup]

def predict(request):
    import reverse_geocode
    import joblib
    import reverse_geocoder as rg

    allusers = list(DetailedUser.objects.all())
    print(allusers)
    for user in allusers:
        cred = [user.recent,user.frequent,user.monetary,user.time]
        coordinates = (user.latitude,user.longitude)
        #print (rg.search(coordinates)[0]['name'], rg.search(coordinates)[0]['admin1'])
        mydict = {
                        "query" : f"{coordinates[0]},{coordinates[1]}",
                        "city" : rg.search(coordinates)[0]['name'],
                        "state" : rg.search(coordinates)[0]['admin1']
                    }
        filename = 'donationpredictor.sav'
        loaded_model = joblib.load(filename)
        arg=loaded_model.predict([cred])[0]
        if arg==1:
            status=f"High probability of donation from {mydict['city']} city, {mydict['state']}"
        else:
            status=f"Low probability of donation from {mydict['city']} city, {mydict['state']}"

        print(status)
    return HttpResponse("end")

    



def matchAlgorithm(currentuser,allusers):
    canBeDonatedBy = canBeDonatedByMethod(currentuser.bloodgroup)
    matchedusers = []
    donor = ["Donor","DONOR","donor"]
    for user in allusers:
        if user.bloodgroup in canBeDonatedBy and user.username != currentuser.username and (user.role in donor):
            matchedusers.append(user)
    return matchedusers


def mydetails(request,requestname):
    try:
        currentuser = DetailedUser.objects.filter(username=requestname).first()
        allusers = list(DetailedUser.objects.all())
        matchedusers = matchAlgorithm(currentuser,allusers)
        return render(request,'mydetails.html',{
            "currentuser" : currentuser,
            "matchedusers" : matchedusers
            })
    except:
        return render(request,'detailregister.html')

def makepost(request):
    return render(request,'post.html')

def submitpost(request):
    obj = Post()
    obj.username = request.POST['username']
    obj.title = request.POST['title']
    obj.description = request.POST['description']
    obj.save()
    return render(request,'post.html',{
        "message" : "Posted Successfully"
        })

def api(request):
    users = list(DetailedUser.objects.all().values())
    return JsonResponse({
        "users" : users
        })

def vieweditdetails(request,requestname):
    currentuser = DetailedUser.objects.filter(username=requestname).first()
    return render(request,'detailregister.html',context={
        'currentuser' : currentuser
        })

def track(request):
    return render(request,'track.html')