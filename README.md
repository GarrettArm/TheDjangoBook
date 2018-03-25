
Since splitting the settings file into dev & production versions:

    specify the settings when running python manage, E.g., 

        '--setting=mysite.setting.production' or 
        '--setting=mysite.settings.development'

    examples:

    migrate via 'python manage.py makemigrations ajax_polls --setting=mysite.settings.production'
    
    run the dev server 'python manage.py runserver --setting=mysite.settings.development'

    run the tests 'python manage.py test polls --setting=mysite.settings.development'

running 'gunicorn --workers 3 --bind unix:/tmp/mysite_project.sock mysite.wsgi' automatically does the production version through gunicorn & nginx, due to how wsgi.py is configured.

running 'python manage.py runserver' will no run any version, as the setting must be specified.  It seems safer to me that way.
