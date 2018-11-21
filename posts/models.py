from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group

#markdown inside POSTS
import misaka

#Get current user into a session
from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    title_html = models.TextField(editable=False)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.title_html = misaka.html(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ('title',)



class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ["user", "message"]
