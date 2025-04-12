---
title: Testing a PyZMQ Client and Server
date: April 12, 2025
---

The ZeroMQ context and socket for PyZMQ code can be patched and mocked using pytest and pytest-mock. This allows the code to be tested without having to run the server and connect the client. For the example discussed below, the client sends a request to the server, the request message is used by the server to execute a command, and the result of this command is sent back to the client. Finally, tests are demonstrated for the client and server codes.

## Client

Here is a client class for sending messages to the server. The `get_serial_number` and `add_numbers` methods send a message where `"command"` is a method name on the `Commands` class (see next section).

```python
# client.py

import zmq
from typing import Any

class Client:
    """Client for sending requests to server."""

    def __init__(self, address="tcp://localhost:5555"):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect(address)
        self.socket = socket

    def _send_message(self, command: str, *args: Any):
        msg = {"command": command, "args": args}
        self.socket.send_json(msg)

    def _recv_message(self) -> Any:
        msg: Any = self.socket.recv_json()
        return msg["result"]

    def get_serial_number(self) -> str:
        """Get serial number from server."""
        self._send_message("get_serial_number")
        serial_num = self._recv_message()
        return serial_num

    def add_numbers(self, x, y):
        """Add two numbers on server and get result."""
        self._send_message("add_numbers", x, y)
        total = self._recv_message()
        return total

    def close(self):
        self.socket.close()

def main():
    """Run the client."""
    client = Client()
    serial_num = client.get_serial_number()
    total = client.add_numbers(2.5, 19)
    client.close()

    print(f"Serial number: {serial_num}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()
```

## Server

Code for the `Commands` and `Server` classes is shown below. Methods on the `Commands` class act as commands that can be requested by the client. The `Server` class waits for a request message from the client and executes the proper command based on message received from the client.

```python
# server.py

import zmq
from typing import Any

class Commands:
    """Server commands that can be requested by client."""

    @staticmethod
    def get_serial_number() -> str:
        """Get serial number."""
        return "s4234asdf1e99"

    @staticmethod
    def add_numbers(x: float, y: float) -> float:
        """Add two numbers."""
        total = x + y
        return total

class Server:
    """Server for receiving/sending messages."""

    def __init__(self, address="tcp://localhost:5555"):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(address)
        self.socket = socket
        print("Server is running")

    def _recv_message(self) -> Any:
        msg: Any = self.socket.recv_json()
        print("\nReceived message:", msg)
        return msg

    def _send_message(self, result: Any):
        msg = {"result": result}
        self.socket.send_json(msg)
        print("Sent message:", msg)

    def run(self):
        """Run the server."""

        while True:
            # Wait for requests from client
            message = self._recv_message()

            # Get result from service
            command = message["command"]
            args = message["args"]
            result = getattr(Commands, command)(*args)

            # Send result to client
            self._send_message(result)

def main():
    """Server example."""
    server = Server()
    server.run()

if __name__ == "__main__":
    main()
```

## Running the example

First, run the server with `uv run server.py` then in a separate terminal session run the client with `uv run client.py`. By the way, [uv](https://docs.astral.sh/uv/) is an excellent tool for installing and running Python code, don't bother with other options.

## Testing

The tests for the client code are shown here. The ZeroMQ context is patched with the mocked socket. This allows the client tests to run without having to run the server and connect to it.

```{.python .pre1000}
# test_client.py

from client import Client
from pytest_mock import MockerFixture

def test_serial_number(mocker: MockerFixture):
    # Arrange
    mock_socket = mocker.Mock()
    mocker.patch("zmq.Context.socket", return_value=mock_socket)

    # Set up mocked socket methods
    mock_socket.send_json = mocker.Mock()
    mock_socket.recv_json = mocker.Mock(return_value={"result": "SN123456"})

    # Act
    client = Client()
    result = client.get_serial_number()

    # Assert
    mock_socket.send_json.assert_called_once_with({"command": "get_serial_number", "args": ()})
    mock_socket.recv_json.assert_called_once()
    assert result == "SN123456"

    client.close()

def test_add_numbers(mocker: MockerFixture):
    # Arrange
    mock_socket = mocker.MagicMock()
    mocker.patch("zmq.Context.socket", return_value=mock_socket)

    mock_socket.send_json = mocker.Mock()
    mock_socket.recv_json = mocker.Mock(return_value={"result": 42})

    # Act
    client = Client()
    result = client.add_numbers(19, 23)

    # Assert
    mock_socket.send_json.assert_called_once_with({"command": "add_numbers", "args": (19, 23)})
    mock_socket.recv_json.assert_called_once()
    assert result == 42

    client.close()
```

The tests for the server code are shown next. As with the client, the ZeroMQ context is patched with the mocked socket. This allows the server tests to run without having to connect to the client.

```{.python .pre1000}
# test_server.py

from server import Commands, Server
from pytest_mock import MockerFixture

def test_init(mocker: MockerFixture):
    mock_context = mocker.patch("server.zmq.Context")
    mock_socket = mocker.MagicMock()
    mock_context.return_value.socket.return_value = mock_socket

    server = Server("tcp://test:1234")

    mock_socket.bind.assert_called_once_with("tcp://test:1234")
    assert server.socket == mock_socket

def test_serial_number(mocker: MockerFixture):
    # Arrange
    mock_socket = mocker.MagicMock()
    mocker.patch("zmq.Context.socket", return_value=mock_socket)

    # Simulate client message and expected result
    mock_socket.recv_json.return_value = {"command": "get_serial_number", "args": []}

    # Patch the Commands.get_serial_number method
    service_mock = mocker.patch("server.Commands.get_serial_number", return_value="sn1234x89")

    server = Server()

    # Simulate one run loop iteration manually
    msg = server._recv_message()
    command = msg["command"]
    args = msg["args"]
    result = getattr(Commands, command)(*args)
    server._send_message(result)

    # Assert
    service_mock.assert_called_once()
    mock_socket.recv_json.assert_called_once()
    mock_socket.send_json.assert_called_once_with({"result": "sn1234x89"})

def test_add_numbers(mocker: MockerFixture):
    # Arrange
    mock_socket = mocker.MagicMock()
    mocker.patch("zmq.Context.socket", return_value=mock_socket)

    # Simulate client message and expected result
    mock_socket.recv_json.return_value = {"command": "add_numbers", "args": [2, 3]}

    # Patch the Commands.add_numbers method
    service_mock = mocker.patch("server.Commands.add_numbers", return_value=5)

    server = Server()

    # Simulate one run loop iteration manually
    msg = server._recv_message()
    command = msg["command"]
    args = msg["args"]
    result = getattr(Commands, command)(*args)
    server._send_message(result)

    # Assert
    service_mock.assert_called_once_with(2, 3)
    mock_socket.recv_json.assert_called_once()
    mock_socket.send_json.assert_called_once_with({"result": 5})
```

The example code and tests are available in the pythonic repo on GitHub at [pythonic/projects/pyzmq-test-client-server](https://github.com/wigging/pythonic/tree/main/projects/pyzmq-test-client-server).

## Further reading

See the [pytest](https://docs.pytest.org/en/stable/) and [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/) documentation for more information about developing and running tests in Python. See the [PyZMQ](https://pyzmq.readthedocs.io/en/latest/) documentation to learn more about using ZeroMQ with Python.
