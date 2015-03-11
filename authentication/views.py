from django.shortcuts import render
from authentication.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.
def  index(request):
	return render(request, 'authentication/index.html', {})

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			registered = True

			messages.success( request, 'Registration Complete!' )
			return HttpResponseRedirect(reverse('register'))
	else:
		user_form = UserForm()

	return render(request, 
		'authentication/register.html',
		{'user_form': user_form, 'registered': registered})

def user_login(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(username=username,password=password)

			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/tasks/')
				else:
					return render(request, 'authentication/login.html', {'message': 'Your account is disabled.'})
			else:
				return render(request, 'authentication/login.html', {'message': 'Invalid credentials.'})

		else:
			return render(request, 'authentication/login.html', {})
	else:
		return HttpResponseRedirect('/')

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/')