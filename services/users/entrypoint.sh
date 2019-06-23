#!/bin/sh

echo "Waiting for datastore emulator..."

while ! nc -z datastore 8001; do
  sleep 0.1
done

echo "Datastore emulator started"

python manage.py run -h 0.0.0.0