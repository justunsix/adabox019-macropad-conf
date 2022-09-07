# Adabox019 Macropad Configurations

Test different uses for the Macropad

## Built With

- [CircuitPython](https://circuitpython.org/board/adafruit_macropad_rp2040/) version 7.0.0-alpha.5
- [Adabox019](https://www.adafruit.com/adabox019)

## Getting Started

### Prerequisites

- [Mu Editor](https://codewith.mu/) (recommended)

or

- [VS Code with CircuitPython extension](https://marketplace.visualstudio.com/items?itemName=joedevivo.vscode-circuitpython). Use the update bundle and reload project libraries to get code completion in VS Code.

### Installation

[Load CircuitPython](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython) to the board

#### Library manager

- This loading installs CircuitPython into the `CIRCUITPY` drive and create directories like `lib` to store libraries OR follow library instructions using [`circup`](https://github.com/adafruit/circup), `circup install`, and `circup update` at [CircuitPython_MacroPad](https://github.com/adafruit/Adafruit_CircuitPython_MacroPad).

#### Manual library install

Install the [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries) 7.x. Unzip the bundle and copy the library files you need to the `lib` folder in the `CIRCUITPY` drive. Using the library bundle or `circup`, install these libraries on the `CIRUITPY` drive:

- `simpleio.mpy`
- `neopixel.mpy`
- `adafruit_simple_text_display.mpy`
- `adafruit_debouncer.mpy`
- `adafruit_pixelbuf.mpy`
- folder and files:
  - `adafruit_hid` 
  - `adafruit_midi`
  - `adafruit_display_text`
  - `adafruit_displayio_layout`
  - `adafruit_led_animation`
- Create your own libraries in `.mpy` format using [`mpy-cross`](https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/mpy-cross/)

When using VS Code, install dependencies you are using, for example:

```sh
pip3 install adafruit-circuitpython-simpleio

```

## Usage

[Enter the REPL](https://learn.adafruit.com/adafruit-macropad-rp2040/the-repl) in Mu. Press `ctrl+c` to get the `>>>` prompt and use commands:

```py
# Check CircuitPython version and modules available
help()
help("modules")

# List all pins on the board for use in code
import board
dir(board)

# Test printing
print("Hello, CircuitPython!")

# Check memory available
import gc
gc.mem_free()
```

Press `ctrl+d` to return to the serial console to see output from your program.

### Restart fresh

 CircuitPython includes a built-in function to erase and reformat the filesystem. `CIRCUITPY` will be erased and reformatted.

```py
import storage
storage.erase_filesystem()
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

[justunsix on GitHub](https://github.com/justunsix/)

## See Also

- [Keys and Events explained and example code](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython/keys-one-key-per-pin)
- [Learn Adafruit019](https://learn.adafruit.com/adabox019)
- [Macropad hotkeys](https://learn.adafruit.com/macropad-hotkeys) project
  - [Human Interface Device (HID) devices](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices)
  - CircuitPython's standard USB keyboard descriptor only supports pressing up to 6 non-modifier keys at a time, called 6-Key Rollover or 6KRO. [An example](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/n-key-rollover-nkro-hid-device) on how you can use an alternate USB descriptor to enable unlimited rollover (also called N-Key Rollover or NKRO) using the Adafruit MacroPad.
- [CircuitPython_MacroPad](https://github.com/adafruit/Adafruit_CircuitPython_MacroPad) examples and [documentation with API reference](https://circuitpython.readthedocs.io/projects/macropad/en/latest/#).
- [Curated list of apps macros, 3d printed cases, and guides for the Adafruit CircuitPython rp2040 Macropad](https://github.com/prcutler/awesome-macropad)
