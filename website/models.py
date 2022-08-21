from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse




Choices_users = (
    ('دارد','دارد'),
    ('ندارد','ندارد'),
)



class kharid_khone_orginal(models.Model):
    finder_home = models.CharField(max_length=444,blank=True)
    home_code = models.CharField(max_length=444,blank=True)
    slug = models.SlugField(max_length=444,blank=True)
    like_post = models.ManyToManyField(User,blank=True,related_name='likeds')
    dislike_post = models.ManyToManyField(User,blank=True,related_name='dislikeds')
    viewed_post = models.ManyToManyField(User,blank=True,related_name='view_users')
    metrazh = models.CharField(max_length=444,blank=True)
    aks_asli_1 = models.ImageField(upload_to='image_home_org',blank=True)
    aks_asli_2 = models.ImageField(upload_to='image_home_org',blank=True)
    aks_asli_3 = models.ImageField(upload_to='image_home_org',blank=True)
    aks_dakhli_1  = models.ImageField(upload_to='image_home_shots',blank=True)
    aks_dakhli_2  = models.ImageField(upload_to='image_home_shots',blank=True)
    aks_dakhli_3  = models.ImageField(upload_to='image_home_shots',blank=True)
    aks_dakhli_4  = models.ImageField(upload_to='image_home_shots',blank=True)
    aks_dakhli_5  = models.ImageField(upload_to='image_home_shots',blank=True)
    aks_dakhli_6  = models.ImageField(upload_to='image_home_shots',blank=True)
    tedade_otag_khab = models.CharField(max_length=444,blank=True)
    kaf_seamick = models.BooleanField(blank=True)
    jens_kabint = models.CharField(max_length=444,blank=True)
    parking = models.BooleanField(blank=True)
    balkon = models.BooleanField(blank=True)
    estakhr = models.BooleanField(blank=True)
    adderss = models.CharField(max_length=444,blank=True)
    geymt = models.CharField(max_length=444,blank=True)
    vadie_rahn = models.CharField(max_length=444,blank=True)
    ejare = models.CharField(max_length=444,blank=True)
    tarikh_sakht = models.CharField(max_length=444,blank=True)
    tabaghe_chandom = models.CharField(max_length=444,blank=True)
    anbari = models.BooleanField(blank=True)
    coler = models.BooleanField(blank=True)
    shomine = models.BooleanField(blank=True)
    tedad_dasteshoyi = models.CharField(max_length=444,blank=True)
    tedad_hamam = models.CharField(max_length=444,blank=True)
    sanad_tak_barg = models.BooleanField(blank=True)
    shomare_telefon = models.CharField(max_length=444,blank=True)
    mantaghe_shargi_ya_gharbi = models.CharField(max_length=444,blank=True)
    kagaz_divary = models.BooleanField(blank=True)
    nama_romy = models.BooleanField(blank=True)
    dorbin = models.BooleanField(blank=True)
    tozihat = models.TextField(blank=True)
    ertefae_saghf = models.CharField(max_length=444,blank=True)


    def __str__(self):
        return '%s - %s' %(self.finder_home,self.home_code)

    def get_absolute_url(self):
        return reverse('website:go_to_post',args=[self.slug])

    class Meta:
        ordering = ['-id']





        # end_home_model
################################################################################################################################
        # start profile model






class Profile_website_users(models.Model):
      users = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
      fake_name = models.CharField(max_length=444)
      slug = models.SlugField(max_length=444)
      image = models.ImageField(upload_to='profile_images',blank=True)
      age = models.IntegerField(default=20,blank=True)
      body = models.TextField(blank=True)
      created = models.DateTimeField(auto_created=True)

      def __str__(self):
          return '%s - %s' % (self.users,self.fake_name)




      def get_absoluted_url(self):
          pass



      class Meta:
          ordering = ['-created']







class Comment_users_post(models.Model):
    find_post = models.ForeignKey(kharid_khone_orginal,on_delete=models.CASCADE,blank=True)
    commenter_name = models.ForeignKey(Profile_website_users,on_delete=models.CASCADE,blank=True)
    liked_comment = models.ManyToManyField(User,related_name='liked_user',blank=True)
    disliked_comment = models.ManyToManyField(User,related_name='dislaike_user',blank=True)
    time_created = models.DateTimeField(auto_created=True,blank=True)
    text_body = models.TextField(blank=True)


    def __str__(self):
        return '%s - %s' % (self.find_post,self.commenter_name)

    def get_absolute_urls(self):
        pass

    class Meta:
        ordering = ['-time_created']








class Replay_comment(models.Model):
    finder_commenter = models.ForeignKey(Comment_users_post,on_delete=models.CASCADE)
    replayer_comment = models.ForeignKey(Profile_website_users,on_delete=models.CASCADE)
    text_replay = models.TextField(blank=True)
    date_comment = models.DateTimeField(auto_created=True)

    def __str__(self):
        return '%s - %s' % (self.finder_commenter,self.replayer_comment)

    def get_absoluteds_url(self):
        pass

    class Meta:
        ordering = ['-date_comment']
