
import asyncio
import json
import logging
import os
import threading
import time
import pika


_message_number = None

def push_audio_inference(channel:pika.BlockingConnection.channel):

    # Declare the queue
    channel.queue_declare(
        queue="radiostData", durable=True, exclusive=False, auto_delete=False
    )
    channel.queue_bind("radiostData",'radadspread_analytics',
                                 "radspdrdsc###0000*")
    channel.confirm_delivery()
    data = {
        "audio_name": "MTNJingle",
        "audio_uuid": "dfefdsewreffdefds",
        "is_analyzed": False,
        "station_freq": 96.9,
        "station_name": "Cool FM",
        "station_stm_url": "https:ok.com",
        "station_uuid": "hgghgbygyv",
        "is_active": False,
        "stream_pdate": "21-03-2023",
        "stream_stime": "00:00:00",
        "stream_etime": "00:00:00",
        "is_completed": False,
    }
    properties = pika.BasicProperties(app_id='example-publisher',
                                          content_type='application/json')


      
    i = 5
    while i < 10:
        try:
            print("ok")
            channel.basic_publish(
                'radadspread_analytics',
                "radspdrdsc###0000*",
                json.dumps(data).encode("utf-8"),
                properties
            )
            print("Message publish was confirmed")
            
        except pika.exceptions.UnroutableError:
            print("Message could not be confirmed")
        time.sleep(5)
    # connection.close()
