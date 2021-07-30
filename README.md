# Adabox019 Macropad Configurations

Test different uses for the Macropad

## Built With

- [CircuitPython](https://circuitpython.org/board/adafruit_macropad_rp2040/) version 7.0.0-alpha.5 
- [Adabox019](https://www.adafruit.com/adabox019)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- [Mu Editor](https://codewith.mu/) (recommended)

### Installation

[Load CircuitPython](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython) to the board

- This loading installs CircuitPython into the `CIRCUITPY` drive and create directories like `lib` to store libraries.

Install the [Adafruit CircuitPython Library Bundle](https://circuitpython.org/libraries) 7.x. Unzip the bundle and copy the library files you need to the `lib` folder in the `CIRCUITPY` drive.

- Extract the bundle, find the `simpleio.mpy` file and copy it to the `lib` folder in the `CIRCUITPY` drive.
- Create your own libraries in `.mpy` format using [`mpy-cross`](https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/mpy-cross/)

When using VS Code, install dependencies you are using:

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

[JustinTungOnline on GitHub](https://github.com/justintungonline/)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

