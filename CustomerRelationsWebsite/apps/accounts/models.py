from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from apps.core.models import TimeStampedModel

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('staff', 'Staff'),
    ('user', 'User'),
]
GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('common', 'common'),)
COUNTRY = [
    ('Saudi Arabia', 'Saudi Arabia'),
    ('South Sudan', 'South Sudan'),
    ('Sudan', 'Sudan'),
    ('Egypt', 'Egypt'),
    ('common', 'common'),
]


class Profile(TimeStampedModel, models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=False, default='new user')

    bio = models.TextField(default='No bio data', max_length=400)
    gender = models.CharField(max_length=6, choices=GENDER, default='common')
    country = models.CharField(max_length=200,choices=COUNTRY, default='common')
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default='User')

    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    slug = models.SlugField(unique=True, blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.user.username}-{self.created}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
