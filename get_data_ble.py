from Exode import *
uno = Board('/dev/tty.HC-06-DevB')

led13 = Led(13)
led14 = Led(14)

led13.blink(250)
led14.blink(500)