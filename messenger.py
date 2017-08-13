# Text chat messenger for the BBC micro:bit.
#
# Press B to cycle through the alphabet
# Press A to select the current letter
# Press A+B to broadcast your message over the radio
#
# Incoming messages from other micro:bits are displayed.
#
# Copyright 2017 Stefan Hajnoczi, Clyde French, and Linton French
# MIT Licensed https://opensource.org/licenses/MIT

from microbit import *
import radio

message = ''
letter = 'A'
last_press = 0

radio.on()

while True:
    now = running_time()
    if now >= last_press + 300:
        if button_a.is_pressed() and button_b.is_pressed():
            radio.send(message)
            message = ''
            last_press = now
        elif button_b.is_pressed():
            if letter == 'Z':
                letter = ' '
            elif letter == ' ':
                letter = 'A'
            else:
                letter = chr(ord(letter) + 1)
            last_press = now
        elif button_a.is_pressed():
            message += letter
            last_press = now
    received = radio.receive()
    if received:
        display.scroll(received, delay=300)
    else:
        display.show(letter, delay=0)
