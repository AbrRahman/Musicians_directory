from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from musician.models import MusicianModel
class MusicianForm(forms.ModelForm):
    class Meta:
        model=MusicianModel
        fields = "__all__"


        def __str__(self) -> str:
            self.First_name

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"id":"required"}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={"id":"required"}))
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']