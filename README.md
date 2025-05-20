# CS361_MicroserviceA
Microservice for Daniel Green

## Getting Started
This microservice communicates over ZeroMQ which can be installed via pip like so:
```bash
pip install pyzmq
```

## Usage
ZeroMQ communicates over a network. The server file currently sets the socket to bind over the local network at port 5555.
Simply request the microservice for a string by sending the text 'MSG'. After sending this, a random, encouraging string of text will be returned.
To end the connection, send the text 'Q'.

If any message other than 'MSG' or 'Q' is sent, the microservice will respond with 'ERR' to indicate an error has occured. The connection will not terminate until 'Q' is sent.

## Example Request and Receival
```python
#request
socket.send_string('MSG')

#receival
encouragingMessage = socket.recv()
```
## UML Sequence Diagram
