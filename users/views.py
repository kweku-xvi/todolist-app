from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserInfoForm, UserImageForm
from django.contrib import messages

def signup(response):
    if response.method == 'POST':
        form = SignUpForm(response.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(response, f'Account created for {username}! Log In now')
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(response, 'users/signup.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST, instance=request.user)
        profile_form = UserImageForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserInfoForm(instance=request.user)
        profile_form = UserImageForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'u_form':user_form, 'p_form':profile_form})
