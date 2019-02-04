# Mr. Riley's map class v1.90204
#
# How to use Mr. Riley's map class...
# 1.) create a map instance: map = Map()
# 2.) draw/redraw the map inside the game loop: map.draw(rooms, items, currentlocation)
# Don't wanna show yer item locations? Do this: map.draw(rooms, False, currentlocation)

from turtle import *
import math

class Map(Turtle):
  def __init__(self):
    Turtle.__init__(self)
    self.speed(0)
    self.penup()
    self.screen = Screen()
    self.size = 200 # map window size
    self.roomsize = 20
    self.roomborder = 2
    self.startinglocation = None
    self.columnheight = 100
    self.screen.setup(self.size,self.size)
    self.screen.tracer(0)
    self.screen.bgcolor("black")
    #self.screen.register_shape("bigdiamond",((-6,-6),(0,9),(6,-6),(-9,3),(9,3),(-6,-6)))
    self.screen.register_shape("bigstar",((-10,-6.5),(10,0),(-10,6.5),(2.5,-10),(2.5,10),(-10,-6.5)))
    self.screen.register_shape("lilstar",((-3,-2),(3,0),(-3,2),(1,-3),(1,3),(-3,-2)))

  # use the draw method to draw and redraw the map
  def draw(self,rooms,roomitems,mylocation):
    rowwidth = int(math.ceil(len(rooms) / self.columnheight))
    self.penup()
    self.clear()
    if self.startinglocation is None:
      self.startinglocation = mylocation
    for row in range(self.columnheight):
      for column in range(rowwidth):
        try:
          if rooms[column*self.columnheight+row]:
            self.color('white')
            self.shape("square")
            self.goto(-self.size/2+(self.roomsize/2)+column*(self.roomsize+self.roomborder),self.size/2-(self.roomsize/2)-row*(self.roomsize+self.roomborder))
            self.stamp()
        except:
          pass
        try:
          if roomitems[column*self.columnheight+row]:
            self.color('gold')
            self.shape("lilstar")
            self.goto(-self.size/2+(self.roomsize/2)+column*(self.roomsize+self.roomborder),self.size/2-(self.roomsize/2)-row*(self.roomsize+self.roomborder))
            self.stamp()
        except:
          pass
        if self.startinglocation == column*self.columnheight+row:
            self.color('green')
            self.back(self.roomsize/2)
            self.write('Start', font=("Arial", 7, "normal"))
            self.forward(self.roomsize/2)
        if mylocation == column*self.columnheight+row:
            self.color('red')
            self.shape("bigstar")
            self.stamp()
    self.screen.update()
