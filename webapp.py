from os import environ
from flask import Flask, render_template
from crochet import setup, run_in_reactor, wait_for
import logging
logging.basicConfig()
# crochet.setup() MUST be called before any Autobahn or Twisted imports
setup()
from autobahn.twisted.wamp import Application  # noqa
from led_lib import ledOnOff

# global WAMP app
wapp = Application()

# global Flask app
app = Flask(__name__)

# this is a synchronous wrapper around the asynchronous WAMP code
@wait_for(timeout=1)
# RPC caller side:
def call(name, *args, **kwargs):
    return wapp.session.call(name, *args, **kwargs)

@app.route('/')
def homepage():
    x = 40
    y = 2
    kwargs = {
        'x': x,
        'y': y,
    }
    # call the "add2" remote procedure
    result = call(u'com.myapp.add2', **kwargs)
    env_var = environ.get("CROSSBAR_ROUTER_ADDRESS", u"ws://127.0.0.1:8080/ws")
    data = {
        'result': result,
        'crossbar_router_address': env_var,
    }
    data.update(kwargs)
    return render_template('home.html', data=data)

@app.route('/led') # URL to chose the mode
@app.route('/led/<status>') # on/off mode URL
def led(status = None): #None : optional parameter
    status_bool = False
    if status is not None and status == 'on':
        status_bool = True
    kwargs = {
        'status': status_bool,
    }
    # call the "led_turn_on" remote procedure
    call(u'com.myapp.led_turn_on', **kwargs)
    return render_template('led.html', **kwargs)

if __name__ == '__main__':
    # this will start the WAMP app on a background thread and setup communication
    # with the main thread that runs a (blocking) Flask server
    @run_in_reactor
    def start_wamp():
        env_var = environ.get("CROSSBAR_ROUTER_ADDRESS", u"ws://127.0.0.1:8080/ws")
        wapp.run(unicode(env_var), u"realm1", start_reactor=False)

    start_wamp()
    # now start the Flask dev server (which is a regular blocking WSGI server)
    #
    # before forking (only listen locally)
    # app.run(port=8050)
    # now the rasperry listen on port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
