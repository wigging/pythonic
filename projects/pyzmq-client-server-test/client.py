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
