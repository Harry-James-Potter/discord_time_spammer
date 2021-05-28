import time
from pynput import keyboard
keyboardd = keyboard.Controller()

print (time.time)
while True:
    ti_me = time.localtime(round(time.time()))
    if ti_me.tm_hour == ti_me.tm_min:
        keyboard.type(str(ti_me.tm_hour)*2)
        keyboardd.press(keyboard.Key.space)
        keyboardd.release(keyboard.Key.space)
        time.sleep(600)

    elif ti_me.tm_hour + 12 == ti_me.tm_min:
        keyboardd.type(str(ti_me.tm_hour + 12)*2)
        keyboardd.press(keyboard.Key.space)
        keyboardd.release(keyboard.Key.space)
        time.sleep(600) 
