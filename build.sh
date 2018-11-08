!# /bin/sh
echo Building GarrettArm/DjangoSite
docker-compose up -d --build --no-cache
docker-compose run webapp python3 manage.py makemigrations contact polls etextbook vue_test ajax_polls shwagswap --settings=site_core.settings.production
docker-compose run webapp python3 manage.py migrate --settings=site_core.settings.production
docker-compose run webapp python3 manage.py createsuperuser --settings=site_core.settings.production
docker-compose run webapp python3 manage.py collectstatic --settings=site_core.settings.production
