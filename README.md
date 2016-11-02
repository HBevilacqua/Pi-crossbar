# Pi-crossbar

This application drives a LED via a raspberry pi.<br>
To better understand the crossbar concept, I divided this project into 4 parts.<br>
In the last part, the user is able to drive the LED from any platform (mobile device, computer, etc).<br>
For example, from my office I can drive the LED (and then the raspberry pi) which is located in my house.<br>

### Overview:
- Step 1: Understand the role of each node
- Step 2: Add a new RPC
- Step 3: See the crossbar node dependance
- Step 4: Use Heroku, a cloud platform as a service (PaaS)

### Step 1: Understand the role of each node
release: https://github.com/HBevilacqua/Pi-crossbar/releases/tag/v20161014pm
- cloud = local network
- all nodes are hosted on the Raspeberry Pi itself
- the web application uses crochet
- the backend implements a remote procedure, add2(x, y)
- the web app can call this procedure because it is connected to the same router and realm.
![GitHub Logo](screenshot/network.png)

##### Sources:
backend.py/frontend.py forked from https://github.com/HBevilacqua/crossbar_template

webapp.py forked from https://github.com/crossbario/autobahn-python/blob/224370cd9dda312fc0583b61ed416b3f4d0e00d0/examples/twisted/wamp/app/crochet/example1/server.py

templates/home.html forked from https://github.com/crossbario/autobahn-python/blob/224370cd9dda312fc0583b61ed416b3f4d0e00d0/examples/twisted/wamp/app/crochet/example1/client.html

### Step 2: Add a new RPC
release: https://github.com/HBevilacqua/Pi-crossbar/releases/tag/v20101020step2
- cloud = local network
- add the remote procedure to blink the raspberry pi LED

### Step 3: See the crossbar node dependance
release: https://github.com/HBevilacqua/Pi-crossbar/releases/tag/v20161020step3
- cloud = local network
- the crossbar router is no longer hosted by the raspberry pi but by another node (for example my computer)
- you have to set the CROSSBAR_ROUTER_ADDRESS environment variable  with the new crossbar ip address 
before launching the backend.py and the webapp.py

### Step 4: Use Heroku, a cloud platform as a service (PaaS)
##### 1. Deploy your owm crossbar router through Heroku
> **Note:**
> You have to create your account on Heroku.

  - Go to https://github.com/AndreMiras/crossbar-hello-python-to-heroku.git
  - Click on the "Deploy to Heroku" button
  - Give a name to your node, ex: "crossbarnode"
  - Your app can be found at https://crossbarnode.herokuapp.com/
  
##### 2. The backend runs on the raspberry pi to drive the LED
```
$ export CROSSBAR_ROUTER_ADDRESS=wss://crossbarnode.herokuapp.com/ws - start the backend: python backend.py 
```

##### 3. The flask application (frontend) runs also on Heroku
> **Note:**
> If you do not wish start your webapp from scratch, use a template forked from https://github.com/AndreMiras/flask-autobahn-to-heroku.git and follow the README instructions to start/shutdown your Heroku application.

Create a new git repository:
```
$ cd flask_app_on_heroku
$ git init
$ git add .
$ git commit -m "Initial commit"
```
Heroku uses a Procfile to determine what commands to use to start your app:
```
echo "web: gunicorn webapp:app" > Procfile
```
Download and extract the client tarball:
```
$ wget https://s3.amazonaws.com/assets.heroku.com/heroku-client/heroku-client.tgz
$ tar -xvzf heroku-client.tgz --directory ~/bin/
$ echo 'export PATH="${PATH}:~/bin/heroku-client/bin/"' >> ~/.bashrc
$ . ~/.bashrc
```
Create the app on Heroku:
```
$ heroku create
```
Design your webapp, commmit your local changes...<br>
Deploy and start the app:
```
$ git push heroku master
$ heroku config:set ROUTER_ADDRESS=wss://crossbarnode.herokuapp.com/ws
```

##### 4. The web browser runs on my mobile phone
Once the crossbar/webapp run on Heroku and the backend on your Raspberry pi, open a web browser and visit the web page to use the application.<br>
![GitHub Logo](screenshot/network_Step4.png)
