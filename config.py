import pika
import ssl

RMQ_HOST = "seal-01.lmq.cloudamqp.com"
RMQ_PORT = 5671

RMQ_USER = "pbyprbxf"
RMQ_PASSWORD = "fiG86M-XmSJnpXhGc8_RALLjxw925XLJ"
RMQ_VIRTUAL_HOST = "pbyprbxf"

ssl_context = ssl.create_default_context()

print(ssl_context)

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    virtual_host=RMQ_VIRTUAL_HOST,
    credentials=pika.PlainCredentials(username=RMQ_USER, password=RMQ_PASSWORD),
    ssl_options=pika.SSLOptions(context=ssl_context)
)

def get_connection()-> pika.BlockingConnection:
    return pika.BlockingConnection(parameters=connection_params)