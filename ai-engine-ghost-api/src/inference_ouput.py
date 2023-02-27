
import asyncio
import json
import logging
import os
import threading
import time
import pika



_message_number = None
import datetime

# Get current datetime and add 3 days
dt = datetime.datetime.now() + datetime.timedelta(days=3)

# Format datetime in ISO 8601 format
dt_str = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

# Get the current time
start_time = datetime.datetime.now().time()

# Calculate the end time 30 seconds later
end_time = (datetime.datetime.now() + datetime.timedelta(seconds=30)).time()

# Convert the times to strings
start_time_str = start_time.strftime("%H:%M:%S")
end_time_str = end_time.strftime("%H:%M:%S")
def push_audio_inference(channel:pika.BlockingConnection.channel):

    # Declare the queue
    channel.queue_declare(
        queue="radiostData", durable=True, exclusive=False, auto_delete=False
    )
    channel.queue_bind("radiostData",'radadspread_analytics',
                                 "radspdrdsc###0000*")
    channel.confirm_delivery()
    data =  [{
    'advertiser_id': 123,
    'title': 'My Campaign',
    'ga_file': 'ga_file.txt',
    'ga_pid': 456,
    'radio_stations': [
        {
            'station_name': 'Rhythm',
            'station_freq': 93.7,
            'station_state': 'Lagos',
            'station_stm_url':  "http://topradio.servotechstream.com:8550/;;",
            'stream_schedule': [
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                },
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str 
                }
            ]
        },
        {
            'station_name': 'Beat FM',
            'station_freq': 99.9,
            'station_state': 'PH',
            'station_stm_url':  "http://topradio.servotechstream.com:8550/;;",
            'stream_schedule': [
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str 
                },
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                }
            ]
        }
    ],
    'audio_name': 'audio.mp3',
    'audio_url': 'https://radioadspreadblob.blob.core.windows.net/radio-jingles/cool-fm-lagos-96.9/MTNJingle.wav'
},
{
    'advertiser_id': 7689,
    'title': 'My Campaign',
    'ga_file': 'ga_file.txt',
    'ga_pid': 456,
    'radio_stations': [
        {
            'station_name': 'Rhythm',
            'station_freq': 93.7,
            'station_state': 'Lagos',
            'station_stm_url':  "http://topradio.servotechstream.com:8550/;;",
            'stream_schedule': [
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                },
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                }
            ]
        },
        {
            'station_name': 'Beat FM',
            'station_freq': 99.9,
            'station_state': 'PH',
            'station_stm_url':  "http://topradio.servotechstream.com:8550/;;",
            'stream_schedule': [
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str 
                },
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                }
            ]
        }
    ],
    'audio_name': 'audio.mp3',
    'audio_url': 'https://radioadspreadblob.blob.core.windows.net/radio-jingles/cool-fm-lagos-96.9/MTNJingle.wav'
},
{
    'advertiser_id': 6178,
    'title': 'My Campaign',
    'ga_file': 'ga_file.txt',
    'ga_pid': 456,
    'radio_stations': [
        {
            'station_name': 'Rhythm',
            'station_freq': 93.7,
            'station_state': 'Lagos',
            'station_stm_url':  "http://topradio.servotechstream.com:8550/;;",
            'stream_schedule': [
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                },
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                }
            ]
        },
        {
            'station_name': 'Cool FM',
            'station_freq': 96.9,
            'station_state': 'Lagos',
            'station_stm_url':  "http://topradio.servotechstream.com:8550/;;",
            'stream_schedule': [
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                },
                {
                    'stream_pdate': dt_str,
                    'stream_stime': start_time_str,
                    'stream_etime': end_time_str
                }
            ]
        }
    ],
    'audio_name': 'audio.mp3',
    'audio_url': 'https://radioadspreadblob.blob.core.windows.net/radio-jingles/cool-fm-lagos-96.9/MTNJingle.wav'
}
]

    properties = pika.BasicProperties(app_id='example-publisher',
                                          content_type='application/json')
      
    i = 5
    while i < 10:
        try:
            for k,d in enumerate(data):
                channel.basic_publish(
                    'radadspread_analytics',
                    "radspdrdsc###0000*",
                    json.dumps(data[k]).encode("utf-8"),
                    properties
                )
                print("Message publish was confirmed")
            
        except pika.exceptions.UnroutableError:
            print("Message could not be confirmed")
        time.sleep(20)
    # connection.close()
