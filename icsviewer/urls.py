from django.urls import path

from . import views

app_name = 'icsviewer'
urlpatterns = [
    # ex: /icsviewer/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /icsviewer/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
