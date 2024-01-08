from django.urls import path

from .views import (
    MusicListView,
    MusicDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView,
    UserMusicListView,
  
   
   
)   
from .import views

urlpatterns = [
    path('', MusicListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserMusicListView.as_view(), name='user-posts'),
    path('Music/<int:pk>/', MusicDetailView.as_view(), name='post-detail'),

   
    path('post/new/', views.UploadMusicFile, name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
   
]
