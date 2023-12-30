from django.db import models

class MusicianModel(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    phone_number=models.CharField(max_length=12)
    instrument_type=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.first_name

