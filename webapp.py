from flask import Flask
from crochet import setup, run_in_reactor, wait_for
# crochet.setup() MUST be called before any Autobahn or Twisted imports
setup()
from autobahn.twisted.wamp import Application  # noqa

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
def index():
    x = 40
    y = 2
    kwargs = {
        'x': x,
        'y': y,
    }
    # call the "add2" remote procedure
    result = call(u'com.myapp.add2', **kwargs)
    print "add result:", result
    return "x: %s, y: %s, result: %s" % (x, y, result)


if __name__ == '__main__':
    # this will start the WAMP app on a background thread and setup communication
    # with the main thread that runs a (blocking) Flask server
    @run_in_reactor
    def start_wamp():
        wapp.run(u"ws://127.0.0.1:8080/ws", u"realm1", start_reactor=False)

    start_wamp()

    # now start the Flask dev server (which is a regular blocking WSGI server)
    #
    # before forking (only listen locally)
    # app.run(port=8050)
    # now the rasperry listen on port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
