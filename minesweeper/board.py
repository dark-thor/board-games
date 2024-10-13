from tile import Tile
import random

class Board:
    tiles = []
    size = 0
    def __init__(self, size: int, mine_count: int):
        self.size = size
        self.mine_count = mine_count
        for r in range(size):
            row = []
            for c in range(size):
                row.append(Tile(r,c))
            self.tiles.append(row)
        self.generate_board()

    def show_solution(self):
        for row in self.tiles:
            print(''.join(col.value for col in row))

    def display_board(self):
        for row in self.tiles:
            print(''.join(col.display for col in row))

    def count_neighbour_mines(self, row, col):
        size = len(self.tiles)
        count = 0
        for r in range(max(0,row-1), min(row+2, size)):
            for c in range(max(0,col-1), min(col+2, size)):
                if self.tiles[r][c].value == 'M' and (r != row or c != col):
                    count = count + 1
        return count

    def generate_board(self):
        if (self.size <= 0 or self.mine_count <= 0
                or self.mine_count > self.size*self.size):
            raise ValueError(f"Board size: {self.size} with"
                                + f" mine_count: {self.mine_count} is invalid")

        # place mines
        mine_coordinates = [divmod(ele, self.size)
                                for ele in random.sample(
                                    range(self.size * self.size),
                                    self.mine_count
                                )]
        for mine_row, mine_col in mine_coordinates:
            self.tiles[mine_row][mine_col].set_mine()

        # set values
        for r in range(self.size):
            for c in range(self.size):
                if self.tiles[r][c].value == 'M':
                    continue
                count = self.count_neighbour_mines(r, c)
                self.tiles[r][c].value = str(count)

    def is_solved(self):
        for r in range(self.size):
            for c in range(self.size):
                if (self.tiles[r][c].value == 'M'
                        or self.tiles[r][c].value == self.tiles[r][c].display):
                    continue
                else:
                    return False
        return True

    def open_tile(self, row:int, col: int):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return

        if (self.tiles[row][col].value == 'M'):
            raise Exception("Landed on a mine")
        count = self.count_neighbour_mines(row, col)
        self.tiles[row][col].display = str(count)

        # if no mines around, open all unopened neighbouring tiles
        if count == 0:
            for r in range(max(0,row-1), min(row+2, self.size)):
                for c in range(max(0,col-1), min(col+2, self.size)):
                    if self.tiles[r][c].display == 'X':
                        self.open_tile(r, c)
