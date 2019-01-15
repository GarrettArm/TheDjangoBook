
docker stop DjangoSiteDjango 
docker rm DjangoSiteDjango 
docker volume rm djangosite_mysite_project 

docker stop DjangoSitePostgres 
docker rm DjangoSitePostgres
docker volume rm djangosite_postgres_data 


docker system prune


docker-compose up -d --build
docker-compose run webapp python3 manage.py makemigrations shwagswap --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations vue_test --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations polls --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations etextbook --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations contact --settings=site_core.settings.production && docker-compose run webapp python3 manage.py makemigrations ajax_polls --settings=site_core.settings.production && docker-compose run webapp python3 manage.py migrate --settings=site_core.settings.production && docker-compose run webapp python3 manage.py createsuperuser --settings=site_core.settings.production && docker-compose run webapp python3 manage.py collectstatic --settings=site_core.settings.production

