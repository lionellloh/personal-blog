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
