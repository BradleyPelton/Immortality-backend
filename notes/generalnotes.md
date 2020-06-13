

# Motiviation for naming convention
"You hear that Mr. Anderson? That is the sound of inevitability"
https://www.youtube.com/watch?v=x5m1A7zoIcc 


# More reading material for advanced migrations
https://docs.djangoproject.com/en/3.0/topics/migrations/
https://realpython.com/digging-deeper-into-migrations/
https://stackoverflow.com/questions/36153748/django-makemigrations-no-changes-detected


Entity Relationship Diagram (ERD)
https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/






### General notes
- Apparently you arent suposed to make the "inevitability" directory a python module. (i.e. DONT INCLUDE
A __init__ file in this directory). Doing so causes a lot of problems with manage.py test. See
https://stackoverflow.com/questions/21069880/running-django-tutorial-tests-fail-no-module-named-polls-tests