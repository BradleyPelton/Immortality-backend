
https://stackoverflow.com/questions/35494035/django-migrate-doesnt-create-tables/35494384

##### my workflow  (CURRENT VERSION)

# Clear old database and migrations
rm dblsqlite3
rm -rf person/migrations/
rm -rf immortality_users/migrations/



# MANUALLY CREATE MIGRATIONS FOR EACH APP(order matters, models with one-to-one to other models)
        # I think you always have to run initial migrations like this (one at a time)
winpty python manage.py makemigrations person
winpty python manage.py makemigrations immortality_users

winpty python manage.py migrate


##### my workflow  (OLD VERSION)
- delete database (dblsqlite3)
- delete migrations in each app
- python manage.py makemigrations
- python manage.py migrate --run-syncdb  
# why --run-syncdb
# Synchronizing apps without migrations
# CREATE TABLES FOR MODELS WITHOUT MIGRATIONS
- winpty python manage.py createsuperuser

##### normal workflow
python manage.py makemigrations
python manage.py migrate


rm db.sqlite3



MIGRATIONS
migrations propagate changes to models into the database schema
e.g adding a new field requires a migration
