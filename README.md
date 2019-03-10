

The site is containerized: one docker for gunicorn+webapp, one for nginx, one for postgres. Plus a couple of volumes for non-ephemeral data.  To run them:

  - ./build.sh
  - app is at localhost or 127.0.0.1

To stop:

  - docker-compose down

Rebuilding app server (i.e., after editing code):

  - ./wipe_volumes.sh

[[ The following are old instructions that might still have a kernel of truth, these are baked into mysite_project/site_core/Dockerfile ]]


You must specify the settings file since splitting it into dev & production versions:

    specify the settings when running python manage, E.g., 

        '--settings=site_core.settings.production' or 
        '--settings=site_core.settings.development'

