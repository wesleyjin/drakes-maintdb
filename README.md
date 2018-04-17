# drakes-maintdb
Files for IEOR 180 project
Drake's Brewing Co. Maintenance DB

## Getting started:
0. Install Django and Python dependencies. (Activate 'maintdb' virtual environment)
1. 'cd' into the folder named 'maintenance'
2. To start server, run the following in command line >> python manage.py runserver
	- Anytime you run this line, make sure the current directory is the root maintdb folder, with the file 'manage.py' in it.
3. Visit http://localhost:8000/admin in your web browser. Should see admin login

## Creating a New App:
> https://docs.djangoproject.com/en/2.0/intro/tutorial01/
1. To create a new app called 'newapp': python manage.py startapp newappp
2. Open the newapp/views.py and create some index page functionality.
3. In the newapp folder, create a 'urls.py' file and include url patterns
4. In the maintdb/urls.py file, include the reference to the urls file for the app.
5. Command line >> python manage.py runserver
6. Open localhost:8000/newapp/. Verify it is working with functionality created in #2.

## Database (SQLite) Setup: 
> https://docs.djangoproject.com/en/2.0/intro/tutorial02/
1. In the settings file of the project, set database ENGINE, NAME, TIME_ZONE.
2. Migrate in the necessary database tables by running: python manage.py migrate

## Creating & Activating Models (database schema/structures):
1. Edit the newapp/models.py file so it contains the models and classes desired.
2. Each class (table) inherits from another (usually models.Model), and has class variables that represents the attributes. See documentation for naming & how to implement relationships & foreign keys.
3. ACTIVATE the model by including the dotted path to its configuration class (usually  'newapp.apps.NewappConfig') in the INSTALLED_APPS setting of the settings.py file. 
4. Run: python manage.py makemigrations newapp (similar to a commit in git)
5. (Optional) check sql equivalent: python manage.py sqlmigrate newapp {migrateIDHERE}
6. Run: 'python manage.py migrate' to apply the model changes in the database
8. Add 'def __str__(self):' method to models to create string representations.
7. API: python manage.py shell
	- https://docs.djangoproject.com/en/2.0/intro/tutorial02/

## Using the admin site:
> Username: admin; PW: drakes180
1. Run: python manage.py runserver. Navigate to localhost:8000/admin
2. Login using above credentials.
3. Register objects that need admin interface by editing newapp/admin.py file
	- https://docs.djangoproject.com/en/2.0/intro/tutorial02/    (bottom of page)

## Views:
> A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template. For instance the most basic views for a poll app would be - index page (with all the questions), detail page (with question and vote), results page, vote action.
https://docs.djangoproject.com/en/2.0/intro/tutorial03/#writing-more-views
1. To create a new view, add a function to 'views.py' that takes in atleast one request argument and returns a HttpResponse object.
	- ex: def name_of_view(request, ...): return HttpResponse("contents here")
2. Add the new views to the url path by editing 'urls.py' and adding the corresponding path() calls for each. [See tutorial link for example]
3. Use Django database API to make views useful and not just some html text. Use templates to keep functionality but change web design: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#write-views-that-actually-do-something
4. Create a 'templates' directory in app directory. Create a .html file with html template code. Then update 'views.py' of the app to use the template. [Same link as 3]
5. Quickly prevent non-objects from having pages by using helper method: "get_object_or_404()" in the 'views.py' file: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#a-shortcut-get-object-or-404
6. Use the template system to get attributes or other information to view on the webpage: https://docs.djangoproject.com/en/2.0/intro/tutorial03/#use-the-template-system
7. HTML Template Creation Tool: https://getbootstrap.com/docs/3.3/components



