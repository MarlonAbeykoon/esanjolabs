#!/usr/bin/env bash

pip install virtualenv
virtualenv -p /usr/bin/python3.5  venv
echo 'export FLASK_APP=app/app.py' >> ./venv/bin/activate
source ./venv/bin/activate
sudo venv/bin/pip install -r requirement.txt
python manage.py createdb -t
