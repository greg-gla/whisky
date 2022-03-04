# Install database

step1. Enter the project directory '*whisky/*', open the terminal , enter the command as follows:
```
python manage.py migrate
python manage.py makemigrations
```
step2. create your own superuser
```
python manage.py createsuperuser
```

step3 migrate the database again
```
python manage.py migrate
```
the database will generate automatically

step4. run *populate_whisky.py* will insert some testing data into the database

```
python populate_whisky.py   
```
