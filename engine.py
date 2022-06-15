# a simple game to make a player move 10 steps across the screen and change the screen after 10 seconds

import json
import engine
import time
import threading as t



name = "clouds1"
f = open(name+".asset", 'r')
screen_width = int(f.readline())
screen_length = int(f.readline())
with f as fp:
    filled_list = json.load(fp)

f = open("clouds2.asset", 'r')
screen_width = int(f.readline())
screen_length = int(f.readline())
with f as fp:
    filled_list2 = json.load(fp)

window1 = engine.Window()
clouds = engine.Frames()
ground = engine.Frames()

player = engine.Player()
object1 = engine.Objects()


clouds.screen = []
clouds.screen.append(filled_list)
clouds.screen.append(filled_list2)
clouds.updation_time=2
clouds.priority=1


name = "g1"
f = open(name+".asset", 'r')
screen_width = int(f.readline())
screen_length = int(f.readline())
with f as fp:
    filled_list = json.load(fp)

f = open("g2.asset", 'r')
screen_width = int(f.readline())
screen_length = int(f.readline())
with f as fp:
    filled_list2 = json.load(fp)

f = open("g3.asset", 'r')
screen_width = int(f.readline())
screen_length = int(f.readline())
with f as fp:
    filled_list3 = json.load(fp)

ground.screen = []
ground.screen.append(filled_list)
ground.screen.append(filled_list2)
ground.screen.append(filled_list3)
ground.updation_time=0.5
ground.priority=2


player.avatar = ">"
object1.avatar = "-"
player.x_position = 26
player.y_position = 5
object1.x_position = 25
object1.y_position = 5
window1.screens = []
window1.screens.append(clouds.screen[0])
window1.screens.append(ground.screen[0])

window1.screen_change=True



window1.plot(player, [clouds,ground], [object1])
