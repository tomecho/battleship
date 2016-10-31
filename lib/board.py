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
        print(point[0])
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

    def check_in_range(self, point, direction, length):
        # todo: implement this
        return
