"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Haiden Smith.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
window.tracer(100)

stevo = rg.SimpleTurtle()
stevo.pen = rg.Pen('green', 2)
stevo.speed = 10

size = 1

for k in range(90):
    stevo.draw_circle(size)

    stevo.pen_up()
    stevo.left(45)
    stevo.forward(10)
    stevo.left(45)
    stevo.pen_down()
    size = size + 10

window.tracer(100)

susan = rg.SimpleTurtle()
susan.pen = rg.Pen('black', 2)
susan.speed = 10

for k in range(500):
    susan.draw_circle(size)

    susan.pen_up()
    susan.right(45)
    susan.forward(10)
    susan.right(45)

    susan.pen_down()
    size = size + 10

window.close_on_mouse_click()
