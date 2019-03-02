'''spinning cube with only standard python.
Left and right arrow keys speed/slow spin'''
import tkinter
from math import cos, sin

fps = 50
speed = 0.1

def cubeVerts(size=1,rot=0.0):
    wd = 0.5 * size
    crn = [[-wd,wd,-wd],[wd,wd,-wd],[wd,-wd,-wd],[-wd,-wd,-wd],
        [-wd,wd,wd],[wd,wd,wd],[wd,-wd,wd],[-wd,-wd,wd]]
    #rotate on y
    for idx,val in enumerate(crn):
        x,y,z=val
        crn[idx][0]=x*cos(rot)-z*sin(rot)
        crn[idx][2]=z*cos(rot)+x*sin(rot)
    #list of verts that draw a cube in one segment (some overlaps b/c of backtracking)
    return [crn[0],crn[1],crn[2],crn[3],crn[0],crn[4],crn[5],crn[6],
        crn[7],crn[4],crn[5],crn[1],crn[0],crn[4],crn[7],crn[3],crn[0],
        crn[1],crn[2],crn[6]]

def draw(angle=0.0):
    global speed
    projVerts=list()
    for vert in cubeVerts(rot=angle):
        #translate in z
        zpos = vert[2]+3
        #project onto XY plane
        #squaring zpos to get a more dramatic projection
        x = vert[0]/zpos**2
        y = vert[1]/zpos**2
        #scale up
        x*=1000
        y*=1000
        #translate in screen space
        x+=120
        y+=100
        projVerts.append([x,y])

    #clear frame and draw
    canvas.delete("all")
    for idx in range(len(projVerts)-1):
        line = canvas.create_line(
            projVerts[idx][0], projVerts[idx][1], 
            projVerts[idx+1][0], projVerts[idx+1][1]
        )
    #get new angle from (old angle + speed) * a little deceleration
    newAngle = (angle+speed)*0.97
    #tkinter callback loop
    window.after(int(1000/fps),draw,newAngle)

def onRightKey(event):
    global speed
    speed += 0.01

def onLeftKey(event):
    global speed
    speed -= 0.01

#setup window and  callbacks
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
window.bind('<Right>',onRightKey)
window.bind('<Left>',onLeftKey)
draw()
window.mainloop()