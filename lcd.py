#from ev3dev2.sound import Sound
#sound = Sound()
#sound.speak('Left')

import ev3dev2.fonts as fonts
from ev3dev2.display import Display
from time import sleep


display = Display()
display.clear()
display.update()

display.text_grid(
    'Hello World!', 
    x=2, y=2,
    text_color='black',
    font=fonts.load('luBS14'))
display.update()


sleep(10)
