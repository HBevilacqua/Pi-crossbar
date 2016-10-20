from os import environ
from twisted.internet.defer import inlineCallbacks
from twisted.internet.task import LoopingCall
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from led_lib import ledOnOff

# This class presents our lib to the crossbar router
class MyComponent(ApplicationSession):
    # calls onJoin when it joins the realm1
    @inlineCallbacks 
    def onJoin(self, details):
        # RPC, callee side
        def add2(x, y):
            print "MyComponent.add2"
            return x + y
        # bind add2 method to the com.myapp.add2 uri
        yield self.register(add2, u'com.myapp.add2')

        # other RPC (raspberry)
        def led_turn_on(status):
            print "ledOnOff(status)"
            ledOnOff(status)
        yield self.register(led_turn_on, u'com.myapp.led_turn_on')

if __name__ == '__main__':
    # retrieves the environment variables
    env_var = environ.get("CROSSBAR_ROUTER_ADDRESS", u"ws://127.0.0.1:8080/ws")
    runner = ApplicationRunner(
        unicode(env_var),
        u"realm1",
    )
    runner.run(MyComponent)
