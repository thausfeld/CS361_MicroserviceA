# Microservice itself that upon request, sends an encouraging message to the client

import datetime
import zmq
import json

# Establish the connection settings on the network
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Accept requests indefinetly until prompted to "shut down"
while True:
    message = socket.recv().decode()
    print(f'Recieved client message: {message}')

    # Determine if client wants a response or to shut down
    if len(message) > 0:
        if message == 'Q':
            print('Client has requested to close connection!')
            break
        if message != 'MSG':
            socket.send_string('ERR')

        # Generate a random number using time
        randInt = datetime.datetime.now()
        randInt = str(((randInt.second) * (randInt.microsecond)) % 100)

        # Gather data from local json file for the client
        with open('encouragement.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            friendlyMessage = data[randInt]
            file.close()

        # Send the gathered data to the client
        print(f'Sending response: {friendlyMessage}')
        socket.send_string(friendlyMessage)

context.destroy()
