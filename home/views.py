from django.shortcuts import render
from .models import Music,Categorie
from django.shortcuts import render,get_object_or_404,redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy,reverse
from django.views.generic import RedirectView
from django.contrib import messages
from .forms import  CreateMusicUpload


from django.views.generic import (
    ListView,
    DetailView,
    # CreateView,
    # UpdateView,
    # DeleteView
)
def home(request):
    context = {
        'music': Music.objects.all()
    }
    return render(request,'blog/home.html',context)



class MusicListView(ListView):
    model = Music
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'music'
    ordering = ['-date_posted']
    paginate_by = 5


class UserMusicListView(ListView):
    model = Music
    template_name = 'blog/user_music.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'music'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Music.objects.filter(author=user).order_by('-date_posted')
    

class MusicDetailView(DetailView):
    model = Music
    template_name = 'blog/music_detail.html'



def UploadMusicFile(request):
    form = CreateMusicUpload()

    if request.method == 'POST':
        form = CreateMusicUpload(request.POST,request.FILES)
        if form.is_valid():
            form.instance.author= request.user
            form.save()
            messages.success(request,f'A few Post Music has been Created')
            return redirect('blog-home')

        else:
            messages.info(request,f'error the Post is not created!')
            return redirect('post-create')

    context ={
        'form':form
    }
    
    return render(request,'blog/uploadFile.html',context)
