import os
from flask import Flask
from mysql_db.connect import connect_db
from flask_cors import CORS

from  chat_controller.pubnub_connection_util import connect_pubnub,publish,subscribe
from  chat_controller.chatgpt import subscribe_to_channel,publish_message,get_channel_history
app = Flask(__name__)
CORS(app)
import chat_controller.chat_connection

def main():
    conn = connect_db()
    if conn is None:
        print("Unable to connect to database")
        conn.close()
    else:
        '''pubnub = connect_pubnub()
        if pubnub:
            print("History: ",get_channel_history(pubnub,'my_channel'))
            # Call the functions to subscribe to a channel and publish a message
            subscribe_to_channel(pubnub,'my_channel')
            publish_message(pubnub,'my_channel', 'How u doing!')
            
            if not publish(pubnub):
                print("Published successfully to My channel")
                subscribe(pubnub,"my_channel")
            else:
                print("Publish Failed")'''
        app.run()
        

if __name__ == '__main__':
    main()
