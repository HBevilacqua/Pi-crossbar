# crossbar_demo

Example that demonstrate WebSocket programming with Autobahn|Python on Twisted.<br>
Fork from the twisted-native objects demo:<br>
https://github.com/crossbario/autobahn-python/tree/master/examples/twisted/wamp/overview<br>
<br>
These codes are a good starting point for own apps.<br>

###Setup
Prepare the virtualenv:
```
virtualenv venv
```

Switch to the virtualenv:
```
. venv/bin/activate
```

System level requirements:
```
pip install libssl-dev
pip install libffi-dev
```

Install deps
```
pip install autobahn
pip install twisted
pip install pyOpenSSL
pip install service_identity
pip install crossbar
```

Download code examples for frontend and backend:
```
wget https://raw.githubusercontent.com/crossbario/autobahn-python/master/examples/twisted/wamp/overview/backend.py
wget https://raw.githubusercontent.com/crossbario/autobahn-python/master/examples/twisted/wamp/overview/frontend.py
```

Change the AUTOBAHN_DEMO_ROUTER url (by default it is ws://localhost:8080/ws)
```
export AUTOBAHN_DEMO_ROUTER="wss://demo.crossbar.io/ws"
```


###Running the examples

Open three terminal sessions:

Running the router
```
crossbar init
crossbar start
```
Running the backend
```
python backend.py
```
Running the frontend
```
python frontend.py
```


#### error:
When I run
```
python backend.py
```
This error message appears
```sh
2016-10-11T15:03:29+0000 wamp.error.no_such_realm: no realm "crossbardemo" exists on this router<br>
^C2016-10-11T15:03:35+0000 Received SIGINT, shutting down.<br>
```
solution:<br>
<br>
The name of the realm in crossbar_demo/.crossbar/config.json<br>
must be the same in the backend.py and frontend.py files (here it is "realm1").<br>

```py
if __name__ == '__main__':
    runner = ApplicationRunner(
        environ.get("AUTOBAHN_DEMO_ROUTER", u"ws://127.0.0.1:8080/ws"),
        # u"crossbardemo",
        u"realm1",
    )
```
