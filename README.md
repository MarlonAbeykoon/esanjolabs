# esanjolabs
Clone the repo
```
git clone https://github.com/MarlonAbeykoon/esanjolabs.git
```

Create a DB in mySQL and update the SQLALCHEMY_DATABASE_URI in app/instance/config.py SQLALCHEMY_DATABASE_URI section with username password and db

Go inside the directory
```
cd esanjolabs
```

Give permission to install.sh
```
sudo chmod 777 install.sh
```

Run the shell script which creates a virtual env in python 3.5, set a flask env variable and run requirement.txt
```
./install.sh
```
Activate the virtual environment
```
source ./venv/bin/activate
```
Run flask app
```
flask run
```
