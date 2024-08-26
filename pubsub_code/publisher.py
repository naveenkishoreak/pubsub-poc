from google.cloud import pubsub_v1

project_id = 'naveen-dbt-project'
topic_id = 'order_topic'

# create publisher client

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Publish the message

message_data = [f'{time} naveen' for time in range(10)] 

for message in message_data:
    future = publisher.publish(topic_path, message.encode('utf-8'))

    print(f"Published message ID: {future.result()}")