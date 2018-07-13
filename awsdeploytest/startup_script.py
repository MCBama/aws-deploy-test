from awsdeploytest.models import Client
import os

if not Client.objects.filter(schema_name='public').exists():
    tenant = Client(domain_url=os.environ['SERVER_DOMAIN_URL'], schema_name='public')
    tenant.save()
if not Client.objects.filter(schema_name='test1').exists():
    tenant = Client(domain_url=f'test1.{os.environ["SERVER_DOMAIN_URL"]}', schema_name='test1')
    tenant.save()