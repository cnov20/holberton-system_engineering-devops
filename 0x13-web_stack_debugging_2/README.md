0x13. Web stack debugging #2

Tasks

0. Run Nginx as Nginx

The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it's a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.

Fix this container so that Nginx is running as the nginx user.

Requirements:

nginx must be running as nginx user
nginx must be listening on all active IPs on port 8080
You cannot use apt-get remove
Write a Bash script that configures the container to fit the above requirements