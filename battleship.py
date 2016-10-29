#!/usr/bin/python3
import pdb
from lib.board import Board
from IPython import embed

def setup(ships_each):
    for j in range(2):
        print('player ' + str(j) + ' selct your ships!')
        for i in range(ships_each):
            name = input('Name your ship (must be unique): ')
            name = "%s%s" % (name, str(j)) # this is how we identify the ship
            point_x = input('Initial point(x): ')
            point_y = input('Initial point(y): ')
            point = (int(point_y),int(point_x))
            direction = input('Direction (N,S,E,W): ')
            board.insert_ship(point, direction, 4, name) 

board = Board(16)
setup(3)
