from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms





class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(help_text='A valid email address, please.')

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
