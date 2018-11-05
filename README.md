
You must specify the settings file since splitting it into dev & production versions:

    specify the settings when running python manage, E.g., 

        '--settings=site_core.settings.production' or 
        '--settings=site_core.settings.development'

    examples:

    migrate via 'python manage.py makemigrations ajax_polls --settings=site_core.settings.development'
    
    run the dev server 'python manage.py runserver --settings=site_core.settings.development'

    run the tests 'python manage.py test polls --settings=site_core.settings.development'

You may prefer to run the production version, but it relies on nginx & gunicorn.  These require your configuration.  I recommend using the development settings.  Production settings only run on the live site.
