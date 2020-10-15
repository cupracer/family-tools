#!/bin/bash

if [ -z "$ALLOWED_HOSTS" ]; then
  ALLOWED_HOSTS="['*']"
fi

sed -E -i 's/^DEBUG[ ]*=.*/DEBUG = False/' family_tools/settings.py
sed -E -i "s/^ALLOWED_HOSTS[ ]*=.*$/ALLOWED_HOSTS = ${ALLOWED_HOSTS}/" family_tools/settings.py

./manage.py migrate
./manage.py runserver --insecure 0.0.0.0:8000
