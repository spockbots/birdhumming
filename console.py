#!/usr/bin/env micropython
from ev3dev2.console import Console
from time import sleep

# create a Console instance, which uses the default font
console = Console()

# reset the console to clear it, home the cursor at 1,1, and then turn off the cursor
console.reset_console()

# display 'Hello World!' at row 5, column 1 in inverse, but reset the EV3 LCD console first
console.text_at('Hello World!', column=1, row=5, reset_console=True, inverse=True)
sleep(10)