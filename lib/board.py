class Board:
    board = []
    ships = []
    board_size = 0

    def __init__(self, size):
        self.board = [["miss" for x in range(size)] for y in range(size)]
        self.ships = []
        self.board_size = size

    def insert_ship(self, point, direction, length, uid):
        if uid in self.ships:
            print("there is already a ship with that name!")
            return False # dont add the ship
        # import ipdb; ipdb.set_trace()
        if uid in ["miss", "boom"]:
            print("dont name it that!")
            return False
        if not self.board[point[0]][point[1]] is "miss":
            print("there is already a ship there!")
            return False # dont add the ship
        self.ships.append(uid) # do add the ship

        if direction is "N":
            for i in range(length):
                self.board[point[0]+i][point[1]] = uid
        elif direction is "S":
            for i in range(length):
                self.board[point[0]-i][point[1]] = uid
        elif direction is "E":
            for i in range(length):
                self.board[point[0]][point[1]+i] = uid
        elif direction is "W":
            for i in range(length):
                self.board[point[0]][point[1]-i] = uid

        return True

    def check_point(self, point):
        import pdb; pdb.set_trace()
        print("the board spot is")
        print(self.board[point[0]][point[1]])
        if not self.board[point[0]][point[1]] is "miss":
            return True
        else:
            return False

    def attack(self, point):
        # make sure it isnt out of range
        if point[0] > self.board_size or point[1] > self.board_size:
            return False

        if self.check_point(point):
            self.board[point[0]][point[1]] = "boom"
            return True
        else:
            return False

    def ships_by_player(self):
        split_ships = []
        for i in range(2):
            part = []
            for ship in self.ships:
                if ship.endswith(str(i)): part.append(ship)
            split_ships.append(part)
        return split_ships

    def check_in_range(self, point, direction, length):
        # todo: implement this
        return
