echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'asdf1234')" | python manage.py shell