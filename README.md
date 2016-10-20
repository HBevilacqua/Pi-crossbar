# Pi-crossbar

Flask Web application with Autobahn WAMP code using Crochet.

### Sources:
backend.py/frontend.py forked from https://github.com/HBevilacqua/crossbar_template

webapp.py forked from https://github.com/crossbario/autobahn-python/blob/224370cd9dda312fc0583b61ed416b3f4d0e00d0/examples/twisted/wamp/app/crochet/example1/server.py

templates/home.html forked from https://github.com/crossbario/autobahn-python/blob/224370cd9dda312fc0583b61ed416b3f4d0e00d0/examples/twisted/wamp/app/crochet/example1/client.html

### Step 1:
release: https://github.com/HBevilacqua/Pi-crossbar/releases/tag/v20161014pm
- cloud = local network
- all nodes are hosted on the Raspeberry Pi itself
- the web application uses crochet
- the backend implements a remote procedure, add2(x, y)
- the web app can call this procedure because its connected to the same router and realm.
![GitHub Logo](screenshot/network.png)

### Step 2:
release: https://github.com/HBevilacqua/Pi-crossbar/releases/tag/v20161020step2
- add the remote procedure to blink the raspberry pi LED

### Step 3 (current):
release: https://github.com/HBevilacqua/Pi-crossbar/releases/tag/v20161020step3
- the crossbar router is no longer hosted by the raspberry pi but by another node (for example my computer)
- you have to set the CROSSBAR_ROUTER_ADDRESS environment variable (raspberry side) with the new crossbar ip address 
before launchong the backend.py and the webapp.py
