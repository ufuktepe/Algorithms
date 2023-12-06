class Robot:
    def __init__(self, room, pos):
        self.room = room
        self.x = pos[0]
        self.y = pos[1]
        self.d = 0
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def get_x_dir(self):
        return self.directions[self.d][0]

    def get_y_dir(self):
        return self.directions[self.d][1]

    def move(self):
        n_x = self.x + self.get_x_dir()
        n_y = self.y + self.get_y_dir()
        if not (0 <= n_x < len(self.room) and 0 <= n_y < len(self.room[0])):
            return False
        if self.room[n_x][n_y] == 0:
            return False
        self.x = n_x
        self.y = n_y
        return True

    def turnLeft(self):
       self.d = (self.d + 1) % 4

    def clean(self):
       self.room[self.x][self.y] = 2


class Solution:
    def cleanRoom(self, robot):
        pos = (0, 0)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        d = 0
        explored = set()

        def turn_left(d):
            robot.turnLeft()
            return (d + 1) % 4

        def move_back():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        def move(from_pos, to_pos, d):
            from_x, from_y = from_pos
            to_x, to_y = to_pos
            for _ in range(4):
                i, j = directions[d]
                if i + from_x == to_x and j + from_y == to_y:
                    robot.move()
                    break
                d = turn_left(d)
            return d

        def get_neighbors(pos, d):
            neighbors = []
            x, y = pos
            for _ in range(4):
                if robot.move():
                    n_x, n_y = x + directions[d][0], y + directions[d][1]
                    neighbors.append((n_x, n_y))
                    move_back()
                d = turn_left(d)

            return neighbors

        def visit(pos, d):
            explored.add(pos)
            neighbors = get_neighbors(pos, d)
            for neighbor in neighbors:
                if neighbor not in explored:
                    new_pos = neighbor[0], neighbor[1]
                    d = move(pos, new_pos, d)
                    d = visit(new_pos, d)
                    d = move(new_pos, pos, d)

            robot.clean()
            return d

        visit(pos, d)

    def cleanRoom_v2(self, robot):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def move_back():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        def turn_left(d):
            robot.turnLeft()
            return (d + 1) % len(directions)

        def visit(pos, d, explored):
            explored.add(pos)
            robot.clean()

            for _ in range(len(directions)):
                next_x = pos[0] + directions[d][0]
                next_y = pos[1] + directions[d][1]
                new_pos = (next_x, next_y)
                if new_pos not in explored and robot.move():
                    visit(new_pos, d, explored)
                    move_back()
                d = turn_left(d)

        d = 0
        pos = (0, 0)
        explored = set()
        visit(pos, d, explored)



room = [[1, 0],
        [1, 0],
        [1, 1]]

robot = Robot(room, [2, 0])

sltn = Solution()
sltn.cleanRoom_v2(robot)

print(robot.room)















