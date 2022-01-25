# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
from tkinter import Tk


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
    make_sky(canvas, scene_height, scene_width)
    make_ground(canvas, scene_height, scene_width)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def make_sky(canvas, scene_height, scene_width):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height,
    width = 0, fill="sky blue")
    
def make_ground(canvas, scene_height, scene_width):
      draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="snow2")
      drawCloud(canvas,2,0,int(scene_height/3),scene_width,scene_height)



    #def draw_cloud(canvas, center_x, bottom, height): 
        #for i in range(1,16):  
         #size=randint(20,70)
         #xOffset=randint(-40,40)
         #yOffset=randint(-30,30)
         #ellipse(100+xOffset,100+yOffset,size,size)


def drawCloud(canvas,cloud_num,min_x, min_y , max_x, max_y,): 
        for i in range(cloud_num):  
            rand_x = randint(min_x,max_x)
            rand_y = randint(min_y,max_y)
            draw_oval(canvas,rand_x, rand_y,rand_x,rand_y)

# Call the main function so that
# this program will start executing.
main()