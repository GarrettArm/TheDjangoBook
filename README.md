

The site is containerized: one docker for gunicorn+webapp, one for nginx, one for postgres, and a couple volumes for static files.  To run them:

  - git clone --recursive https://github.com/GarrettArm/DjangoSite
  - create a file django_secret_key.txt at parent of DjangoSite folder, containing text "PROD_SECRET_KEY=SomeFiftyCharacterRandomStringUnquoted"
  - cd DjangoSite
  - docker-compose up -d --build
  - docker-compose run webapp python3 manage.py makemigrations shwagswap --settings=site_core.settings.development && docker-compose run webapp python3 manage.py makemigrations vue_test --settings=site_core.settings.development && docker-compose run webapp python3 manage.py makemigrations polls --settings=site_core.settings.development && docker-compose run webapp python3 manage.py makemigrations etextbook --settings=site_core.settings.development && docker-compose run webapp python3 manage.py makemigrations contact --settings=site_core.settings.development && docker-compose run webapp python3 manage.py makemigrations ajax_polls --settings=site_core.settings.development && docker-compose run webapp python3 manage.py migrate --settings=site_core.settings.development && docker-compose run webapp python3 manage.py createsuperuser --settings=site_core.settings.development && docker-compose run webapp python3 manage.py collectstatic --settings=site_core.settings.development

 - app is at localhost or 127.0.0.1
  
To stop:

  - docker-compose down

To remove a container & it's volume:
  - docker system prune
  - docker stop DjangoSiteDjango 
  - docker rm DjangoSiteDjango
  - docker volume rm djangosite_mysite_project 



[[ The following are old instructions that might still have a kernel of truth ]]


You must specify the settings file since splitting it into dev & production versions:

    specify the settings when running python manage, E.g., 

        '--settings=site_core.settings.production' or 
        '--settings=site_core.settings.development'

