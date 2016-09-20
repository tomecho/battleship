#!/usr/bin/python3
import pdb
from .board import board

def setup(ships_each):
    for j in range(2):
        print('player' + j + 'selct your ships!')
        for i in range(ships_each):
            name = input('Name your ship (must be unique): ')
            name += j # this is how we identify the ship
            point = input('Initial point: ')
            direction = input('Direction (N,S,E,W): ')
            board.insert_ship(point, direction, 4, name) 

board = Board(16)
setup()
