from Arduino import Arduino
from time import sleep

board = Arduino("115200", port="COM3")

board.Servos.attach(13)

board.Servos.writeMicroseconds(13, 1100)
sleep(5)

while True:
    board.Servos.writeMicroseconds(13, 1300)

