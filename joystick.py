import pygame
from Arduino import Arduino
import serial
import display

board = Arduino("115200", port="COM3")
# receiver =serial.Serial('COM11', 9600)

left = 9
right = 7

up1 = 13
up2 = 5

servo_pin = 3
board.Servos.attach(servo_pin)

board.Servos.attach(left)
board.Servos.attach(right)
board.Servos.attach(up1)
board.Servos.attach(up2)

board.Servos.writeMicroseconds(left, 1100)
board.Servos.writeMicroseconds(right, 1000)

board.Servos.writeMicroseconds(up1, 1100)
board.Servos.writeMicroseconds(up2, 1100)

rchange = 0
lchange = 0
upchange = 0

# Initialize the Pygame joystick module
pygame.init()
pygame.joystick.init()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Define the joystick deadzone (i.e. values below this threshold will be ignored)
deadzone = 0.1

# Loop until the user quits
done = False
while not done:
    # Get events from the Pygame event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get the current joystick axis positions
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1) * -1
    twist = joystick.get_axis(2)

    # Apply the deadzone to the joystick values
    if abs(x_axis) < deadzone:
        x_axis = 0
    if abs(y_axis) < deadzone:
        y_axis = 0
    if abs(twist) < deadzone:
        twist = 0

    # Throttle Button
    if joystick.get_button(0) == 1:
        # Turn Left
        if x_axis < 0 or twist < 0:
            rchange = lchange - (abs(x_axis) * lchange)
        else:
            rchange = y_axis * 1200

        # Turn Right
        if x_axis > 0 or twist > 0:
            lchange = rchange - (abs(x_axis) * rchange)
        else:
            lchange = y_axis * 1200
    else:
        rchange = 0
        lchange = 0

    if upchange < 1200:
        if joystick.get_button(4) == 1:
            upchange += 10
        if joystick.get_button(2) == 1:
            upchange -= 10
    if joystick.get_button(1) == 1:
        upchange = 0
    
    # Write PWM to ESC 
    board.Servos.writeMicroseconds(right, 1000 + rchange)
    board.Servos.writeMicroseconds(left, 1000 + lchange)

    board.Servos.writeMicroseconds(up1, 1000 + upchange)
    board.Servos.writeMicroseconds(up2, 1000 + upchange)

    # Calculate servo angle from joystick
    servo1 = abs((joystick.get_axis(3) - 1)* 180)/2
    servo1 = round(servo1 / 10) * 10

    #Write Angle to Servo
    board.Servos.write(servo_pin,servo1)

# Display/Monitor
    if board.analogRead(1) > 200:
       #print("WARNING WATER IS REALLY INSIDE")
        display.warning1 = False
        display.warning2 = True
    elif board.analogRead(1) > 100:
       # print("WARNING WATER IS INSIDE")
        display.warning2 = False
        display.warning1 = True
    else:
        display.warning1 = False
        display.warning2 = False

    display.lmotor = round(lchange)
    display.rmotor = round(rchange)
    display.umotor = round(upchange)

    display.update_status()
    display.app.update()

# Clean up the Pygame and serial resources
joystick.quit()
pygame.joystick.quit()
pygame.quit()
