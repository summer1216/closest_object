import matplotlib.pyplot as plt
import numpy as np
import math
import random
from matplotlib.patches import Rectangle

def corner(x,y,yaw,cx,cy):
     x1 = x*math.cos(yaw) - y*math.sin(yaw)
     y1 = x*math.sin(yaw) + y*math.cos(yaw)
     x1 = x1 + cx
     y1 = y1 + cy
     return x1,y1
    

def draw_box(x, y, yaw, l, w, c='b'):
    x1,y1 = corner(l/2, w/2, yaw,x,y) 
    x2,y2 = corner(l/2, -w/2, yaw,x,y) 
    x3,y3 = corner(-l/2, -w/2, yaw,x,y) 
    x4,y4 = corner(-l/2, w/2, yaw,x,y) 
    if c=='b':
        c = np.random.rand(3,)
        c = c.reshape(1,-1)
    plt.scatter(x,y, s=1,c=c)
    plt.plot([x1,x2,x3,x4,x1],[y1,y2,y3,y4,y1],c=c)
    


def draw_lane(poly_x,poly_y):
    poly_y = [x+2.5 for x in poly_y]
    plt.plot(poly_x,poly_y,color='grey',linestyle="-")
    poly_y = [x+5 for x in poly_y]
    plt.plot(poly_x,poly_y,color='grey',linestyle="-")
    poly_y = [x-10 for x in poly_y]
    plt.plot(poly_x,poly_y,color='grey',linestyle="-")
    poly_y = [x-5 for x in poly_y]
    plt.plot(poly_x,poly_y,color='grey',linestyle="-")
    
    
    
def create_object_poses(seed):
    random_x = []
    random_y = []
    yaw = []

    x = -70
    y = -15
    is_in_loop = True
    i = 0
    
    random.seed(seed)
    while is_in_loop:
        x = x+10
        n = random.randint(1,3)
        n2 = random.randint(-1,1)
        if(x>5 and x<20):
            n2 += 2
        if(x>20):
            n2 += 3
        if(random.choice([True, False]) and not((y == 0) and x < 60)):
            i+=1;
            random_x.append(x+n)
            random_y.append(y+n2)
            n3 = random.uniform(-0.3,0.3)
            yaw.append(n3)

            if x>150:
                x = -70
                y += 5

        if i==97:
            break
    return random_x, random_y, yaw       

def draw_all_boxes(x,y,yaw):

    for i in range(0,len(x)):
        draw_box(x[i], y[i],yaw[i],5,3 )
        
    draw_box(13,2,0.2,5,3,c='g')
    draw_box(34,5,0.1,5,3,c='r')
    draw_box(5,-5,0.1,5,3,c='m')

def create_object_poses_straight(seed):
    random_x = []
    random_y = []
    yaw = []

    x = -70
    y = -15
    is_in_loop = True
    i = 0
    
    random.seed(seed)
    while is_in_loop:
        x = x+10
        n = random.randint(1,3)
        n2 = random.randint(-1,1)
        if(random.choice([True, False]) and not((y == 0) and x < 60)):
            i+=1;
            random_x.append(x+n)
            random_y.append(y+n2)
            n3 = random.uniform(-0.3,0.3)
            yaw.append(n3)

            if x>150:
                x = -70
                y += 5

        if i==97:
            break
    return random_x, random_y, yaw

def draw_all_boxes_straight(x,y,yaw):

    for i in range(0,len(x)):
        draw_box(x[i], y[i],yaw[i],5,3 )

    draw_box(13,0,0.2,5,3,c='g')
    draw_box(34,0,0.1,5,3,c='r')
    draw_box(5,-5,0.1,5,3,c='m')
    
def draw_ego(ax):
    ax.add_patch(Rectangle((-2.5, -1.5), 5, 3,fill = True,zorder=4))

    plt.arrow(0, 0, 3,0,
          head_width = 1,
          width = 0.05,
          ec ='grey')
    plt.scatter(0,0,s=100, marker=(5, 1),c='y',zorder =5)	
