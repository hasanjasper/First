from django.contrib import admin
from .models import *














@admin.register(kharid_khone_orginal)
class kharidAdmin(admin.ModelAdmin):
    list_display = ['finder_home','home_code','metrazh','aks_asli_1','tedade_otag_khab','geymt','tabaghe_chandom','tarikh_sakht','coler','shomare_telefon','jens_kabint','kaf_seamick']


    prepopulated_fields =  {'slug':('home_code',)}



@admin.register(Profile_website_users)
class Profileadmin(admin.ModelAdmin):
    list_display = ['users','fake_name','image','age','created','body']

    list_filter = ['created']

    prepopulated_fields = {'slug':('users',)}







@admin.register(Comment_users_post)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['time_created','find_post','commenter_name','text_body']


    list_editable = ['text_body','find_post','commenter_name']

    list_filter = ['time_created']






@admin.register(Replay_comment)
class ReplayAdmin(admin.ModelAdmin):
    list_display = ['finder_commenter','replayer_comment','text_replay','date_comment']

    list_display_links = ['finder_commenter']

    list_editable = ['text_replay','replayer_comment']





