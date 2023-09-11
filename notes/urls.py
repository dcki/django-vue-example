from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('note/update', views.update_note, name='update_note'),
]
