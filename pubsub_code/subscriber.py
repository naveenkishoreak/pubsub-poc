from google.cloud import pubsub_v1

project_id = 'naveen-dbt-project'
subscription_id = 'notification_sub'

# create Subscriber Client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)


def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()
    
# Subscribe to the subscription
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}...")

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()