import user

from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm

from accounts.models import UserProfile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username=forms.CharField(required=True,max_length=10)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description','city',
                  'website','phone','experience',
                  'skills','image']

        def save(self, commit=True):
            ob = super(UserProfileForm, self).save(commit=False)
            ob.description = self.cleaned_data['description']
            ob.city = self.cleaned_data['city']
            ob.website = self.cleaned_data['website']
            ob.phone = self.cleaned_data['phone']
            ob.experience = self.cleaned_data['experience']
            ob.skills = self.cleaned_data['skills']
            ob.image=self.cleaned_data['image']

            if commit:
                user.save()

            return ob

class FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    selectuser = forms.CharField()

class ContactFilterForm(forms.Form):
    User = forms.ModelChoiceField(queryset=User.objects.all())

