from django.db import models
from django.contrib.auth import get_user_model


# from tenant_schemas.models import TenantMixin

# class Client(TenantMixin):
#     name = models.CharField(max_length=100)
#     created_on = models.DateField(auto_now_add=True)
#     auto_create_schema = True

class Thread(models.Model):
    title = models.CharField(max_length=360)
    start_date = models.DateTimeField('date started')

class Post(models.Model):
    from awsdeploytest.models import Client
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    text = models.TextField()
    post_date = models.DateTimeField('date posted')
    edited = models.BooleanField(default=False)
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)