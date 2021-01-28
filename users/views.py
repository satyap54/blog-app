from django.shortcuts import render, redirect
from . forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from . models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):

	if(request.method == 'POST'):
		form = SignUpForm(request.POST)
		if(form.is_valid()):
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Your account has been created! Try to login now')
			return redirect('login')
	else:
		form = SignUpForm()
	context = {
		'form' : form,
	}

	return render(request, 'users/register.html', context)

@login_required
def profile_view(request):

	#To check what is sent in request object
	# print("Logged in : ", (request.user).__dict__)
	profile_obj = Profile.objects.get(user = request.user)
	print(profile_obj) # Checking if the correct user is grabbed or not

	u_form = UserUpdateForm(request.POST, instance = request.user)
	p_form = ProfileUpdateForm(request.POST, request.FILES, instance = profile_obj)

	if(request.method == 'POST'):
		if(u_form.is_valid() and p_form.is_valid()):
			u_form.save()
			p_form.save()
			messages.success(request, "Your account has been updated")
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = profile_obj)

	context = {
		'u_form' : u_form,
		'p_form' : p_form,
	}

	return render(request, 'users/profile.html', context)