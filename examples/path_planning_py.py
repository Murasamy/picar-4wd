import numpy as np
import matplotlib.pyplot as plt
from vision import scan_surroundings
from PIL import Image

class Node:
    def __init__(self, coor: tuple, parent=None):
        self.coor = coor  # The coordinates of the node (x, y)
        self.parent = parent  # The parent node
        self.g = 0  # steps takes from the origin to this node
        self.h = 0  # Heuristic distance
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.coor == other.coor


def path_planning(map: np.ndarray, origin: tuple, target: tuple):
    """
    :param map: A numpy array (2D) with 0 as traversible space and 1 as obstacles.
    :param origin: The coordinates of the origin.
    :param target: The coordinates of the target.
    """
    origin_node = Node(origin)
    target_node = Node(target)
    path_list = [origin_node]
    traveled_set = set()
    while path_list:
        print("Path list:", path_list)
        node = path_list.pop(0)
        traveled_set.add(node.coor)
        if node == target_node:
            print("Found the target")
            return_list = []
            while node:
                return_list.append(node.coor)
                node = node.parent
            return return_list[::-1]
        
        # test the next action
        actions = [(0, 1), (1, 0), (0, -1), (-1, 0), 
                   (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for action in actions:
            new_x = node.coor[0] + action[0]
            new_y = node.coor[1] + action[1]
            if (0 <= new_x < map.shape[0] and 0 <= new_y < map.shape[1] and
                map[new_x][new_y] == 0 and (new_x, new_y) not in traveled_set):
                # check if the new node is traversible
                if map[new_x, new_y] == 1:
                    continue
                # check if the new node is already in the path
                if (new_x, new_y) in traveled_set:
                    # print("Already traveled:", (new_x, new_y))
                    continue
                else:
                    # create a new node and add it to the path list
                    new_node = Node((new_x, new_y), node)
                    path_list.append(new_node)
                    traveled_set.add(new_node.coor)
                    # print("New node:", new_node.coor)

                new_node = Node((new_x, new_y), node)
                
                # add the new node to the path list if it is not already in the path
                can_add = True
                for n in path_list:
                    if n.coor == new_node.coor:
                        can_add = False
                        break
                if can_add:
                    path_list.append(new_node)
                # print("New node:", new_node.coor)
                # print("Path list:", path_list)
    return None
            
if __name__ == "__main__":
    # Example usage
    map = scan_surroundings(90)
    origin = (0, 0)
    target = (99, 99)
    # plot map
    # print("Map shape:", map)
    array_image = (1-map)*255
    # print(map)
    img = Image.fromarray(array_image.astype(np.uint8), mode='L')
    # img.save('padded_img.png')
    # img.show()
    

    path = path_planning(map, origin, target)
    print("Path:", path)
    
    # Plot the map and the path
    # plt.imshow(map, cmap='gray')
    # if path:
    #     path_x, path_y = zip(*path)
    #     plt.plot(path_y, path_x, color='red')
    # plt.show()

    