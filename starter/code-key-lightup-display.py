# For pressed keys, display the key number pressed
# on screen and turn key light blue
# from https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython/keys-one-key-per-pin
import board
import keypad
import neopixel

KEY_PINS = (
    board.KEY1,
    board.KEY2,
    board.KEY3,
    board.KEY4,
    board.KEY5,
    board.KEY6,
    board.KEY7,
    board.KEY8,
    board.KEY9,
    board.KEY10,
    board.KEY11,
    board.KEY12,
)

# keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)

# optionally, Increase event queue size to 128 events
# The EventQueue for each scanner is of fixed size. 
# The default size is 64 events.
# You can change this value by setting the optional max_events parameter
keys = keypad.Keys(
    KEY_PINS,
    value_when_pressed=False,
    pull=True,
    max_events=128
)

neopixels = neopixel.NeoPixel(board.NEOPIXEL, 12, brightness=0.4)

# Create an event we will reuse over and over to avoid generating
# new event objects for garbage collection / storage allocation
event = keypad.Event()

while True:
    # event = keys.events.get(), not required with reused event above
    # In the background, polling of events in done every 20 miliseconds 
    # and can be configured
    if keys.events.get_into(event):
        # A key transition occurred.
        print(event)

        if event.pressed:
            # Turn the key blue when pressed
            neopixels[event.key_number] = (0, 0, 255)

        # This could just be `else:`,
        # since event.pressed and event.released are opposites.
        if event.released:
            neopixels[event.key_number] = (0, 0, 0)
    
    # Check if we lost some events.
    if keys.events.overflowed:
        keys.events.clear()    # Empty the event queue.
        keys.reset()           # Forget any existing presses. Start over.