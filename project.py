# Reeborg's World Simulator

class Reeborg:
    def __init__(self, world_size, start_position=(0, 0), start_direction="N"):
        self.world_size = world_size  # (rows, cols)
        self.position = list(start_position)  # [row, col]
        self.direction = start_direction  # "N", "E", "S", "W"
        self.world = [[" " for _ in range(world_size[1])] for _ in range(world_size[0])]
        self.carrying_object = False

    def move(self):
        # Move one step in the direction the robot is facing
        if self.direction == "N" and self.position[0] > 0:
            self.position[0] -= 1
        elif self.direction == "E" and self.position[1] < self.world_size[1] - 1:
            self.position[1] += 1
        elif self.direction == "S" and self.position[0] < self.world_size[0] - 1:
            self.position[0] += 1
        elif self.direction == "W" and self.position[1] > 0:
            self.position[1] -= 1
        else:
            print("Blocked! Cannot move.")

    def turn_left(self):
        # Change direction 90 degrees to the left
        directions = ["N", "W", "S", "E"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_right(self):
        # Change direction 90 degrees to the right
        directions = ["N", "E", "S", "W"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def front_is_clear(self):
        # Check if the front is clear based on the robot's direction
        if self.direction == "N" and self.position[0] > 0:
            return True
        elif self.direction == "E" and self.position[1] < self.world_size[1] - 1:
            return True
        elif self.direction == "S" and self.position[0] < self.world_size[0] - 1:
            return True
        elif self.direction == "W" and self.position[1] > 0:
            return True
        return False

    def wall_in_front(self):
        # Opposite of front_is_clear()
        return not self.front_is_clear()

    def at_goal(self, goal_position):
        # Check if the robot is at the goal position
        return self.position == list(goal_position)

    def put(self):
        # Place an object at the robot's current position
        self.world[self.position[0]][self.position[1]] = "O"
        self.carrying_object = False

    def take(self):
        # Pick up an object at the robot's current position
        if self.world[self.position[0]][self.position[1]] == "O":
            self.world[self.position[0]][self.position[1]] = " "
            self.carrying_object = True

    def object_here(self):
        # Check if there is an object at the robot's current position
        return self.world[self.position[0]][self.position[1]] == "O"

    def carries_object(self):
        # Check if the robot is carrying an object
        return self.carrying_object


# Initialize the world and robot
robot = Reeborg(world_size=(5, 5), start_position=(2, 2))

# Example Usage
robot.turn_left()
robot.move()
robot.put()
print("Robot at:", robot.position, "Facing:", robot.direction)
print("World Grid:")
for row in robot.world:
    print(row)
