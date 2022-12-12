from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name ="story"),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
]


# urlpatterns += staticfiles_urlpatterns()
