"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui
import poc_simpletest
import test


# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        location = (row, col)
        self._zombie_list.append(location)

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)


    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        location = (row, col)
        self._human_list.append(location)

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human


    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        height = self.get_grid_height()
        width = self.get_grid_width()

        # Create a new grid of the same size as the obstacle grid
        visited = poc_grid.Grid(height, width)
        visited.clear()

        # Create a 2D list of the same size as the grid and initialize its entries to be (heigth * width).
        max_distance = height * width
        distance_field = [[max_distance for dummy_col in range(width)]
                      for dummy_row in range(height)]

        # Create a queue that is a copy entity_type
        boundary = poc_queue.Queue()
        # for entity in entity_type:
        #     boundary.enqueue(entity)
        # entity_type = self.zombies() if entity_type == ZOMBIE else self.humans()
        if entity_type == ZOMBIE:
            entity_type = self.zombies()
        elif entity_type == HUMAN:
           entity_type = self.humans()
        else:
            print "ERROR: Entity type is incorrect"
        [boundary.enqueue(entity) for entity in entity_type]

        for cell in boundary:
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0

        # Updates a 2D distance field computed using the four-way distance to entities of the given type
        while len(boundary) != 0:
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0], cell[1])
            # #neighbors = self.eight_neighbors(cell[0], cell[1])
            for neighbor in neighbors:
                if self.is_empty(neighbor[0], neighbor[1]) and \
                        visited.is_empty(neighbor[0], neighbor[1]):
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[cell[0]][cell[1]] + 1
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
        return distance_field


    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        pass

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        pass

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Zombie(30, 40))
height = 3
width = 3
# obstacle_list = [(4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)]
obstacle_list = []
grid = Zombie(height, width, obstacle_list)
grid.add_zombie(1, 1)
grid.add_human(1, 1)

#
# print grid
# print 'zombie_list', grid._zombie_list
# print 'num_zombies', grid.num_zombies()
#
# queue = poc_queue.Queue()
# for zombie in grid._zombie_list:
#     queue.enqueue(zombie)
# print "queue", queue
#
# print '4 neighbors', [grid.four_neighbors(zombie[0], zombie[1]) for zombie in grid.zombies()]
# # print '4 neighbors', grid.compute_distance_field(grid.zombies)
# print
# zombies = grid._zombie_list
entity_list = ZOMBIE
# print "zombies", zombies
print "compute_distance_field", grid.compute_distance_field(entity_list)
#

test.phase1_test(Zombie)
test.phase2_test(Zombie)
# test.phase3_test(Zombie)
#
