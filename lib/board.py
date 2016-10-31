class Board:
    board = []
    ships = []

    def __init__(self, size):
        self.board = [["miss" for x in range(size)] for y in range(size)] 
        self.ships = []

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
        True if not self.board[point[0]][point[1]] is "miss" else False

    def attack(self, point):
        if check_point(point):
            self.board[point[0]][point[1]] = "boom"
            return True
        else:
            return False

    def ships_by_player(self):
        split_ships = []
        for i in range(2):
            part = []
            for ship in self.ships:
                if ship.endswith(str(i)): part.push(ship) 
            split_ships.push(part)
        return split_ships

    def check_in_range(self, point, direction, length):
        # todo: implement this
        return
