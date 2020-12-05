from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def submitresponse(request):
	user = User()
	user.name = request.POST["username"]
	user.age = request.POST["userage"]
	user.location = request.POST["userlocation"]
	user.contact = request.POST["usercontact"]
	user.gender = request.POST["gender"]
	user.bloodgroup = request.POST["bloodgroup"]
	user.preference = request.POST["preference"]
	user.recent = request.POST["recent"]
	user.frequent = request.POST["frequent"]
	user.monetary = request.POST["monetary"]
	user.times = request.POST["times"]
	user.latitude = request.POST["latitude"]
	user.longitude = request.POST["longitude"]
	user.save()
	data = {
	"successmsg" : "User Registered Successfully"
	}
	return render(request,'index.html',context=data)

