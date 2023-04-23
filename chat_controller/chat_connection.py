from __main__ import app
import json
from models.Channels import Channels
from mysql_db.config import config
import mysql.connector as connector
from flask import Flask, request, Response
from chat_controller.pubnub_connection_util import connect_pubnub
from DAO.ChannelsDAO import ChannelsDAO
from DAO.ChannelsDAO1 import get_channel_wishcoordinator,get_channel_wishmaker 
from chat_controller.chat_pubnub import MySubscribeCallback
params = config()
conn = connector.connect(**params)
cur = conn.cursor()

pubnub = connect_pubnub()

'''@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    inp_data = request.get_json()
    sender_id = inp_data['sender_id']
    message = inp_data['message']
    if connect_pubnub():
        print("Connected to Pubnub successfully!")
    else:
        print("Error while connecting to pubnub")
    return Response(status = 200)
'''
def get_channel_name(request):
    user_name = request.form['user_name']
    user_role = request.form['user_role']
    #channelsDAO  = channelsDAO()
    #print("Created channelsDAO object")
    channel_name  = ""
    if user_role == 'wish_maker':
        channel_name = get_channel_wishmaker(user_name)
    else:
        channel_name = get_channel_wishcoordinator(user_name)
    return channel_name


@app.route('/assignCoordinator', methods=['GET'])
def create_channel():
    wish_maker = request.form['wish_maker']
    wish_coordinator = request.form['wish_coordinator']
    channel_name = f"{wish_maker}_{wish_coordinator}"    
    channels = Channels(wish_maker,wish_coordinator,channel_name)
    channelsDAO = ChannelsDAO(channels)
    if channelsDAO.create_channel():
        return json.dumps({'message':"Wish coordiator assigned successfully!"}), 200
    else:
        return json.dumps({'message':"Problem assigning coordinator...Please try again.."}), 200

def _callback(message,channel_name):
    return "{}: {}".format(message['user_name'], message['message'])

@app.route('/subscribe', methods=['GET'])
def subscribe_channel():
    print("Entering subscribe method")
    channel_name  = get_channel_name(request)
    print("channel_name",channel_name)
    pubnub.add_listener(MySubscribeCallback())
    result = pubnub.subscribe().channels(channel_name).execute()
    return json.dumps(result),200


@app.route('/sendMessage', methods=['POST'])
def publish_message():
    channel_name = get_channel_name(request)
    print(channel_name)
    message = request.form['message']
    user_name = request.form['user_name']
    msg_object = {user_name:message}
    pubnub.publish().channel(channel_name).message(message).sync()
    #pubnub.publish(channel=channel_name, message=msg_object)
    return json.dumps({'message':'Message sent successfully!'}),200

def history_callback(result, status):
    if not status.is_error():
        print('Message history:', result.messages)
    else:
        print('Failed to retrieve message history:', status.error_data.exception)

@app.route('/openChat',methods=['GET'])
def get_channel_history():
    channel_name = get_channel_name(request)
    response = pubnub.history().channel(channel_name).count(100).sync()
    if not response.status.is_error():
        message_hist = []
        for message in response.result.messages:
            message_hist.append(message.entry)
        return json.dumps({'messages':message_hist}),200
    else:
        print('Failed to retrieve channel history:', response.status.error_data.exception)
        return json.dumps({'messages':None}),200