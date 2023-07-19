
from gasp import *

begin_graphics()

key_text = Text("a", (320, 240), size=48)

while True:
    key = update_when('key_pressed')
    remove_from_screen(key_text)
    key_text = Text(key, (320, 240), size=48)
    if key == 'q':     # See Sheet C if you don't understand this
        break          # See Sheet L if you aren't sure what this means

end_graphics()