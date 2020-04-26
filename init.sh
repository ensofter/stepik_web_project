sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient
#sudo /etc/init.d/mysql restart
#mysql -uroot -e "create database stepic_web;"
#mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
#cd ask
#python3.5 manage.py makemigrations
#python3.5 manage.py migrate
sudo /etc/init.d/nginx restart
#sudo gunicorn --bind 0.0.0.0:8000 ask.wsgi
python3 ask/manage.py makemigrations
python3 ask/manage.py migrate --run-syncdb
python3 ask/manage.py runserver 0.0.0.0:8000
