# Add your Python code here. E.g.
from microbit import *
import random


while True:
    n = random.randint(0, 5)
    dice_face = [
        '00000:00000:00900:00000:00000',
        '00009:00000:00000:00000:90000',
        '00009:00000:00900:00000:90000',
        '90009:00000:00000:00000:90009',
        '90009:00000:00900:00000:90009',
        '90009:00000:90009:00000:90009',
        ]
    display.show(Image(dice_face[n]))
    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            break
