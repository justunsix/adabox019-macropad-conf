# Simpletest demo for MacroPad. Prints the key pressed, the relative position of
# encoder switch, and the state of the rotary encoder switch to built-in display
# see https://github.com/adafruit/Adafruit_CircuitPython_MacroPad
from adafruit_macropad import MacroPad

# create Macropad object
macropad = MacroPad()

text_lines = macropad.display_text(title="MacroPad Info")

while True:
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        text_lines[0].text = "Key {} pressed!".format(key_event.key_number)
    text_lines[1].text = "Rotary encoder {}".format(macropad.encoder)
    text_lines[2].text = "Encoder switch: {}".format(macropad.encoder_switch)
    text_lines.show()

