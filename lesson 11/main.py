import pgzrun
import itertools
import random
WIDTH = 600
HEIGHT = 500
block = Actor("rock")
block.x = 50
block.y = 450
ship = Actor("rocket")
ship.x = 300
ship.y = 250
block_positions = [(50, 50), (550, 50), (550,450 ), (50, 450) ]
final = itertools.cycle(block_positions)
def draw():
    screen.fill((186, 186, 181))
    block.draw()
    ship.draw()
def moveblock():
    animate(block, "bounce_end", duration = 1, pos = next(final))
def moveship():
    x = random.randint(100, 400)
    y = random.randint(100, 300)
    t = ship.angle_to((x, y))
    animate(ship, "accel_decel", duration = 1, pos = (x, y), angle = t)    
moveblock()  
moveship()
clock.schedule_interval(moveblock,2)  
clock.schedule_interval(moveship, 1)
pgzrun.go()