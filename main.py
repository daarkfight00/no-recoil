import time
import platform
from pynput import mouse, keyboard
import pyautogui
import os

# Get screen resolution
size = pyautogui.size()


no_recoil_active = False
mouse_button_pressed = False

def no_recoil(size):
    def on_click(x, y, button, pressed):
        global mouse_button_pressed
        if button == mouse.Button.left:
            mouse_button_pressed = pressed

    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    try:
        while True:
            global no_recoil_active
            x, y = pyautogui.position()
            if no_recoil_active and mouse_button_pressed:
                new_y = y + 40
                if new_y < size.height:
                    pyautogui.moveTo(x, new_y)

            print(f"Mouse position: x={x}, y={y}", end='\r')
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nProgram Interrupted")
    finally:
        mouse_listener.stop()

def on_press(key):
    global no_recoil_active
    if key == keyboard.Key.num_lock:
        no_recoil_active = not no_recoil_active
        if no_recoil_active:
            print("\nActive")
        else:
            print("\nInactive")

def main():
    # Get the clear command for Windows or Linux
    operating_system = platform.system()

    if operating_system == "Windows":
        clear_command = "cls"
    else:
        clear_command = "clear"

    # Introduction to the program, settings and startup
    print("Welcome to my project, use this for legal activities")
    print("\nAuthor : daarkfight00 => GITHUB")
    time.sleep(3)
    os.system(clear_command)

    print("\n\nHELP => Press the key 'BLOCK NUM' to activate or disable the no-recoil script")
    print("Script will start in", end=' ')
    for i in range(4, 0, -1):
        print(i, end=' ', flush=True)
        time.sleep(1)

    os.system(clear_command)
    print("SCRIPT RUNNING...")

    # Start listener for the key
    keyboard_listener = keyboard.Listener(on_press=on_press)
    keyboard_listener.start()

    no_recoil(size)

    # Stop the listener
    keyboard_listener.stop()

if __name__ == "__main__":
    main()
