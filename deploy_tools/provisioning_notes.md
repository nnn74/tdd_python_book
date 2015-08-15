Provisioning a new site
=======================

## Required packages:

* nginx
* python3
* git
* pip
* virtualenv

Ubuntu:
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## nginx virtual host config

* see nginx.template.conf
* replace SITENAME with example, staging.my-domain.com

## Upstart job

* see gunicorn-upstart.template.conf
* replace SITENAME with example, staging.my-domain.com

## Folder structure:

/home/username
|__sites
   |__SITENAME
       |__database
       |__source
       |__static
       |__virtualenv

