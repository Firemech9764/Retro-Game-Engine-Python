import json
import engine
import time
import threading as t

name = "bg2"
f = open(name+".asset", 'r')
screen_width = int(f.readline())
screen_length = int(f.readline())
with f as fp:
    filled_list = json.load(fp)

window1 = engine.Window()
footballField = engine.Frames()
player = engine.Player()
object1 = engine.Objects()


def game():
    for i in range(10):
        time.sleep(2)
        player.x_position+=1

footballField.screen = []
footballField.screen.append(filled_list)
footballField.updation_time=10
player.avatar = "*"
object1.avatar = "o"
player.x_position = 5
player.y_position = 5
object1.x_position = 3
object1.y_position = 3
window1.screens = []
window1.screens.append(footballField.screen[0])
window1.screen_change=True

g = t.Thread(target=game)
g.start()

window1.plot(player, [footballField], [object1])

