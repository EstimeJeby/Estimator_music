from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Categorie(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self) :
        return self.name
    
    def save(self, *args, **Kwargs):
        super(Categorie,self).save(*args,**Kwargs)
        

class Music(models.Model):

    name = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(upload_to='Image_Music_upload',blank=False)
    music = models.FileField(upload_to='Music_upload',blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.name
    
    def save(self, *args, **Kwargs):
        super(Music,self).save(*args,**Kwargs)






  