=====
Notes
=====

Notes is a Django app that allows you to add notes to your models.
Notes was designed to work with Django Rest Framework.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "notes" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'notes',
    ]

2. Include the notes URLconf in your project urls.py like this::

    path('notes/', include('notes.urls')),

3. Run ``python manage.py migrate`` to create the notes models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a note (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to see all notes.
