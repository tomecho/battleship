#!/usr/bin/python3
import pdb
from lib.board import Board
from IPython import embed

def setup(ships_each):
    for j in range(2):
        print('player ' + str(j) + ' selct your ships!')
        for i in range(ships_each):
            while True:
                print('Ship ' + str(i))
                name = input('Name your ship (must be unique): ')
                name = "%s%s" % (name, str(j)) # this is how we identify the ship
                point_x = input('Initial point(x): ')
                point_y = input('Initial point(y): ')
                point = (int(point_y),int(point_x))
                direction = input('Direction (N,S,E,W): ')
                if board.insert_ship(point, direction, 4, name):
                    break

def play():
    i=0
    while True:
        # check winner condition
        ships = board.ships_by_player()
        if len(ships) is 1: # there is a winner
            ships[0]

        # there is no winner we must continue the battle(ship)
        player = "1" if i % 2 is 0 else "2"
        print('move ' + str(i) + ' player ' + player + "'s move")

board = Board(16)
setup(3)
play()
