# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

###[Unreleased]
## Added
- The crossbar router can be deployed on Heroku by following the README instructions (step 4)
- The webapp flask application can be deployed on Heroku by following the README instructions (step 4)
- The user is able to use the webapp from any platform which have access to the internet
- Fork new rpc, new templates from https://github.com/AndreMiras/flask-autobahn-to-heroku
- Add README instructions to use Heroku
- Add a ticket authentification between the crossbar node and the backend

##[v20161020step3] (Step 3)
### Added
- the crossbar router is no longer hosted by the raspberry pi
- create the "COSSBAR_ROUTER_ADDRESS" environment variable (export CROSSBAR_ROUTER_ADDRESS=ws://aaa.bbb.xxx.yyy:8080/ws)<br>

### Fixed
- delete unused java script code in home.html

##[v20101020step2] (step 2)
### Added
- change the home page

##[v20161014pm2] (step 1)
### Added
- the remote procedure to turn on/off the raspberry pi LED

##[v20161014]
### Added
- backend.py, presenting the "add2" remote procedure
- the flask web application webbapp.py (frontend)
- crochet lib (in webapp) to wait for asynchronous events
