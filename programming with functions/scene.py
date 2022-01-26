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
    drawsnow(canvas,200,0,int(scene_height/3),scene_width,scene_height)
    drawclouds(canvas,2,1,3,15,int(scene_width-30),int(scene_height/3),int(scene_height-100))
    #testCloud(canvas,4,1,3,15,int(scene_width-30),int(scene_height/3),int(scene_height-10))
    
def make_ground(canvas, scene_height, scene_width):
      draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="snow2")
     



    #def draw_cloud(canvas, center_x, bottom, height): 
        #for i in range(1,16):  
        # size=randint(20,70)
        # xOffset=randint(-40,40)
        # yOffset=randint(-30,30)
        # ellipse(100+xOffset,100+yOffset,size,size)


def drawsnow(canvas,snow_num,min_x, min_y , max_x, max_y,): 
    diameter = 10
    for i in range(snow_num):  
            rand_x = randint(min_x,max_x)
            rand_y = randint(min_y,max_y)
            draw_oval(canvas,rand_x, rand_y,rand_x + diameter,rand_y+diameter,fill="snow1")

def drawclouds(canvas, cloud_num , min_cloud_size, max_cloudsize, min_x, max_x, min_y, max_y):
    #diameter is how big the chunks of cloud are individually cloud size uses min_x, min_y max_x 
    # and Max_y to determine the size of each cloud cluster, cloud_size unknown?
   
    for i in range(cloud_num): 
        cloud_size = 2#randint(min_cloud_size,max_cloudsize)
        
        #rand_x = randint(30, 60)
        #rand_y = randint(30,70)
        for i in range(cloud_size):
            diameter = randint(20,70)
            xOffset=randint(min_x,max_x-20)
            yOffset=randint(min_y,max_y-50)
           
            
            draw_oval(canvas,  xOffset+100, yOffset+100, xOffset +(150+randint(-30,60)) , yOffset+(150+randint(-30,70)) ,fill="yellow")
            draw_oval(canvas,  xOffset+100, yOffset+100, xOffset +(150+randint(-30,60)) , yOffset+(130+randint(-30,70)) ,fill="yellow")
            draw_oval(canvas,  xOffset+100, yOffset+100, xOffset +(150+randint(-30,60)) , yOffset+(160+randint(-30,70)) ,fill="yellow")

def testCloud(canvas, cloud_num , min_cloud_size, max_cloudsize, min_x, max_x, min_y, max_y):
     for i in range(1,16):
            diameter = randint(20,70)
            xOffset=randint(-40,40)
            yOffset=randint(-30,30)
            draw_oval(canvas, 100+xOffset , 100+yOffset , diameter , diameter ,fill="yellow")
            

# Call the main function so that
# this program will start executing.
main()