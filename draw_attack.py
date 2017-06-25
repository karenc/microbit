from microbit import *
import radio


def set_bit(screen, position, bit):
    y = int(position / 5)
    x = position % 5
    screen[y][x] = bit
    return screen

def image_str(image):
    return ':'.join([''.join(y) for y in image])

def show_image(image):
    display.show(Image(image_str(image)))

def draw_cursor(position, bit):
    display.set_pixel(position % 5, position // 5, int(bit))

def receive_and_sleep():
    for i in range(256):
        image_str = radio.receive()
        if image_str:
            display.show(Image(image_str))
            sleep(3000)

radio.on()
cursor = 0
screen = [['0'] * 5, ['0'] * 5, ['0'] * 5, ['0'] * 5, ['0'] * 5]
timestamp = 4
while True:
    show_image(screen)
    draw_cursor(cursor, '9')

    receive_and_sleep()
    show_image(screen)
    draw_cursor(cursor, '0')
    receive_and_sleep()


    if button_b.is_pressed():
        cursor += 1
        cursor = cursor % 25

    if button_a.is_pressed() and timestamp > 4:
        if screen[cursor//5][cursor%5] == '9':
            set_bit(screen, cursor, '0')
        else:
            set_bit(screen, cursor, '9')
        timestamp = 0
            
        radio.send(image_str(screen))
    timestamp += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
