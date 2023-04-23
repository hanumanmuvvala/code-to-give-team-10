from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException
from pubnub.enums import PNStatusCategory
from pubnub.pubnub import SubscribeListener, PubNub

def connect_pubnub():
    print("Conneting to PubNUB!!!")
    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = 'sub-c-20d104fc-16c3-4c53-a5be-96dbb5899503'
    pnconfig.publish_key = 'pub-c-26796ddc-eb66-4abc-9aac-3f9df0604e66'
    pnconfig.user_id = "hanumanmuvvala28@gmail.com"
    pnconfig.reconnect_policy = "linear"
    pnconfig.reconnect_callback = reconnect_callback
    pubnub = PubNub(pnconfig)
    if pubnub:
        print("Connected to pubnub successfully!")
        return pubnub
    else:
        return None

def publish(pubnub):
    '''
    
    try:
        envelope = pubnub.publish().channel("my_channel").message({
            'name': 'Alex',
            'online': True
        }).sync()
        print("publish timetoken: %d" % envelope.result.timetoken)
        print(envelope.status)
        #if envelope.status.isError == True:
        #    return False
        #else:
        #    return True
    except PubNubException as e:
        print(e)
    return True
    '''
    result = pubnub.publish().channel("my_channel").message(["hello", "there"]) \
    .meta({'name': 'Alex'}).pn_async(publish_callback)
    return result

def publish_callback(result, status):

    return status.is_error()

def reconnect_callback(pubnub):
    print("Reconnected to PubNub network")
    pubnub.subscribe().channels("my_channel").execute()

class MySubscribeListener(SubscribeListener):
    
    def __init__(self,pubnub,channel_name):
        self.channel_name  = channel_name
        #envelope = pubnub.set_state().channels(channel_name).state(state).sync()

    def status(self, pubnub, status):
        pass

    def message(self, pubnub, message):
        return message

    def presence(self, pubnub, presence):
        pass

def subscribe(pubnub,channel_name):
    my_listener = MySubscribeListener(pubnub,channel_name)
    pubnub.add_listener(my_listener)
    print(channel_name)
    pubnub.subscribe().channels(channel_name).execute()