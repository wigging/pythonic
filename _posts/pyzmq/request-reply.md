---
title: Request-Reply Pattern with PyZMQ
date: April 10, 2025
---

This demonstrates a simple request-reply pattern using the [PyZMQ](https://pyzmq.readthedocs.io/en/latest/) package for Python. In the example, the client sends a message to the server which replies back to the client.

## Client

The client socket connects to localhost port 5555 to send the message `"Hello"` to the server. After sending the message to the server, the client waits for the server's reply.

```python
# client.py

import zmq

# Create socket and connect on localhost port 5555
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send message to server
msg = "Hello"
socket.send_string(msg)
print("Sent:", msg)

# Get reply from server
message = socket.recv_string()
print("Received:", message)
```

## Server

The server socket binds to the localhost on port 5555 (`*` is localhost). After it receives a message from the client, the server replies with the message `"World"`.

```python
# server.py

import zmq

# Create socket and bind on localhost port 5555
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Server is running...")

while True:
    # Wait for message from client
    msg = socket.recv_string()
    print("Received:", msg)

    # Send a reply to client
    message = "World"
    socket.send_string(message)
    print("Sent:", message)
```

## Running the example

First, run the server in a terminal session as shown here:

```console
$ uv run server.py
Server is running...
```

Next, run the client in a different terminal session. The client will quickly receive the reply message from the server.

```console
$ uv run client.py
Sent: Hello
Received: World
```

After running the client, the server terminal will update with the following:

```console
$ uv run server.py
Server is running...
Received: Hello
Sent: World
```
