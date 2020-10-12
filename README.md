# family-tools

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

### pull image
```shell script
docker pull docker.pkg.github.com/cupracer/family-tools/family-tools:latest
```

### run basic container for non-productive environment
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
