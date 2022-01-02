from ursina import *
app = Ursina()
#màu backround
window.color = color.green

#khung
frames = Entity(model = 'cube',color = color.black,scale = (6.8,3.7))

#rắn
snake = Entity(model = 'cube',color = color.red,scale = 0.15,z = -1,collider = 'box')

#thân rắn
body = [Entity(model='cube', scale =0.1,z = -1) for i in range(30)]

#thức ăn
foods = Entity(model='cube',scale=0.15, position=(1,-1,-1), collider='mesh')

from random import randint

dx = dy = 0
def update():

#random thức ăn
  info = snake.intersects()
  if info.hit:
    foods.x = randint(-6,6)/2
    foods.y = randint(-3,3)/2

#gắn thân và đầu
  for i in range(len(body)-1,0,-1):
    pos = body[i-1].position
    body[i].position = pos
  body[0].x = snake.x
  body[0].y = snake.y

#di chuyển
  snake.x += time.dt * dx
  snake.y += time.dt * dy

#nơi va chạm
  if abs(snake.x) > 3.35:
    snake.x = snake.y = stop
  if abs(snake.y) > 1.77:
    snake.x = snake.y = stop

#điều khiển
def input(key):
  global dx,dy
  for x,y,z in zip(['d','a'],[2,-2],[270,90]):
    if key==x:
      snake.rotation = z
      dx = y
      dy = 0
  for x,y,z in zip(['w','s'],[2,-2],[270,90]):
    if key==x:
      snake.rotation = z
      dy = y
      dx = 0

camera.orthographic = True
camera.fov = 4
app.run()