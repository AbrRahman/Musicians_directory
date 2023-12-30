from django import forms
from album.models import AlbumModel
class AlbumForm(forms.ModelForm):
    class Meta:
        model=AlbumModel
        fields = "__all__"


        # def __str__(self) -> str:
        #     self.album_name