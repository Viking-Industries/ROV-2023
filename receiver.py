import pyfirmata
import piVirtualWire as virtualwire

# Set up the board
board = pyfirmata.Arduino('COM3') # Change 'COM3' to match your Arduino's port
it = pyfirmata.util.Iterator(board)
it.start()

# Set up the receiver
receiver_pin = board.get_pin('d:2:i')
virtualwire.vw_set_rx_pin(receiver_pin)

# Set up the callback function to receive messages
def receive_message():
    buf = bytearray(100)
    buflen = len(buf)
    if virtualwire.vw_get_message(buf, buflen):
        message = buf.decode()
        print("Received message:", message)

# Set up the receiver loop to continuously check for incoming messages
virtualwire.vw_setup(2000, 500) # Set the receive frequency to 2000Hz, pulse width to 500µs
virtualwire.vw_rx_start()
while True:
    receive_message()