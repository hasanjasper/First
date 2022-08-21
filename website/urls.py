from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('',views.home,name='home'),
    path('go_to_post/<slug:slug>/',views.go_to_post,name='go_to_post'),
    path('likeds/<int:id>/', views.likeds, name='likdes'),
    path('dislikeds/<int:id>/', views.dislikeds, name='dislikdes'),
    path('profile/',views.profile,name='profile'),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('deleted_profile/',views.deleted_profile,name='deleted_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('like_comment/<int:id>/',views.like_comment,name='like_comment'),
    path('dislike_comment/<int:id>/',views.dislike_comment,name='dislike_comment'),
    path('add_commenter/<int:id>/',views.add_commenter,name='add_commenter'),
    path('deleted_comment/<int:id>/<slug:slug>/',views.deleted_comment,name='deleted_comment'),
    path('serchid/',views.serchid,name='serchid'),
    path('searched_tags/',views.searched_tags,name='searched_tags'),
]