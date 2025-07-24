#!/bin/bash

# 🚦 Wait for the database to be ready (adjust if needed)
# echo "⏳ Waiting for the database to be ready..."
# sleep 5

# 🔄 Apply migrations
echo "🗃️ Applying database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# 👤 Create default superuser if not exists
echo "🔐 Creating superuser 'h1Admin' if it doesn't exist..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='h1Admin').exists():
    User.objects.create_superuser('h1Admin', 'admin@example.com', 'h1Admin*')
    print("✅ Superuser created.")
else:
    print("ℹ️ Superuser already exists.")
EOF

# 🚀 Start Django development server
echo "🚀 Starting development server on 0.0.0.0:8000..."
exec python manage.py runserver 0.0.0.0:8000