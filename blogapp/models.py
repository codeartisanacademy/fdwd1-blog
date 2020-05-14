from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# create class for Post

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    


class Post(models.Model):
    STATUSES = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    title = models.CharField(max_length=200)
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=0)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts', blank=True, null=True)

