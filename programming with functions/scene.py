# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from calendar import c
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
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def make_sky(canvas, scene_height, scene_width):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height,
    width = 0, fill="sky blue") 
    drawsnow(canvas,200,0,int(scene_height/3),scene_width,scene_height)
    drawclouds(canvas,300,350,200)
    drawclouds(canvas,400,500,200)
    

    #testCloud(canvas,4,1,3,15,int(scene_width-30),int(scene_height/3),int(scene_height-10))
    
def make_ground(canvas, scene_height, scene_width):
      draw_rectangle(canvas, 0, 0,scene_width, scene_height / 3, width=0, fill="snow2")
      makeSnowman(canvas, 100)
      makeSnowman(canvas,650 )
        
     

def makeSnowman(canvas,x_coord1):


    draw_oval(canvas,x_coord1,168,x_coord1+100,250,width=2,outline="black",fill="white")
    draw_oval(canvas,x_coord1+10,250,x_coord1+90,325,width=2,outline="black",fill="white")
    draw_oval(canvas,x_coord1+20,325,x_coord1+80,400,width=2,outline="black",fill="white")
    draw_oval(canvas,x_coord1+40,375,x_coord1+44,380,width=2,outline="black",fill="black")
    draw_oval(canvas,x_coord1+56,375,x_coord1+60,380,width=2,outline="black",fill="black")
    draw_arc(canvas,x_coord1+30,350,x_coord1+70,368, width=2, fill="black", start=230, extent= 90)


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

def drawclouds(canvas, cloud_base, cloud_height, cloud_length):
    #diameter is how big the chunks of cloud are individually cloud size uses min_x, min_y max_x 
    # and Max_y to determine the size of each cloud cluster, cloud_size unknown?          
        cloud_base_left = cloud_base
        cloud_base_right = cloud_base + cloud_length
        cloudHeightLeft = cloud_base
        cloudHeightRight= cloud_height
        cloudVar = 20
        
        draw_oval(canvas,  cloud_base_left-(cloudVar*2), cloudHeightLeft-cloudVar, cloud_base_right-int(cloudVar/2), cloudHeightRight-cloudVar, outline="snow2", fill="snow2")
        draw_oval(canvas,  cloud_base_left+(cloudVar+100), cloudHeightLeft-(cloudVar), cloud_base_right-int((cloudVar*2)-100), cloudHeightRight-cloudVar, outline="snow2", fill="snow2")
        draw_oval(canvas,  cloud_base_left, cloudHeightLeft, cloud_base_right, cloudHeightRight, outline="snow2", fill="snow2")    


def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Call the main function so that
# this program will start executing.
main()