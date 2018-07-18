https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser -> This talks about the ModuleNotFoundError: No module named 'ConfigParser'issue when I tried to install mysql-python


When I was installing mysqlclient (recommended for python3), I
ran into Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/0f/b_80hhzn737cz2ppmf2vkyzm0000gn/T/pip-install-i4lkegvv/mysqlclient/

The solution

https://github.com/PyMySQL/mysqlclient-python/issues/169

 ModuleNotFoundError: No module named 'ConfigParser'
 Response: pip3 install ConfigParser

mysql command not found
export PATH=${PATH}:/usr/local/mysql/bin


2059, "Authentication plugin 'caching_sha2_password' cannot be loaded: dlopen
Solution:
Note: For MAC OS

Open MySQL from System Preferences > Initialize Database >
Type your new password.
Choose 'Use legacy password'
Start the Server again.
Now connect the MySQL Workbench


AttributeError: 'str' object has no attribute '_sa_instance_state'
https://stackoverflow.com/questions/33083772/sqlalchemy-attributeerror-str-object-has-no-attribute-sa-instance-state

ssh: The authenticity of host 'hostname' can't be established
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no


https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu

Python locale error: unsupported locale setting
https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting

TODO:
Write a script for this: http://songhuiming.github.io/pages/2016/10/30/set-up-flask-web-host-on-digitalocean-vps/

Skipping adding existing rule (v6)
https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-16-04

nginx - nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
https://stackoverflow.com/questions/14972792/nginx-nginx-emerg-bind-to-80-failed-98-address-already-in-use

Hosting
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04


Secure Copy
scp -r ./personal-blog/ lion@159.65.7.56:Setting up mysql on ubuntu vps

https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04


sqlalchemy.exc.OperationalError: (_mysql_exceptions.OperationalError) (1045, "Access denied for user 'pb_admin'@'localhost' (using password: YES)") (Background on this error at: http://sqlalche.me/e/e3q8)

Your password does not satisfy the current policy requirements
https://stackoverflow.com/questions/43094726/your-password-does-not-satisfy-the-current-policy-requirements?rq=1


------- THIS IS THE MAIN SHIT
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04
--------

bad gateway could be due to the lack of file "myproject.sock" inside ~/myproject
