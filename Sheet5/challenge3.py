from gasp import *
from gasp.utils import *
x = 5
y = 5

begin_graphics()
c = Circle((5, 5), 5)

while x < 635:
    x = x + 4
    y = y + 3
    move_to(c, (x, y))
    sleep(.04)
    