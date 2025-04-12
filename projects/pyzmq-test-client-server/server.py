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
