IP-Mirror
=========

Python3 daemon that listens on port 5000 and returns either ip or header information.

Getting Started:
================

Begin by ensuring you have Python installed as well as Flask.  Flask can be installed via pip.  It's a good idea to install the virtual python environment handler as well.  If you are using 'venv', simply activate your environment, set the FLASK_APP variable, and run flask:

$ cd ip-mirror

The following is for dev:

$ virtualenv -p python3 venv

$ . venv/bin/activate

Required for all environments (dev or otherwise):

(venv) $ pip install Flask

(venv) $ export FLASK_APP=ip-mirror.py

(venv) $ flask run

To exit from venv, simply deactivate:

(venv) $ deactivate

$

Get IP:
=======

$ curl http://localhost:5000/ip

127.0.0.1

== OR ==

$ curl http://localhost:5000/ip?format=json

{
      "ip": "127.0.0.1"
}

Get Headers:
============

$ curl http://localhost:5000/headers

Accept: */*, Host: localhost:5000, Content-Length: , Content-Type: , User-Agent: curl/7.43.0

== OR ==

$ curl http://localhost:5000/headers?format=json

{
  "Accept": "*/*",
  "Content-Length": "",
  "Content-Type": "",
  "Host": "localhost:5000",
  "User-Agent": "curl/7.43.0"
}

