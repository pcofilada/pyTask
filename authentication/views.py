from django.shortcuts import render
from authentication.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			registered = True

		else:
			print user_form.errors
	else:
		user_form = UserForm()

	return render(request, 
		'authentication/register.html',
		{'user_form': user_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Your account is disabled.')
		else:
			print "Invalid login detauls: {0}, {1}".format(username, password)
			return HttpResponse('Invalid login details')

	else:
		return render(request, 'authentication/login.html', {})

@login_required
def  index(request):
	return HttpResponse("Since you're logged in, you can see this text")