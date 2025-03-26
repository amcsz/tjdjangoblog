# Run this script to setup stuff without having to reinstall everything

python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python djangoblog/manage.py makemigrations blog
python djangoblog/manage.py migrate
python djangoblog/manage.py createsuperuser