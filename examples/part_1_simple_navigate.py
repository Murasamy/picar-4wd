#Base code is from obstacle_avoidance.py
import picar_4wd as fc

speed = 30

def main():
    while True:
        # scan_list = fc.scan_step(35) # ref1=35: 35cm is the distance to return 2
        distance_list = fc.scan_step_distance()
        if not distance_list:
            continue

        tmp = distance_list[3:7] # distance in front, uint: cm
        # print(tmp)
        # if tmp != [2,2,2,2]:
        #     fc.turn_right(speed)
        # else:
        #     fc.forward(speed)
        # if no obstacle in front, keep moving forward
        if tmp == [2,2,2,2]:
            fc.forward(speed)
        # if obstacle detected in front, deside to turn left or right
        else:
            distance_list = fc.scan_step_distance()
            # detect whether to turn left or right
            



if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
