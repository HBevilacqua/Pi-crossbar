from __future__ import division
from platform import system, release
from os import environ
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from led_lib import ledOnOff
import argparse
import logging
logging.basicConfig()

class Component(ApplicationSession):
    """
    An application component providing procedures with different kinds
    of arguments.
    """

    def onConnect(self):
        self.join(self.config.realm, [u"ticket"], "backend_id")

    def onChallenge(self, challenge):
        if challenge.method == u"ticket":
            print("backend: WAMP-Ticket challenge received: {}".format(challenge))
            return "return_chall"
        else:
            raise Exception("Invalid authmethod {}".format(challenge.method))

    @inlineCallbacks
    def onJoin(self, details):

	self.args1 = self.config.extra['args1']
        print("backend[%s]: session attached" % self.args1)

	def on_topic(title):
            print("backend[%s] Got event: %s" % (self.args1, title))

        def platform():
            print "backend[%s] platform()" % self.args1
            return [system(), release()]

        def divide(a, b):
            print "backend[%s] divide()" % self.args1
            return a / b

        def led_turn_on(status):
            print "backend[%s] ledOnOff()" % self.args1
            ledOnOff(status)
	
        yield self.subscribe(on_topic, u'com.myapp.topic')#+self.args1)
        yield self.register(platform, u'com.myapp.platform')#+self.args1)
        yield self.register(divide, u'com.myapp.divide')#+self.args1)
        yield self.register(led_turn_on, u'com.myapp.led_turn_on')#+self.args1)
        print("backend[%s] Procedures registered; ready for frontend." % self.args1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", default="0")
    args = parser.parse_args()

    router_address = environ.get("ROUTER_ADDRESS", u"ws://127.0.0.1:8080/ws")
    print "router_address:", router_address

    runner = ApplicationRunner(
        unicode(router_address),
        u"realm1",
        extra={'args1':args.id}
    )
    runner.run(Component)
