from django.urls import path
from . import views
app_name = 'maail'
urlpatterns = [
    path('', views.index, name="index"),
]
