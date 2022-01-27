from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
from tkinter import Canvas, Tk


from random import randint
def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    drawCloud()

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def drawCloud(): 
    Canvas.create_oval(300, 300,600,600)