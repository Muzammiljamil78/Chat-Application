import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 12345))

print("Connected with Jarvis. Type 'exit' to quit.")

while True:
    # Send message to server
    message = input("Alexa: ")
    if message.lower() == "exit":
        break
    client_socket.sendall(message.encode())

    # Receive response from server
    response = client_socket.recv(1024).decode()
    print("Jarvis:", response)

# Close the connection
client_socket.close()

