#!/bin/bash
rm db.sqlite3

python manage.py makemigrations
python manage.py migrate
python manage.py shell


from django.contrib.auth import get_user_model
User = get_user_model()


root_user = User.objects.create_superuser(
	first_name='Ninja', last_name='Robot', username='mr-robot', email='mr_robot@mail.com', password='root1234')
root_user.save()


exit()
rm dump.json
python manage.py dumpdata --format json --indent 4 > dump.json
# python manage.py loaddata dump.json
python manage.py runserver

