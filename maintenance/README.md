# Drake's Brewing Co. Maintenance Database
IEOR 180 Project

Database that logs all maintenance-related equipment, services, schedules, & more. Web user interface to interact with data.

## Required Dependencies:
* Python 3.6 - https://www.python.org/downloads/
### Python Packages
* Django 2.0 - `pip install django` https://docs.djangoproject.com/en/2.0/intro/install/
* django_filters - `pip install django-filter` http://django-filter.readthedocs.io/en/latest/guide/install.html
* django_tables2 - `pip install django-tables2` https://django-tables2.readthedocs.io/en/latest/pages/installation.html
* We suggest installing this version of Python and django installations in a virtual environment to prevent updates from causing bugs in project code.

### Running the Server
0. (Activate virtual environment)
1. `python manage.py runserver`
2. Using browser navigate to `localhost:8000/`


## Directories & Files:
### equipment 
> Plant locations, equipment, and parts

* Models (entities) - Equipment, Location, Parts
* Views (webpages) - equipment list/detail, location_list, location-equipment_list

### logs
> Maintenance Logs, Maintenance Services
* Models (entities) - Log, Service (PMActivity)
* Views - log list, recent/sorted logs, scheduled_services list

### maintenance
> project setting and configuration directory
* Default Models used: User (as employee entity)
* contains project `settings.py` & master `urls.py`

### media
> directory of file uploads
* files uploaded with a log entry or equipment entry are saved locally in this directory

### db.sqlite3
> Project database file
* Contains all database information for project. SQLite3 database engine by default, but can be migrated to other engines in settings.py & running database migrations/merge. https://docs.djangoproject.com/en/2.0/topics/db/multi-db/#synchronizing-your-databases

### manage.py
> Python file to allow for terminal commands with project.
* in terminal `$ python manage.py [command]`
* commands: https://docs.djangoproject.com/en/2.0/ref/django-admin/

### Warnings
> FOR INTERNAL/LOCAL USE ONLY
* some security vulnerabilities include:
* ability to upload any type of file in FileFields (code injection)
* ability to access any media file uploaded to FileFields
