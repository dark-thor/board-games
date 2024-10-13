from enum import Enum

TileStatus = Enum('TileStatus', ['CLOSED', 'OPEN'])
class Tile:
    def __init__(self, row: int, col: int,
                 status=TileStatus.CLOSED, value='X', display='X'):
        self.row = row
        self.col = col
        self.status = status
        self.value = value
        self.display = display

    def set_mine(self):
        self.value = 'M'

    def set_value(self, value: str):
        self.value = value

    def set_display(self, display: str):
        self.display = display
