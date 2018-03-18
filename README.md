# drakes-maintdb
Files for IEOR 180 project
Drake's Brewing Co. Maintenance DB

Getting started:
0. (Activate 'maintdb' environment)
1. 'cd' into the folder named 'maintdb'
2. To start server, run the following in command line: python manage.py runserver
(If necessary, apply necessary migrations: python manage.py migrate)
3. Visit http://127.0.0.1:8000/ in your web browser. Should see rocket graphic & Django.

Creating a New App: https://docs.djangoproject.com/en/2.0/intro/tutorial01/
1. To create a new app called 'newapp': python manage.py startapp newappp
2. Open the newapp/views.py and create some index page functionality.
3. In the newapp folder, create a 'urls.py' file and include url patterns
4. In the maintdb/urls.py file, include the reference to the urls file for the app.
5. Command line: python manage.py runserver
6. Open localhost:8000/newapp/. Verify it is working with functionality created in #2.



4. Start first (polls) app & view: 
5. Connect database: https://docs.djangoproject.com/en/2.0/intro/tutorial02/