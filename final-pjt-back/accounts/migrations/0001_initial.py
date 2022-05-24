# Generated by Django 3.2.12 on 2022-05-24 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('spouse_name', models.CharField(blank=True, max_length=100)),
                ('followings', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, default='media/김태리.jpg', null=True, upload_to='thumbnails/user/image/')),
                ('backdrop', imagekit.models.fields.ProcessedImageField(blank=True, default='media/tmp_pre6_uenvE9N.jpg', null=True, upload_to='thumbnails/user/backdrop/')),
                ('introduce', models.CharField(blank=True, max_length=100, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('남성', '남성'), ('남성', '여성')], max_length=2, null=True)),
                ('location1', models.CharField(blank=True, choices=[('서울특별시', '서울특별시'), ('부산광역시', '부산광역시'), ('대구광역시', '대구광역시'), ('인천광역시', '인천광역시'), ('광주광역시', '광주광역시'), ('대전광역시', '대전광역시'), ('울산광역시', '울산광역시'), ('세종특별자치시', '세종특별자치시'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('제주특별자치도', '제주특별자치도')], max_length=10, null=True)),
                ('location2', models.CharField(blank=True, max_length=5, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
