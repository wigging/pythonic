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
