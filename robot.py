import pyfirmata
import keyboard

port = "COM10"
board = pyfirmata.ArduinoMega(port)
change = 0


water_pin = board.get_pin("a:1:i")

umotor1 = board.get_pin("d:11:o")
umotor2 = board.digital[11]
lmotor = board.digital[9]
rmotor = board.digital[7]

umotor2.mode = pyfirmata.PWM
lmotor.mode = pyfirmata.PWM
rmotor.mode = pyfirmata.PWM





iterate = pyfirmata.util.Iterator(board)
iterate.start()

while True:
    if keyboard.is_pressed("w"):
        umotor1.write(255) #1700w
        print("fwd")
    elif keyboard.is_pressed("s"):
        print("backward")
    else:
        change = 0
        umotor1.write(0) #1500
        print("stop")


    water_sensor = water_pin.read()
    # print(water_sensor)
