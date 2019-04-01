from django.db import models

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField(default='body goes here')
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e, %Y')

    def __str__(self):  
        return self.blog_title