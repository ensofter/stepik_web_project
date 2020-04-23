cd ask
sudo unicorn --bind 0.0.0.0:8000 ask.wsgi
#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/wsgi.example
#sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_application
