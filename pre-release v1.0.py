# modules for display and interfacing are imported
import board, busio, displayio, os, terminalio, time, digitalio, alarm
import adafruit_displayio_ssd1306  # module for screen
from adafruit_display_text import label  # module for labels
from adafruit_bitmap_font import bitmap_font  # module for custom fonts
import adafruit_imageload  # module for showing images


# functions for program specific built-ins
def button_check():  # function checks for any button input and returns the button number when called
    print("button check function has been called!")
    # buttons are set
    left_button = digitalio.DigitalInOut(board.GP15)
    left_button.switch_to_input(
        pull=digitalio.Pull.UP)  # internal pullup resistor must be set as high/UP or else button value fluctuates

    middle_button = digitalio.DigitalInOut(board.GP14)
    middle_button.switch_to_input(pull=digitalio.Pull.UP)

    right_button = digitalio.DigitalInOut(board.GP13)
    right_button.switch_to_input(pull=digitalio.Pull.UP)

    while True:  # loop runs which checks for button input (indefinitely until pressed)
        if left_button.value == False:
            button_num = 1
            # print ("left button was pressed")
            break
        if middle_button.value == False:
            button_num = 2
            # print ("middle button was pressed")
            break
        if right_button.value == False:
            button_num = 3
            # print ("right button was pressed")
            break

    # All buttons are deinitizalized
    middle_button.deinit()
    left_button.deinit()
    right_button.deinit()

    # returns the value of button_num
    return button_num


def clear_menu():  # function clears the screen of any content/reverts to a blank screen, may need to change a bit to account for view switching
    display.root_group = None


def flash(width, length, x, y):
    # Layer 1 Shape Settings
    color_bitmap = displayio.Bitmap(width, length, 1)  # change border size
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White
    # Layer 1 shape (takes x and y coords from FILE input)
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=x, y=y)
    splash.append(bg_sprite)
    time.sleep(0.15)
    splash.remove(bg_sprite)


def menu_square(width, length, x, y, image, menu):  # function for making the squares seen on the function menu
    # Layer 1 Shape Settings
    color_bitmap = displayio.Bitmap(width, length, 1)  # change border size
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White
    # Layer 1 shape (takes x and y coords from FILE input)
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=x, y=y)
    menu.append(bg_sprite)
    # Layer 2 Shape Settings
    inner_bitmap = displayio.Bitmap(width - 2, length - 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    # Layer 2 shape (takes x and y coords from FILE input, and adds 1)
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=x + 1, y=y + 1)
    menu.append(inner_sprite)

    # image settings are defined
    IMAGE_FILE = image
    SPRITE_SIZE = (16, 16)
    FRAMES = 1

    # load the spritesheet
    icon_bit, icon_pal = adafruit_imageload.load(IMAGE_FILE, bitmap=displayio.Bitmap, palette=displayio.Palette)
    # image coordinates calculates
    image_x = x + int((width / 2) - 8)
    image_y = y + int((length / 2) - 8)

    icon_grid = displayio.TileGrid(icon_bit, pixel_shader=icon_pal,
                                   width=1, height=1,
                                   tile_height=SPRITE_SIZE[1], tile_width=SPRITE_SIZE[1],
                                   default_tile=0,
                                   x=image_x,
                                   y=image_y)  # location is x+9 and y+3 (user entered x&y values from before)
    menu.append(icon_grid)


# menu1/main menu functions
def menu1_UI():
    # Menu1 squares are formed by calling on the 'menu1_square' function and giving appropriate arguments
    power_square = menu_square(34, 22, 5, 24, "images/power.bmp", menu1_splash)
    leaf_square = menu_square(34, 22, 48, 24, "images/leaf.bmp", menu1_splash)
    settings_square = menu_square(34, 22, 90, 24, "images/wrench.bmp", menu1_splash)
    # space for other UI elements to be formed (battery status namely), maybe also manipulate menu choices


def menu1():  # function for menu 1 and it's actions
    # menu1 UI is formed
    menu1_UI()

    # menu1_splash is appended to 'splash'/root display group
    splash.append(menu1_splash)

    # the button value is assigned to variable 'button_num', runs a while loop as it calls for variable, eliminating the need for one in 'menu1' function
    button_num = button_check()

    # conditionals which check the button value and do the appropritate task/function (literally lol)
    if button_num == 1:  # enters sleep mode
        print("Left Button was pressed")
        flash(34, 22, 5, 24)
        splash.remove(menu1_splash)
        deep_sleep()
    elif button_num == 2:  # enter menu 2/voltage menu
        print("Middle Button was pressed")
        flash(34, 22, 48, 24)
        splash.remove(menu1_splash)
        time.sleep(0.1)
        menu2()
    elif button_num == 3:  # enter menu 3/settings menu
        print("Right Button was pressed")
        flash(34, 22, 90, 24)
        splash.remove(menu1_splash)
        time.sleep(0.1)
        menu3()


# menu2/voltage menu functions
def menu2_UI():
    # elements of the UI will be appeneded to menu 2 splash. and menu 2 splash will be appended to splash in main 'menu2' function
    switch_square = menu_square(28, 18, 8, 44, "images/switch arrow.bmp", menu2_splash)
    go_square = menu_square(28, 18, 50, 44, "images/go.bmp", menu2_splash)
    return_square = menu_square(28, 18, 92, 44, "images/return arrow.bmp", menu2_splash)

def menu2():
    # menu2 UI is formed
    menu2_UI()

    # menu2_splash is appended to 'splash'/root display group
    splash.append(menu2_splash)
    while True:
        # voltage level of pen is displayed (not to be confused w/ battery voltage)
        global pen_voltage
        print(pen_voltage)
        voltage_str = str(pen_voltage)  # converted variable 'pen_voltage' to string so it can be displayed
        text_label = label.Label(terminalio.FONT, text=voltage_str, color=0xFFFFFF, scale=2, x=32, y=24, )
        menu2_splash.append(text_label)

        # the button value is assigned to variable 'button_num', runs a while loop as it calls for variable, eliminating the need for one in 'menu1' function
        button_num = button_check()

        # conditionals which check the button value and do the appropritate task/function (literally lol)
        if button_num == 1:  # switch key, goes to voltage adjust menu (menu2 sub-menu 1)
            print("Left Button was pressed")
            flash(28, 18, 8, 44)
            menu2_splash.remove(text_label)
            splash.remove(menu2_splash)
            menu2a()
        elif button_num == 2:  # action key, goes to smoke menu (menu2a)
            print("Middle Button was pressed")
            flash(28, 18, 50, 44)
            menu2_splash.remove(text_label)
            splash.remove(menu2_splash)
            menu2b()
        elif button_num == 3:  # return key, exits to menu 1
            print("Right Button was pressed")
            flash(28, 18, 92, 44)
            menu2_splash.remove(text_label)
            splash.remove(menu2_splash)
            menu1()

def menu2a_UI():  # voltage adjust menu UI
    # elements of the UI will be appeneded to sub-menu 2a splash
    p_square = menu_square(28, 18, 8, 44, "images/up arrow.bmp", menu2a_splash)
    return_square = menu_square(28, 18, 50, 44, "images/return arrow.bmp", menu2a_splash)
    down_square = menu_square(28, 18, 92, 44, "images/down arrow.bmp", menu2a_splash)

def menu2a():  # voltage adjust menu
    # UI is called
    menu2a_UI()
    # sub menu 1 of menu 2 is appended to
    splash.append(menu2a_splash)
    # var 'pen_voltage' is declared global as to reference outside of function
    global pen_voltage
    print (pen_voltage)
    # voltage level of pen is displayed (not to be confused w/ battery voltage)
    voltage_str = str(pen_voltage)  # converted variable 'pen_voltage' to string so it can be displayed
    voltage_label = label.Label(terminalio.FONT, text=voltage_str, color=0xFFFFFF, scale=2, x=32, y=24, )
    # loop runs indefinitely or until exit from menu
    while True:
        menu2a_splash.append(voltage_label)
        # the button value is assigned to variable 'button_num', runs a while loop as it calls for variable, eliminating the need for one in 'menu1' function
        button_num = button_check()

        # conditionals which check the button value and do the appropritate task/function (literally lol)
        if button_num == 1:  # up key (increases pen voltage)
            print("Left Button was pressed")
            flash(28, 18, 8, 44)
            if pen_voltage < 4.2:
                pen_voltage += 0.1
                print(f'V:{pen_voltage}')

        elif button_num == 2:  # return key (returns to menu 2)
            print("Middle Button was pressed")
            flash(28, 18, 50, 44)
            menu2a_splash.remove(voltage_label)
            splash.remove(menu2a_splash)
            menu2()
        elif button_num == 3:  # down key (decreases pen voltage)
            print("Right Button was pressed")
            flash(28, 18, 92, 44)
            if pen_voltage > 0:
                pen_voltage -= 0.1
                print(f'V:{pen_voltage}')
        menu2a_splash.remove(voltage_label)
def menu2b_UI():  # the voltage adjust menu
    f = 0
    f = 0

def menu2b():  # the smoke menu
    menu2b_UI()

# menu3/settings menu
def menu3_UI():
    f = 0

def menu3():
    splash.append(menu3_splash)
    f = 0

# power menu
def deep_sleep():  #
    # deinit display pins?
    # (board.GP0).deinit()
    pin_alarm = alarm.pin.PinAlarm(pin=board.GP15, value=True, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm)


########################################################################################################################
# Function end, variables and screen assignments start


# displayio is called/set
displayio.release_displays()

# board type is defined using 'os' module
board_type = os.uname().machine
print(f"Board: {board_type}")

# font is set
'''font_file = "fonts/Minecraft.bdf"
font = bitmap_font.load_font(font_file)
text = "Ahsan is cool!"
text_area = label.Label(font, text=text, color=0xFFFF00, x=28, y=28)
splash.append(text_area)'''

# sda and scl pins are set for rpi-pico
sda, scl = board.GP0, board.GP1

# method of communication variable 'i2c' is defined(?) with appropriate signals being assigned
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# built-in led is set (not neopixel one)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Root display group 'splash' is defined and set to show
splash = displayio.Group()  # splash is the group of things to be shown (not a native container)
display.show(splash)  # command show from module 'display' is run to show contents of splash on screen

# menu1 is assigned a display group for organization (and to make life easier with manipulating groups)
menu1_splash = displayio.Group()

menu2_splash = displayio.Group()
menu2a_splash = displayio.Group()
menu2b_splash = displayio.Group()

menu3_splash = displayio.Group()

# 'pen_voltage' is global variable so it can be interacted with in both the UI and temp control menu(s)
pen_voltage = 0.0  # also defined outside of any function to prevent resetting upon reference back to a menu
pen_voltage = round(pen_voltage, 1)
########################################################################################################################
# variable end, code runs

# menu1_splash.hidden # to hide, when statement is called again, it displays the menu again
menu1()
