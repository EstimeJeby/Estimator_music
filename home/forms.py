from django import forms

from .models import Music


class CreateMusicUpload(forms.ModelForm):
     music = forms.FileField()
     class Meta:
          model = Music
          fields = ['name','image','detail','Categorie','music']


