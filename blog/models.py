from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.title
    
    def publish_post(self):
        self.publish_date = timezone.now()
        self.save()
    
    # def approved_cmts(self):
    #     return self.comments.objects.filter(approved_time=True)
        
    def approved_cmts(self):
        return self.comments.filter(approved_time=True)

    # def get_absolute_url(self):
    #     return reverse("post_detail",kwargs={'pk':self.pk})


    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    comment_msg = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now())
    approved_time = models.BooleanField(default=False)


    def __str__(self):
        return self.comment_msg
    
    def approve(self):
        self.approved_time = True
        self.save()

    
    

