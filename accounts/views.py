from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    UserProfileForm)
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
# Create your views here.

def home(request):
    args = {'user': request.user}
    return render(request , 'feed/index.html',args)



def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            flag=0
            args1 = {'flag': flag}
            form.save()
            return redirect('/account/login/',args1)
        else:
            flag=1
            args1 = {'flag': flag }
            return render(request, 'accounts/login1.html',args1)

    else:
        form = RegistrationForm()

        args = {'form': form,'form_head':"Details"}
        return render(request,'accounts/reg_form.html',args)

def register2(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            hi = form.save(commit=False)
            hi.user = request.user
            UserProfile.objects.filter(user=request.user).delete()
            hi.save()
            return redirect('/account/profile')
    else:
        form = UserProfileForm()

        args = {'form1': form,'form_head':'Details'}
        return render(request,'accounts/reg_form_2.html',args)


@login_required
def view_profile(request):
    args = {'user': request.user}

    if request.method == 'POST':
        form1 = PasswordChangeForm(data=request.POST,user = request.user)

        if form1.is_valid():
            form1.save()
            return redirect('/account/profile')

    else:
        form1=PasswordChangeForm(user = request.user)
        args = {'form' : form1,
                'test': "Change Your Password"}
    return render(request, 'accounts/profile.html',args)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form=EditProfileForm(instance = request.user)
        args = {'form' : form}
        return render(request,'accounts/edit_profile.html',args)
@login_required
def change_password(request):
    if request.method == 'POST':
        form1 = PasswordChangeForm(data=request.POST,user = request.user)

        if form1.is_valid():
            form1.save()
            return redirect('/account/profile')

    else:
        form1=PasswordChangeForm(user = request.user)
        args = {'form' : form1,
                'test': "Change your Password"}
        return render(request,'accounts/profile.html',args)