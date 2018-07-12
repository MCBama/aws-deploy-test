from django.db import models
from django.contrib.auth import get_user_model

class Thread(models.Model):
    title = models.CharField(max_length=360)
    start_date = models.DateTimeField('date started')

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    text = models.TextField()
    post_date = models.DateTimeField('date posted')
    edited = models.BooleanField(default=False)