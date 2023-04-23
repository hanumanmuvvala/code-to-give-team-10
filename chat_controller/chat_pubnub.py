from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'mySubscribeKey'
pnconfig.publish_key = 'myPublishKey'
pnconfig.user_id = "my_custom_user_id"
pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        print("In presenece")
        
        pass  # handle incoming presence data

    def status(self, pubnub, status):
        print(status.category)
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost

        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            print("Entered connected status")
            pass
            #pubnub.publish().channel(self.channel_name).message('Hello world!').pn_async(my_publish_callback)
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            print("Entered reconnected status")
            #self.handle_reconnect(pubnub)
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
        elif status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            # internet got lost, do some magic and call reconnect when ready
            pubnub.reconnect()
        elif status.category == PNStatusCategory.PNTimeoutCategory:
            # do some magic and call reconnect when ready
            pubnub.reconnect()

    def message(self, pubnub, message):
        # Handle new message stored in message.message
        print(message.message)
        sub_msgs = []
        for message in message.message:
            sub_msgs.append(message)
        return sub_msgs
    
    def handle_reconnect(self, pubnub):
        # This function is called when the SDK reconnects to the PubNub network
        # You can customize this function to perform any necessary actions upon reconnection
        pubnub.subscribe().channels("my_channel").execute()

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('my_channel').execute()