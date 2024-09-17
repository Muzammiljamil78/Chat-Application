Basic text-based chat application in Python, we'll implement a simple client-server model using sockets. This will allow two users to exchange messages in real-time using the command line.

How to Use:
Run the server code in one terminal window: python chat_server.py
Run the client code in another terminal window: python chat_client.py
Type messages in the client terminal window to send to the server.
The server will receive the message and respond back to the client.
Type 'exit' to quit the chat application.


Features:
Real-time message exchange between two users using the command line
Simple client-server model using sockets
Supports multiple messages in a single connection

Limitations:
Only supports two users (one client and one server)
Does not handle multiple clients or concurrent connections
Does not implement any error handling or security measures
