import asyncio
import json
import threading
import time
import pika

# from src.internal.dependencies.generatefingerprint import generate_finger_print
async def return_publish(ch,properties,response):
    ch.basic_publish('radadspread_analytics', routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=json.dumps(response))

def on_message(ch, method_frame, properties, body):
        print(method_frame.delivery_tag)
        print("Received map: ", body,properties.reply_to,properties.correlation_id)
        response = {"status": True}
        # generate_finger_print(body)
        # ch.basic_ack(delivery_tag=method_frame.delivery_tag)
        ingression_thread=threading.Thread(target=return_publish, args=(ch,properties,response,))
        ingression_thread.start()




def LoadStationData():
    conn=pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@localhost:5672/"))
    #conn.ioloop.start()
    channel=conn.channel()
    channel.queue_declare('map_queue',
                      passive=False,
                      durable=True,
                      exclusive=False,
                      auto_delete=False)
 
    try:
        channel.basic_consume(on_message_callback=lambda ch, method, properties, body: on_message(ch, method,properties, body),
                      queue="map_queue")
        print('Waiting for map data...')
        channel.start_consuming()
    except pika.exceptions.AMQPConnectionError:
        print('Lost connection to RabbitMQ server. Retrying in 5 seconds...')
        time.sleep(5)
    except pika.exceptions.ChannelClosedByBroker:
        print('Channel closed by broker. Retrying in 5 seconds...')
        time.sleep(5)
    except Exception as e:
        print('Unknown error: {}. Retrying in 5 seconds...'.format(e))
        time.sleep(5)
    finally:
        channel.stop_consuming()