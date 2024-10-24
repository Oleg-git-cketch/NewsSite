from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    search_bar = forms.CharField(max_length=64)

class RegForm(UserCreationForm):
