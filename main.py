import graphics as g
import time
import keyboard


x, y = input('Enter start point X Y ').split()
speed_x, speed_y = input('Set a speed on X Y ').split()
m = input('Ente weight of ball')
#speed_x, speed_y = 0, 0

SIZE_X = 400
SIZE_Y = 400

window = g.GraphWin("First", SIZE_X, SIZE_Y)

coord = g.Point(x, y)
velocity = g.Point(speed_x, speed_y)
tyga = g.Point(0, 0.98)
t = 0


#координаты тела
def add(point_1, point_2):
    new_point = g.Point(point_1.x + point_2.x,
                       round( point_1.y - point_2.y))

    return new_point


#создание тела
def draw_ball(coord):
    telo = g.Circle(coord, 10)
    telo.setFill('blue')
    telo.draw(window)


#чистка окна после завершения
def clear_window():
    rectangle = g.Rectangle(g.Point(0, 0), g.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('white')
    rectangle.draw(window)


#проверка координат для фбсолютно упргого сопротивления
def check_coord(coord, velocity):
    if coord.y < 0 or coord.y > SIZE_Y:
        velocity.y = - velocity.y
    if coord.x  < 0 or coord.x > SIZE_X:
        velocity.x =  - velocity.x
    if coord.y == SIZE_Y:
        velocity.y = - velocity.y//2


#Tyga coord
def coord2(coord, velocity):
    return add(coord, velocity)


# F тяг
def velocity2(velocity, tyga):
    return add(velocity, tyga)

#живность процессу(фпс) - еудщ проги
while True:
    t += 1
    clear_window()
    draw_ball(coord)

    velocity = velocity2(velocity, tyga)
    check_coord(coord, velocity)
    #coord = add(coord, velocity)
    coord = coord2(coord, velocity)

    g.time.sleep(0.1000)

