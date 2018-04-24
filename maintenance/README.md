# Drake's Brewing Co. Maintenance Database
IEOR 180 Project

Database that logs all maintenance-related equipment, services, schedules, & more. Web user interface to interact with data.

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
* project `settings.py` & `urls.py`

### db.sqlite3
> Project database file
* Contains all database information for project. SQLite3 database engine by default, but can be migrated to other engines in settings.py & running database migrations/merge. https://docs.djangoproject.com/en/2.0/topics/db/multi-db/#synchronizing-your-databases

### manage.py
> Python file to allow for terminal commands with project.
* in terminal `$ python manage.py [command]`
* commands: https://docs.djangoproject.com/en/2.0/ref/django-admin/
