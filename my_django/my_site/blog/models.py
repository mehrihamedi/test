from django.db import models

from django.utils import timezone
# Create your models here.
class Article(models.Model):

    title=models.CharField(max_length=100)

    slug=models.SlugField(max_length=100, unique=True,primary_key=True)

    content=models.TextField()

    publish=models.DateTimeField(default=timezone.now)

    created=models.DateTimeField(auto_now_add=True)

    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title +" " +str(self.publish.strftime("%d-%m-%Y %H:%M"))