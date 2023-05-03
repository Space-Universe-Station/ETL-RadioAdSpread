import datetime

# Get current datetime and add 3 days
dt = datetime.datetime.now() + datetime.timedelta(days=0)

# Format datetime in ISO 8601 format
dt_str = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
print(type(dt_str))
# Get the current time
start_time = (datetime.datetime.now() + datetime.timedelta(seconds=10)).time()

# Calculate the end time 30 seconds later
end_time = (datetime.datetime.now() + datetime.timedelta(seconds=30)).time()

# Convert the times to strings
start_time_str = start_time.strftime("%H:%M:%S")
end_time_str = end_time.strftime("%H:%M:%S")

data =  [{
    'advertiser_id': 123,
    'title': 'My Campaign',
    'ga_file': 'ga_file.txt',
    'ga_pid': 352702775,
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
    'ga_pid': 352702775,
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
    'ga_pid': 352702775,
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
print(data)