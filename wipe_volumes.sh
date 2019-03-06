docker system prune

docker stop djangosite_webapp_run_1
docker rm djangosite_webapp_run_1
docker stop djangosite_webapp_run_2
docker rm djangosite_webapp_run_2
docker stop djangosite_webapp_run_3
docker rm djangosite_webapp_run_3
docker stop djangosite_webapp_run_4
docker rm djangosite_webapp_run_4
docker stop djangosite_webapp_run_5
docker rm djangosite_webapp_run_5
docker stop djangosite_webapp_run_6
docker rm djangosite_webapp_run_6
docker stop djangosite_webapp_run_7
docker rm djangosite_webapp_run_7
docker stop djangosite_webapp_run_8
docker rm djangosite_webapp_run_8
docker stop djangosite_webapp_run_9
docker rm djangosite_webapp_run_9
docker stop djangosite_webapp_run_10
docker rm djangosite_webapp_run_10
docker stop djangosite_webapp_run_11
docker rm djangosite_webapp_run_11
docker stop djangosite_webapp_run_12
docker rm djangosite_webapp_run_12
docker stop djangosite_webapp_run_13
docker rm djangosite_webapp_run_13
docker stop djangosite_webapp_run_14
docker rm djangosite_webapp_run_14
docker stop djangosite_webapp_run_15
docker rm djangosite_webapp_run_15

docker stop DjangoSiteDjango 
docker rm DjangoSiteDjango
docker volume rm djangosite_mysite_project
docker image rm djangosite_webapp:latest

# docker stop DjangoSitePostgres 
# docker rm DjangoSitePostgres
# docker volume rm djangosite_postgres_data

docker volume ls
docker image ls
docker ps -a

docker-compose up -d --build
docker-compose run webapp python3 manage.py makemigrations vue_test polls etextbook contact ajax_polls shwagswap --settings=site_core.settings.development
docker-compose run webapp python3 manage.py migrate --settings=site_core.settings.development
# docker-compose run webapp python3 manage.py createsuperuser --settings=site_core.settings.development
docker-compose run webapp python3 manage.py collectstatic --settings=site_core.settings.development
