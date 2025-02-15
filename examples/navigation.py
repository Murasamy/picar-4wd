import picar_4wd as fc
import math
# from speed import Speed
import time
# import obj_det2
from vision import scan_surroundings
from a_star_example import a_star_search

dest_x = int(input("Enter the x coordinate of the destination: "))
dest_y = int(input("Enter the y coordinate of the destination: "))

# adjust the speed of the car
def left_90(cell_jump):
    fc.turn_left(20)
    time.sleep(1.41)
    fc.forward(10)
    time.sleep(0.16 * cell_jump)
    fc.stop()

# adjust the speed of the car
def left_45(cell_jump):
    fc.turn_left(10)
    time.sleep(0.66)
    fc.forward(10)
    time.sleep(0.16 * math.sqrt(2)* cell_jump * 1.1)
    fc.stop()

# adjust the speed of the car
def forward_0(cell_jump):
    fc.forward(10)
    time.sleep(0.17 * cell_jump)
    fc.stop()

# adjust the speed of the car
def right_45(cell_jump):
    fc.turn_right(10)
    time.sleep(0.58)
    fc.forward(10)
    time.sleep(0.16 * math.sqrt(2) * cell_jump)
    fc.stop()

# adjust the speed of the car
def right_90(cell_jump):
    fc.turn_right(10)
    time.sleep(1.08)
    fc.forward(10)
    time.sleep(0.16 * cell_jump)
    fc.stop()

action_dict = {
    -2: left_90,
    -1: left_45,
    0: forward_0,
    1: right_45,
    2: right_90
}

def navigation(dest_x, dest_y):
    padded_map = scan_surroundings(90)
    # print(map[target])
    path_list = a_star_search(padded_map, (99, 49), (dest_x, dest_y))
    print(path_list)
    if dest_x >= 49:
        forward_0(20)
        left_90(50)
    else:
        forward_0(20)
        right_90(50)

left_90(10)
