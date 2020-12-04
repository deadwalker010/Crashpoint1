import math
from time import sleep

totalWidth = 1000
totalHeight = 1000
circleX = totalWidth // 2
circleY = totalHeight // 2
circleDist = 0  # this will be defined outside of the functions so we can use this variable globally
outerCircleRadius = (circleX + circleY) // 2 - 60
innerCircleRadius = 75
line_points = {}  # used to store the values of all the line points
turningWheel = False  # used to determine if the wheel has to be turning or not
all_chances = ['Vertraging','horizontale verplaatsing', 'Storing',
               'Insurance', 'Family insurance', 'Multiplier iedereen', 
               'Multiplier', 'Counter', 'Niks']
degree_points = [0, 360]  # this will be used to position the lines along the outside of the circle
velocity = [0, 0]  # this will be used to determine how fast the circle turns

def setup():
    size(totalWidth, totalHeight)
    ellipseMode(RADIUS) # the ellipses get made through their radiuses and not x and y
    frameRate(240) # slower frame rate
    
def draw():
    global number
    global circleDist
    global velocity
    global degree_points
    
    background(255, 255, 255)
    strokeWeight(1)
    
    circleDist = dist(mouseX, mouseY, circleX, circleY)  # the distance of the middle to the mouse, this will be used later with the inner circle
    
    # the black line of the outer circle
    fill(0, 0, 0)
    ellipse(circleX, circleY,  # the middle of the created circle
            outerCircleRadius + 20, outerCircleRadius + 20)
    
    # outer circle; TODO: change the color
    fill(255, 255, 255)
    ellipse(circleX, circleY,  # the middle of the created circle
            outerCircleRadius, outerCircleRadius)
    
    # IMPORTANT: this section covers drawing in the circle with the triangles(lines) and chances
    # the cosin and sin variable are here to help with finding the right coordinates
    # along the line of the circle
    if turningWheel:
        degree_points[0] += velocity[0]
        degree_points[1] += velocity[1]
        
    for index, angle in enumerate(range(degree_points[0], degree_points[1], 40)):
        # the first two coordinates will help to calculate how far the point is from the center of the circle
        x1 = outerCircleRadius * cos(angle * math.pi / 180)
        y1 = outerCircleRadius * sin(angle * math.pi / 180)
        x2 = circleX + x1
        y2 = circleY + y1

        # line function works like this: line(beginX, beginY, endX, endY)
        textAlign(CENTER, LEFT)
        line(circleX, circleY, x2, y2)
        line_points.setdefault('line' + str(index), [x2, y2])  # adding the line point to a dictionary
        # getting the text in the right place
        
        # this section covers centering the chance text in the middle of each triangle
        textSize(16)
        middle_x = circleX + outerCircleRadius * cos((angle + 20) * math.pi / 180)
        middle_y = circleY + outerCircleRadius * sin((angle + 20) * math.pi / 180)
        textX = circleX + ((middle_x - circleX) / 2)
        textY = circleY + ((middle_y - circleY) / 2)
        pushMatrix()  # opens a change for the matrix (recentering the matrix for the rotation)
        translate(textX, textY)  # sets the new center for rotation
        fill(255, 0, 0)
        rotate((angle + 20) * math.pi / 180)
        text(all_chances[index], 0, 0)
        popMatrix()  # closes the change for the matrix

        fill(255, 0, 0)
    else:
        fill(0)
    
    # inner circle; TODO: this has to be filled in last
    # otherwise the chances will overlap this circle
    fill(255, 0, 0)
    ellipse(circleX, circleY, innerCircleRadius, innerCircleRadius)
    
    # text inside the inner circle
    
    textSize(35)
    fill(255, 255, 255)
    textAlign(CENTER, CENTER)
    if turningWheel:
        text('STOP', circleX, circleY)
    else:
        text('START', circleX, circleY)
    
    # triangle on the side of the circle; this has to be filled in last,
    # after all the chances have been filled in, otherwise this gets overlapped, 
    fill(255, 0, 0)
    triangle(totalWidth - 115, totalHeight // 2,  # tip of the triangle pointing towards the middle
        totalWidth - 10, totalHeight // 2 + 50,  # uppermost corner of the triangle
        totalWidth - 10, totalHeight // 2 - 50)  # lowermost corner of the triangle
    
def mousePressed():
    global turningWheel
    global degree_points
    global velocity

    if circleDist < innerCircleRadius:
        turningWheel = not turningWheel

    if turningWheel:
        velocity = [4, 4]
        
