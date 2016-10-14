from flask import Flask
from crochet import setup, run_in_reactor, wait_for

# this MUST be called _before_ any Autobahn or Twisted imports!
setup()

from autobahn.twisted.wamp import Application  # noqa


# our WAMP app
#
wapp = Application()

# this is a synchronous wrapper around the asynchronous WAMP code
#


@wait_for(timeout=1)
def publish(topic, *args, **kwargs):
    return wapp.session.publish(topic, *args, **kwargs)


# our Flask app
#
app = Flask(__name__)
app._visits = 0


@app.route('/')
def index():
    app._visits += 1
    publish(u'com.example.on_visit', app._visits, msg="hello from flask")
    return "Visit {}".format(app._visits)


if __name__ == '__main__':
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # this will start the WAMP app on a background thread and setup communication
    # with the main thread that runs a (blocking) Flask server
    #
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
