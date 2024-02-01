from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор', editable=False)
    title = models.CharField(max_length=200, verbose_name='Title', blank=False)
    text = models.TextField(blank=False, verbose_name='Text')
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    publish_date = models.DateTimeField(blank=True, null=True, editable=False)
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Изображение поста")

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
        ordering = ['created_date',]
    
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title