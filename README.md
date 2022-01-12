CRUD App

Install requirements
pip install -r requirements.txt

workon ipsr
cd machine_test

Database
python manage.py makemigrations
python manage.py migrate

Run the server
python manage.py runserver
