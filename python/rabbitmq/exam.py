import pika
import ssl

def main():
    url = ""
    parameters = pika.URLParameters(url)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    parameters.ssl_options = pika.SSLOptions(context)

    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        EXCHANGE_NAME = "exchange.a1e53d4c-00c2-4a36-8b48-0ddc3ab0f126"
        ROUTING_KEY = "a1e53d4c-00c2-4a36-8b48-0ddc3ab0f126"
        QUEUE_NAME = "exam"
        MESSAGE = "Hi CloudAMQP, this was fun!"

        try:
            channel.exchange_declare(
                exchange=EXCHANGE_NAME,
                exchange_type='direct',
                durable=True
            )

            channel.queue_declare(
                queue=QUEUE_NAME,
                durable=True
            )

            channel.queue_bind(
                exchange=EXCHANGE_NAME,
                queue=QUEUE_NAME,
                routing_key=ROUTING_KEY
            )

            # delivery_mode=2 for persistence
            channel.basic_publish(
                exchange=EXCHANGE_NAME,
                routing_key=ROUTING_KEY,
                body=MESSAGE,
                properties=pika.BasicProperties(
                    delivery_mode=2  #  persistent message 
                )
            )

            print(f"Message sent: {MESSAGE}")

        finally:
            try:
                channel.queue_unbind(
                    queue=QUEUE_NAME,
                    exchange=EXCHANGE_NAME,
                    routing_key=ROUTING_KEY
                )
                channel.exchange_delete(exchange=EXCHANGE_NAME)
                print("Cleanup completed successfully")
            except Exception as cleanup_error:
                print(f"Error during cleanup: {cleanup_error}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        try:
            if 'connection' in locals() and connection.is_open:
                connection.close()
                print("Connection closed successfully")
        except Exception as close_error:
            print(f"Error closing connection: {close_error}")

if __name__ == "__main__":
    main()