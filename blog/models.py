from django.db import models

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField(default='body goes here')
    image = models.ImageField(upload_to='images/')
