from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers

from models import Sale
from forms import PaymentForm
# Create your views here.

def index(request):
	return render(request, 'hw1/index.html')

def indexjson(request):
	category = request.GET.get('category')
	if category is None:
		querySet = Things.objects.all()
	else:
		querySet = Things.objects.filter(category = category)
	data = serializers.serilize("json", querySet)
	return HttpResponse(data, content_type = "application/json")

def login(request):
	return render(request, 'hw1/login.html') 


def auth_login(request, on success = '/hw1/index', onfail = '/h1/login'):
	email = request.POST.get('email')
    password = request.POST.get('password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    user = authenticate(username=email, password=password)

    if user is None:
    	messages.add_message(request, messages.ERROR, 'Login Failed. Please Try Again.', 'login', True)
        return redirect(onfail)
    else:
    	auth_login(request, user)
    	return redirect(onsuccess)

def signup(request, on success = '/hw1/index', onfail = '/h1/login'):
	email = request.POST.get('email')
    password = request.POST.get('password')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')

    if not user_exists(email):
    	user = User(username = email)
    	user.set_password(password)
    	user.save()
    	auth_login(request, user)
    	return redirect(onsuccess)
   	else:
   		messages.add_message(request, messages.ERROR, 'User Already Existed. Please Try Again.', 'login', True)
        return redirect(onfail)


def user_exists(email):
	return User.objects.filter(username = email.count() != 0

 
def charge(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
 
        if form.is_valid(): # charges the card
            return HttpResponse("Successfully charged your card")
    else:
        form = PaymentForm()
 
    return render_to_response("charge.html",
                        RequestContext( request, {'form': form} ) )



