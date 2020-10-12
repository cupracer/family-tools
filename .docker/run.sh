#!/bin/bash

if [ -z $ALLOWED_HOSTS ]; then
  ALLOWED_HOSTS="['*']"
fi

sed -E -i "s/^(ALLOWED_HOSTS.*=).*$/\1 '${ALLOWED_HOSTS}'/" family_tools/settings.py

./manage.py migrate
./manage.py runserver 0.0.0.0:8000
