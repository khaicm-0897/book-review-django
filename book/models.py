from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=timezone.datetime.now)
    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    image = models.FileField(upload_to='static/home/images/uploads/%Y/%m/')
    author = models.CharField(max_length=100)
    pages = models.IntegerField(default=0)
    publish_date = models.DateTimeField(default=timezone.datetime.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.datetime.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.datetime.now)
    Reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Mark(models.Model):
    choice_status = ((0, 'Unread'), (1, 'Read'), (2, 'Reading'))
    status = models.IntegerField(choices=choice_status, default=0)
    choice_favorite = ((0, 'Normal'), (1, 'Favorite'))
    favorite = models.IntegerField(choices=choice_favorite, default=0)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
