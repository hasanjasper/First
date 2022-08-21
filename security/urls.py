from django.urls import path
from . import views

app_name='security'


urlpatterns = [
    path('register/',views.register,name='register'),
    path('join/',views.join,name='join')

]