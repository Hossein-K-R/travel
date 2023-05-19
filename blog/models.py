from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    titel = models.CharField(max_length=255)
    content = models.TextField()
    conted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(category)
    tags = TaggableManager()

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
