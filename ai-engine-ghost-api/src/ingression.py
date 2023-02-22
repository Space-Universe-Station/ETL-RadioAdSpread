import pika

# from src.internal.dependencies.generatefingerprint import generate_finger_print


def on_message(channel, method_frame, header_frame, body):
        print(method_frame.delivery_tag)
        print("read from queue",body)
        # generate_finger_print(body)
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

def LoadStationData():
    conn=pika.BlockingConnection(
            pika.URLParameters("amqp://guest:guest@localhost:5672/"))
    #conn.ioloop.start()
    channel=conn.channel()
    channel.queue_declare('ai_uplink_queue',
                      passive=False,
                      durable=True,
                      exclusive=False,
                      auto_delete=False)
    channel.queue_bind('ai_uplink_queue','radadspread_analytics','radspdaiuplk')
    channel.basic_consume('ai_uplink_queue', on_message)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()