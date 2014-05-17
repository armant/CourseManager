from polls.models import UserProfile, Choice
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthday',)


class ChoiceForm(forms.ModelForm):
    new_course = forms.CharField(max_length=200, help_text="Please enter the new course name.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Choice
        fields = ('new_course',)