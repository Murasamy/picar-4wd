#Base code is from obstacle_avoidance.py
import picar_4wd as fc

speed = 30

def main():
    while True:
        scan_list = fc.scan_step(35) # ref1=35: 35cm is the distance to return 2
        if not scan_list:
            continue

        tmp = scan_list[3:7]
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
            # if obstacle detected on the left side, turn right
            if tmp[2] < 2 or tmp[3] < 2:
                fc.turn_right(speed)
            # if obstacle detected on the right side, turn left
            elif tmp[0] < 2 or tmp[1] < 2:
                fc.turn_left(speed)
            else:
                fc.turn_right(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
