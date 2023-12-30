from django import forms
from musician.models import MusicianModel
class MusicianForm(forms.ModelForm):
    class Meta:
        model=MusicianModel
        fields = "__all__"


        def __str__(self) -> str:
            self.First_name