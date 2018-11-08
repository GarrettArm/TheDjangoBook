

The site is containerized: one docker for gunicorn+webapp, one for nginx, one for postgres, and a couple volumes for static files.  To run them:

  - git clone --recursive https://github.com/GarrettArm/DjangoSite
  - cd DjangoSite
  - docker-compose up --build  # assumes docker & docker-compose are installed
  - docker-compose run webapp python3 manage.py makemigrations shwagswap --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations vue_test --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations polls --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations etextbook --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations contact --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations ajax_polls --settings=site_core.settings.production && docker-compose run webapp python3 manage.py migrate --settings=site_core.settings.production && docker-compose run webapp python3 manage.py createsuperuser --settings=site_core.settings.production && docker-compose run webapp python3 manage.py collectstatic --settings=site_core.settings.production
  - 127.0.0.1:8000
  
To stop the containers & destroy the images/volumes:

  - docker-compose down
  - docker volume rm djangosite_media_volume djangosite_mysite_project djangosite_postgres_data djangosite_static_volume 



[[ The following are old instructions that might still have a kernel of truth ]]


You must specify the settings file since splitting it into dev & production versions:

    specify the settings when running python manage, E.g., 

        '--settings=site_core.settings.production' or 
        '--settings=site_core.settings.development'

    examples:

    migrate via 'python manage.py makemigrations ajax_polls --settings=site_core.settings.development'
    
    run the dev server 'python manage.py runserver --settings=site_core.settings.development'

    run the tests 'python manage.py test polls --settings=site_core.settings.development'

You may prefer to run the production version, but it relies on nginx & gunicorn.  These require your configuration.  I recommend using the development settings.  Production settings only run on the live site.
