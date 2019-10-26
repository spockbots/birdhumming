#!/usr/bin/env python3
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')
# os.system('setfont Lat15-TerminusBold32x16')  # Try this larger font

print('EV3 Python rules!')
print()  # print a blank line

print('EV3', 'Python rules!')  # comma means continue on same line

# print() has a parameter 'end' which by
# default is the new line character:
print('EV3')    # A new line will be started after this
print('Python rules!')

# Here the 'end' parameter's default new line
# character argument is replaced
# by an empty string so no new line is begun
print('EV3', end='')
print('Python rules!')

# Here the 'end' parameter's default new line
# character argument is replaced
# by a space character so no new line is begun
print('EV3', end=' ')
print('Python rules!')

sleep(15)  # display the text long enough for it to be seen
