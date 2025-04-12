from client import Client
from pytest_mock import MockerFixture


def test_serial_number(mocker: MockerFixture):
    # Arrange
    mock_socket = mocker.Mock()
    mocker.patch("zmq.Context.socket", return_value=mock_socket)

    # Set up the mocked socket methods
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
