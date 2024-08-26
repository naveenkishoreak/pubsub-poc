# pubsub-poc

### Steps to Implement Pub/Sub Messaging

1. **Create a Pub/Sub Topic**: Start by creating a topic in Google Cloud Pub/Sub. This is where the Publisher will send messages.

2. **Create a Subscription**: Set up a subscription for the topic created above. This allows the messages sent by the Publisher to be pulled from the topic by the Subscriber.

3. **Develop Publisher and Subscriber Code**: Write the Python code for both the Publisher and Subscriber to handle message publishing and receiving.

4. **Run the Subscriber**: The Subscriber will run indefinitely, continuously listening for new messages until manually interrupted.

5. **Message Acknowledgment**: Once a message is received, the Subscriber will pull and acknowledge it. This acknowledgment ensures that the message is deleted from the queue and not resent.
