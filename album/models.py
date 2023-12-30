from django.db import models
from musician.models import MusicianModel
class AlbumModel(models.Model):
    album_name=models.CharField(max_length=30)
    musician=models.ForeignKey(MusicianModel,on_delete=models.CASCADE)
    release_date=models.DateField()
    rating=models.IntegerField()

    def __str__(self) -> str:
        return self.album_name


