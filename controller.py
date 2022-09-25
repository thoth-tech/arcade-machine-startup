#!/usr/bin/env python3

# Run in the backgorund using the below cmd
# nohup sudo python controller.py > controller.log &
# OR
# nohup sudo python controller.py > /dev/null 2>&1 &

# List running python processes
# ps -fA | grep python

# Kill process
#  kill PID

# Current key mapping for 
# https://batteryexpert.com.au/usb-fighting-stick-arcade-controller-gamepad-game-joystick-with-8-buttons-for-pc-computer-game.html

#  - Player One
#     - Movement
#         - W, A, S, D
#     - Function Buttons
#         - R, T, Y, F, G, H
# - Player Two
#     - Movement
#         - ⬆️⬅️⬇️➡️
#     - Function Buttons
#         - U, I, O, J, K, L

# Input devices listed by:
# ls /dev/input

from evdev import InputDevice, categorize, ecodes, KeyEvent
import keyboard
gamepad = InputDevice('/dev/input/event4')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:            
            if keyevent.scancode == 288:
                print('Top Left')
                keyboard.press_and_release("r")
                # keyboard.press_and_release("u")
            elif keyevent.scancode == 289:                
                print ('Top Middle')
                keyboard.press_and_release("t")
                # keyboard.press_and_release("i")
            elif keyevent.scancode == 290:                
                print ('Top Right')
                keyboard.press_and_release("y")
                # keyboard.press_and_release("o")
            elif keyevent.scancode == 291:
                print ('Bottom Left')
                keyboard.press_and_release("f")
                # keyboard.press_and_release("j")
            elif keyevent.scancode == 292:
                print ('Bottom Middle')
                keyboard.press_and_release("g")
                # keyboard.press_and_release("k")
            elif keyevent.scancode == 293:
                print ('Bottom Right')
                keyboard.press_and_release("h")
                # keyboard.press_and_release("l")
            elif keyevent.scancode == 294:
                print ('Base 1')
                keyboard.press_and_release("enter")
            elif keyevent.scancode == 295:
                print ('Base 2')
                keyboard.press_and_release("esc")
    
    if event.type == ecodes.EV_ABS:
        if event.code == 0:
            if event.value == 0:
                print("Left")
                keyboard.press_and_release("a")
                # keyboard.press_and_release("left")
            elif event.value == 255:
                print("Right")
                keyboard.press_and_release("d")
                # keyboard.press_and_release("right")
        elif event.code == 1:
            if event.value == 0:
                print("Up")
                keyboard.press_and_release("w")
                # keyboard.press_and_release("up")
            elif event.value == 255:
                print("Down")
                keyboard.press_and_release("s")
                # keyboard.press_and_release("down")
