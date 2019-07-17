# for ((i=1;i<15;i++)); do
#     docker stop djangosite_webapp_run_$i
#     docker rm djangosite_webapp_run_$i
# done

# docker stop DjangoSiteDjango 
# docker rm DjangoSiteDjango
# docker volume rm djangosite_mysite_project
# docker image rm djangosite_webapp:latest

# docker stop DjangoSitePostgres 
# docker rm DjangoSitePostgres
# docker volume rm djangosite_postgres_data

# docker system prune
docker-compose down
docker volume rm djangosite_mysite_project

docker volume ls
docker image ls
docker ps -a

docker-compose up -d --build
docker-compose run webapp python3 manage.py makemigrations milage blog polls etextbook contact ajax_polls shwagswap --settings=site_core.settings.development
docker-compose run webapp python3 manage.py migrate --settings=site_core.settings.development
# docker-compose run webapp python3 manage.py createsuperuser --settings=site_core.settings.development
docker-compose run webapp python3 manage.py collectstatic --settings=site_core.settings.development
