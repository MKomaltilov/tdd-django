New site start to work
======================

## Required packages
* nginx
* Python 3.8
* virtualenv + pip
* Git

## Nginx node configuration

* open nginx.tempate.conf
* change SITENAME for example like staging.my-domain.com

## Systemd service

* open gunicorn-systemd.template.service
* change SITENAME for example like staging.my-domain.com
* change PWD to real email password

## Folders structure

/home/user/

---sites

------SITENAME

----------database

----------source

----------static

----------virtualenv