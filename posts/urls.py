from django.urls import path

from posts.views import HomePageView

urlpatterns = [
    
    path('home/', HomePageView.as_view() , name = 'Home'),
]
