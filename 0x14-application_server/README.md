0x14. Application server #0

You web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. And while a web server can also serve dynamic content, the task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

Tasks

0. Welcome Gunicorn

Let's serve what you built for AirBnB clone - Web framework on web01.

Requirements:

Git clone your Airbnb clone
Install Gunicorn and other libraries required by your application
Create an Upstart script that starts Gunicorn to serve web_flask/0-hello_route.py from your Airbnb clone
Setup Nginx so that the route /airbnb-onepage/ points to Gunicorn
Nginx must serve this locally but also on its public IP on port 80
Provide the Upstart config file you wrote, upload it as answer file with the name 0-welcome_gunicorn-upstart_config
Provide the Nginx config file you wrote, upload it as answer file with the name 0-welcome_gunicorn-nginx_config
Do not forget that logs are your friends, for nginx for instance, they are located in /var/log/nginx. Also init-checkconf is your friend to check your upstart config files.


1. Pass a query parameter

Let's serve what you built for AirBnB clone - Web framework on web01.

Requirements:

Create an Upstart script that starts Gunicorn to serve web_flask/6-number_odd_or_even.py from your Airbnb clone
Setup Nginx so that the route /airbnb-dynamic/ points to Gunicorn
Nginx must serve this locally but also on its public IP on port 80
Provide your Upstart config file, name it 1-pass_parameter-upstart_config
Provide your Nginx config file, name it 1-pass_parameter-nginx_config