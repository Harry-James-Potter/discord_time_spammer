import time
from pynput import keyboard

#  VARIABLES
keyboardd = keyboard.Controller()
print(time.time())

#  TYPE FUNC
def tpe(p_n):
    keyboardd.type(str(ti_me.tm_hour - p_n) * 2)
    keyboardd.press(keyboard.Key.enter)
    keyboardd.release(keyboard.Key.enter)
    time.sleep(600)
    print(str(ti_me.tm_hour - p_n) * 2)

#  WHILE LOOP WHICH REPEATS 1.25 TIMES EVERY MIN
while True:
    ti_me = time.localtime(round(time.time()))
    if ti_me.tm_hour == ti_me.tm_min:
        tpe(0)
    elif ti_me.tm_hour - 12 == ti_me.tm_min:
        tpe(12)
    time.sleep(45)

    #  TO PREVENT FROM SLEEP
    keyboardd.press(keyboard.Key.space)
    keyboardd.release(keyboard.Key.space)
