from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from main.forms import StyleForMixin
from users.models import User


class UserForm (StyleForMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class VerificationForm(forms.Form):
    key = forms.CharField()


