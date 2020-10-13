# FamilyTools

## About

This web project is intended to provide a collection of useful tools on topics related to a family or shared household. At present, only a household book is included, which can be used to record and categorize income and expenditure. 

This project is still in the early stages of development and there is probably only one running installation out there... which is mine.
Nevertheless, I take the project seriously and try to make it the best tool for managing our household.

## Setup dev environment

### 1. setup Python
Use a system-wide interpreter or create a virtual environment

### 2. install requirements
```shell script
pip install -r requirements.txt
```

### 3. generate static files
```shell script
./manage.py collectstatic
```

### 4. initialize database
```shell script
./manage.py migrate
```

### 5. create admin account
```shell script
./manage.py createsuperuser
```

### 6. start web server
```shell script
./manage.py runserver 8000
```

## Run as container

**Warning:** This should only be started within a trusted and secure environment. Expect that this container is not safe and will likely have security issues which could be exploited by an attacker.

### pull image
```shell script
docker pull docker.pkg.github.com/cupracer/family-tools/family-tools:latest
```

### run basic container for non-productive environment
**Attention:** Please note that you'll lose your database if the container is destroyed (see below for persistent storage)!
```shell script
docker run -it docker.pkg.github.com/cupracer/family-tools/family-tools:latest
```

### limit allowed hosts by setting a container env variable
```shell script
-e ALLOWED_HOSTS="['some.host.name', 'some.ip']"
```

### use persistent database file
```shell script
-v /path/to/persistent/db.sqlite3:/opt/family-tools/db.sqlite3
```

### create super-user
```shell script
docker exec -it my-container ./manage.py createsuperuser
```

## Manage users

Login to the admin interface as superuser
```
http://<your-application>:8000/admin/
```
and create one or more users. 

Make sure to add them to the group "members" to enable them for this application.
