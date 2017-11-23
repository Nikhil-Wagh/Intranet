from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    UserProfileForm)
from accounts.models import UserProfile,Feedback,Contact
from accounts.forms import UserProfileForm,FeedbackForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
import os
import datetime
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from accounts.forms import (RegistrationForm,EditProfileForm,ContactFilterForm)
from accounts.models import UserProfile
from accounts.forms import UserProfileForm,ContactForm
from django.conf import settings
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm)
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
# Create your views here.


def current_datetime(request):
    now = datetime.datetime.now()
    args={'time':now}
    return render(request, 'accounts/base.html', args)


@login_required
def home(request):
    args = {'user': request.user}
    return render(request , 'feed/index.html',args)

#feedback taking
@login_required
def feedback(request):
    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            new_feedback = Feedback()
            new_feedback.feedback = feedback_form.cleaned_data['feedback']
            print(new_feedback.feedback)
            #new_feedback.feedback_time = timezone.now()
            #new_feedback.save()
            t = request.user
            logout_time = now = datetime.datetime.now()
            login_time = t.last_login
            filepath = os.path.join('datafolder', str(t))
            f = open(filepath, "a+")
            f.write("-----------------------------------------------------------------\n")
            f.write("Login Time: %s" % str(login_time.strftime("%Y-%m-%d %H:%M")) + "\n")
            f.write("Feedback: \n%s" % str(new_feedback.feedback) + "\n")
            f.write("Logout Time: %s" % str(logout_time.strftime("%Y-%m-%d %H:%M")) + "\n")

            f.write("-----------------------------------------------------------------\n\n")

            return HttpResponseRedirect('/account/logout')

    else:
        feedback_form = FeedbackForm()

    context = {'feedback_form': feedback_form,}
    return render(request, 'accounts/feedback_form.html', context)

"""@login_required
def feedbacktillnow(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            new_contact = Contact()
            new_contact.selectuser = contact_form.cleaned_data['selectuser']
            t = request.user
            directory = "datafolder/" + str(t)
            # print (ret_variable_count())
            filepath = os.path.join(directory)
            f = open(filepath, "r+")
            content = f.readlines()

            return HttpResponse(content, content_type='text/plain')

            #return HttpResponseRedirect('/account/')

    else:
        contact_form = ContactForm()
        all_users = UserProfile.objects.all()

    context = {'contact_form': contact_form,'all_users' : all_users}
    return render(request, 'accounts/summary.html', context)"""

@login_required
def feedbacktillnow(request):
    if request.method == 'POST':
        contact_form = ContactFilterForm(request.POST)
        if contact_form.is_valid():

            t = contact_form.cleaned_data['User']
            print(t)
            #t = request.user
            directory = "datafolder/" + str(t)
            # print (ret_variable_count())

            filepath = os.path.join(directory)
            if os.path.exists(filepath):
                f = open(filepath, "r+")
                content = f.readlines()
                return HttpResponse(content, content_type='text/plain')
            else:
                print("summary not found")
                return HttpResponse("No Record Found")



            #return HttpResponseRedirect('/account/')

    else:
        contact_form = ContactFilterForm()
        all_users = UserProfile.objects.all()

    context = {'contact_form': contact_form,}
    return render(request, 'accounts/summary.html', context)


def logout_view(request):
    print request.user
    logout(request)
    return HttpResponseRedirect('/account/login')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/login/')

        else:
             return render(request, 'accounts/login1.html')
    else:
        form = RegistrationForm
        args = {'form': form, 'form_head': "Details"}
        return render(request, 'accounts/reg_form.html', args)

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

        args = {'form': form,}
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

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
        else:
            return render(request, 'accounts/login1.html')

    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)
