# Run this script to setup stuff without having to reinstall everything

python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser