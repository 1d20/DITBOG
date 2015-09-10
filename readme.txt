# create virtual enviroment
virtualenv env

# activate enviroment
source env/bin/activate

# dependencie for fabric
sudo apt-get -y install python-dev

# fix for PIL
sudo apt-get install libjpeg-dev

# install all requirements
pip install -r aok/requirements.txt

# make *.py scripts executable
chmod 777 -R aok	

# to project root
cd aok

# 'updatedb' + 'startdata' + 'testengine'
# create/update db and do all migrations
# fill db with test data
# add test engine to db and media folder
fab all

# python manage.py runserver
fab run
