from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMessage
from .forms import *
from .models import *
from django.utils.decorators import method_decorator
from django.http import *
from django.template.loader import render_to_string
from django.db.models import Q


def home(request):
    object_model = kharid_khone_orginal.objects.all()
    pagina = Paginator(object_model,1)
    page = request.GET.get('page')
    orginals = pagina.get_page(page)
    atack = 'a' * orginals.paginator.num_pages
    return render(request,'website/home.html',{'orginals':orginals,'atack':atack})






def maxi(request):
    return {
        'maxi': Profile_website_users.objects.all()
    }




def go_to_post(request,slug):
    user = request.user
    item = get_object_or_404(kharid_khone_orginal,slug=slug)
    prof = Profile_website_users.objects.get(users=user)
    commer = Comment_users_post.objects.filter(find_post=item)
    replys = Replay_comment.objects.filter(replayer_comment=prof)
    if user in item.viewed_post.all():
        pass
    else:
        item.viewed_post.add(user)
    return render(request,'website/post_pv.html',{'item':item,'commer':commer,'prof':prof})






def likeds(request,id):
    user = request.user
    objec = kharid_khone_orginal.objects.get(id=id)
    if user in objec.like_post.all():
        objec.like_post.remove(user)
    else:
        objec.like_post.add(user)
    return redirect(objec.get_absolute_url)





def dislikeds(request,id):
    user = request.user
    objecter = kharid_khone_orginal.objects.get(id=id)
    if user in objecter.dislike_post.all():
        objecter.dislike_post.remove(user)
    else:
        objecter.dislike_post.add(user)
    return redirect(objecter.get_absolute_url)






def profile(request):
    user = request.user
    find_user = Profile_website_users.objects.filter(users=user)
    return render(request,'website/profile.html',{'find_user':find_user})



def create_profile(request):
    user = request.user
    if request.method == 'POST':
        form = create_profile_users(request.POST,request.FILES)

        if form.is_valid():
            profix = Profile_website_users.objects.get_or_create(users=user,fake_name=form.cleaned_data['fake_name'],
                                                                 slug=user.id,age=form.cleaned_data['age'],
                                                                 image=form.cleaned_data['image'],body=form.cleaned_data['body'],
                                                                 users_id=user.id,created=datetime.now())



            return redirect('website:profile')
    else:
        form = create_profile_users
    return render(request,'website/created_profile.html',{'form':form})







def deleted_profile(request):
    user = request.user
    opj = Profile_website_users.objects.filter(users=user)
    opj.delete()
    return redirect('website:profile')









def update_profile(request):
    user = request.user
    items = Profile_website_users.objects.get(users=user)
    if request.method == 'POST':
        form = update_profile_users(request.POST,request.FILES,instance=items)
        if form.is_valid():
            form.save()
        return redirect('website:profile')
    else:
        form = update_profile_users
    return render(request,'website/update_profile.html',{'form':form})












def like_comment(request,id):
    user = request.user
    finder_user = Comment_users_post.objects.get(id=id)
    if user in finder_user.liked_comment.all():
        finder_user.liked_comment.remove(user)
    else:
        finder_user.liked_comment.add(user)
    return redirect(finder_user.find_post.get_absolute_url)






def dislike_comment(request,id):
    user = request.user
    find_dis = Comment_users_post.objects.get(id=id)
    if user in find_dis.disliked_comment.all():
        find_dis.disliked_comment.remove(user)
    else:
        find_dis.disliked_comment.add(user)
    return redirect(find_dis.find_post.get_absolute_url())




def add_commenter(request,id):
    user = request.user
    prof_user = Profile_website_users.objects.get(users=user)
    text_body = request.POST['text_body']
    postt = kharid_khone_orginal.objects.get(id=id)
    if request.method == 'POST':
        form = Add_commenter(request.POST)
        if form.is_valid():
            conter = Comment_users_post.objects.get_or_create(find_post=postt,commenter_name=prof_user,time_created=datetime.now(),text_body=text_body,
                                                              )
        return redirect(postt.get_absolute_url())








def deleted_comment(request,id,slug):
    user = request.user
    rower = kharid_khone_orginal.objects.get(slug=slug)
    # while rower == rower.slug:
    #     pass
    # rower = rower
    findes = Comment_users_post.objects.filter(id=id)
    findes.delete()
    return redirect(rower.get_absolute_url())






def serchid(request):
    user = request.user
    searched_user = request.POST['searched_user']
    if request.method == 'POST':
        items = kharid_khone_orginal.objects.filter(Q(finder_home__contains=searched_user) |Q(tedad_hamam=searched_user) |Q(metrazh=searched_user))
        return render(request,'website/searchedss.html',{'items':items,'searched_user':searched_user})





def searched_tags(request):
    user = request.user
    generays = request.POST['generays']
    orginals = kharid_khone_orginal.objects.filter(tedad_hamam=generays)
    if request.method == 'POST':
       return render(request,'website/searched_tags.html',{'orginals':orginals})



















