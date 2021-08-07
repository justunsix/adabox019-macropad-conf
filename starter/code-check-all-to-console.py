# Simpletest demo for MacroPad. Prints the key pressed, the relative position of
# encoder switch, and the state of the rotary encoder switch to the serial console.
# see https://github.com/adafruit/Adafruit_CircuitPython_MacroPad
import time
from adafruit_macropad import MacroPad

# create Macropad object
macropad = MacroPad()

while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        print("Key pressed: {}".format(key_event.key_number))
    print("Encoder: {}".format(macropad.encoder))
    print("Encoder switch: {}".format(macropad.encoder_switch))
    time.sleep(0.4)
