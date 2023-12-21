from django.db import models
from django.contrib.auth.models import User
from apps.users.models import Profile


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return "Group:" + self.name


class Membership(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    role = models.CharField(max_length=20, choices=(
        ('member', 'Member'),
        ('leader', 'Leader'),
        ('supervisor', 'Supervisor'),
        ('assistant', 'Assistant'),
    ))

    def __str__(self):
        return f"{self.user} is a {self.role} in the {self.group}"


class GroupPost(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    published_date = models.DateField(null=True, auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile, default=[])

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name='comments')
    commentor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_commenting')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - {self.commentor.user.username}'
