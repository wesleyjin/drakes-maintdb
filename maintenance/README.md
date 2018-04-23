# Drake's Brewing Co. Maintenance Database
IEOR 180 Project

## Directories & Files:
* equipment 
> Plant locations, equipment, and parts
	* Models (entities) - Equipment, Location, Parts
	* Views (webpages) - equipment list/detail, location_list, location-equipment_list

* logs
> Maintenance Logs, Maintenance Services
	* Models (entities) - Log, Service (PMActivity)
	* Views - log list, recent/sorted logs, scheduled_services list

* maintenance
> project settings directory
	* Project 'settings.py' & master 'urls.py'

* db.sqlite3
> Project database file
	* Contains all database information for project. Can be converted to other SQLDatabase files in settings.py & running database migrations. https://docs.djangoproject.com/en/2.0/topics/db/multi-db/#synchronizing-your-databases

* manage.py
> Python file to allow for terminal commands with project.
	* in terminal $ python manage.py [command]
	* commands: https://docs.djangoproject.com/en/2.0/ref/django-admin/
