# family-tools

## Setup environment

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
