# Generated by Django 4.1 on 2022-08-15 16:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='kharid_khone_orginal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finder_home', models.CharField(blank=True, max_length=444)),
                ('home_code', models.CharField(blank=True, max_length=444)),
                ('slug', models.SlugField(blank=True, max_length=444)),
                ('metrazh', models.CharField(blank=True, max_length=444)),
                ('aks_asli_1', models.ImageField(blank=True, upload_to='image_home_org')),
                ('aks_asli_2', models.ImageField(blank=True, upload_to='image_home_org')),
                ('aks_asli_3', models.ImageField(blank=True, upload_to='image_home_org')),
                ('aks_dakhli_1', models.ImageField(blank=True, upload_to='image_home_shots')),
                ('aks_dakhli_2', models.ImageField(blank=True, upload_to='image_home_shots')),
                ('aks_dakhli_3', models.ImageField(blank=True, upload_to='image_home_shots')),
                ('aks_dakhli_4', models.ImageField(blank=True, upload_to='image_home_shots')),
                ('aks_dakhli_5', models.ImageField(blank=True, upload_to='image_home_shots')),
                ('aks_dakhli_6', models.ImageField(blank=True, upload_to='image_home_shots')),
                ('tedade_otag_khab', models.CharField(blank=True, max_length=444)),
                ('kaf_seamick', models.BooleanField(blank=True)),
                ('jens_kabint', models.CharField(blank=True, max_length=444)),
                ('parking', models.BooleanField(blank=True)),
                ('balkon', models.BooleanField(blank=True)),
                ('estakhr', models.BooleanField(blank=True)),
                ('adderss', models.CharField(blank=True, max_length=444)),
                ('geymt', models.CharField(blank=True, max_length=444)),
                ('vadie_rahn', models.CharField(blank=True, max_length=444)),
                ('ejare', models.CharField(blank=True, max_length=444)),
                ('tarikh_sakht', models.CharField(blank=True, max_length=444)),
                ('tabaghe_chandom', models.CharField(blank=True, max_length=444)),
                ('anbari', models.BooleanField(blank=True)),
                ('coler', models.BooleanField(blank=True)),
                ('shomine', models.BooleanField(blank=True)),
                ('tedad_dasteshoyi', models.CharField(blank=True, max_length=444)),
                ('tedad_hamam', models.CharField(blank=True, max_length=444)),
                ('sanad_tak_barg', models.BooleanField(blank=True)),
                ('shomare_telefon', models.CharField(blank=True, max_length=444)),
                ('mantaghe_shargi_ya_gharbi', models.CharField(blank=True, max_length=444)),
                ('kagaz_divary', models.BooleanField(blank=True)),
                ('nama_romy', models.BooleanField(blank=True)),
                ('dorbin', models.BooleanField(blank=True)),
                ('tozihat', models.TextField(blank=True)),
                ('ertefae_saghf', models.CharField(blank=True, max_length=444)),
                ('dislike_post', models.ManyToManyField(blank=True, related_name='dislikeds', to=settings.AUTH_USER_MODEL)),
                ('like_post', models.ManyToManyField(blank=True, related_name='likeds', to=settings.AUTH_USER_MODEL)),
                ('viewed_post', models.ManyToManyField(blank=True, related_name='view_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
