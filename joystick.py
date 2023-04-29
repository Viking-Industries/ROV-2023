import pygame
from Arduino import Arduino
from time import sleep

board = Arduino("115200", port="COM3")

board.Servos.attach(13)
board.Servos.attach(7)

board.Servos.writeMicroseconds(13, 1100)
board.Servos.writeMicroseconds(7, 1000)


rchange = 0
lchange = 0

# Initialize the Pygame joystick module
pygame.init()
pygame.joystick.init()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Define the joystick deadzone (i.e. values below this threshold will be ignored)
deadzone = 0.1

# Define the maximum motor speed (0-255)
max_speed = 255

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

    # Apply the deadzone to the joystick values
    if abs(x_axis) < deadzone:
        x_axis = 0
    if abs(y_axis) < deadzone:
        y_axis = 0

 #   print(x_axis, y_axis)

    # Throttle Button
    if joystick.get_button(0) == 1:
        # Turn Left
        if x_axis < 0:
            lchange = y_axis * 100
        else:
            lchange = y_axis * 200

        # Turn Right
        if x_axis > 0:
            rchange = y_axis * 200
        else:
            rchange = y_axis * 400
    else:
        rchange = 0
        lchange = 0
    
    
    
    # Write PWM to ESC 
    board.Servos.writeMicroseconds(7, 1000 + rchange)
    board.Servos.writeMicroseconds(13, 1100 + lchange)
  #  board.Servos.writeMicroseconds(11, 1100 + changey)

    
    
    #print(joystick.get_axis(3))
    # BUTTON 0 == back button 
    # BUTTON 1 == thumb button

    # BUTTON 2 == bottom left
    # BUTTON 3 == bottom right
    # BUTTON 4 == top left
    # BUTTON 5 == top right

    # BUTTON 6 == 7


    




# Clean up the Pygame and serial resources
joystick.quit()
pygame.joystick.quit()
pygame.quit()
