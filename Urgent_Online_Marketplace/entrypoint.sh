#!/bin/bash

# Apply database migrations
python manage.py migrate

# Create a Django superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('duet', 'duet@example.com', 'duet')" | python manage.py shell

# Collect static files
python manage.py collectstatic --noinput

# Start the Django development server
python manage.py runserver 0.0.0.0:8000


exec "$@"