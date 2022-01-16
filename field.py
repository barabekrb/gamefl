from __future__ import annotations

from typing import Optional, List
from random import choice, seed
from time import time
from copy import deepcopy
from itertools import product

from cell import Cell


class Field:
    def __init__(self, row_num: int, col_num: int, fill: bool = True) -> None:
        self.row_num: int = row_num
        self.col_num: int = col_num
        self.field: List[List[Cell]] = []

        if fill:
            self.fill()

    def fill(self) -> None:
        for _ in range(self.row_num):
            row: List[Cell] = []
            for _ in range(self.col_num):
                cell = Cell(choice((True, False)))
                row.append(cell)
            self.field.append(row)

    def new_state(self) -> Field:
        new_field: Field = deepcopy(self)
        neighbours_num: int = 0
        seed(time)

        for x in range(self.row_num):
            for y in range(self.col_num):
                for offset_x, offset_y in product(range(-1, 2), range(-1, 2)):
                    if (
                        0 <= x + offset_x < self.row_num
                        and 0 <= y + offset_y < self.col_num
                    ):
                        neighbours_num += int(self.field[x + offset_x][y + offset_y].value)
                neighbours_num -= int(self.field[x][y].value)
                if new_field.field[x][y]:
                    if not neighbours_num in [2, 3]:
                        new_field.field[x][y] = Cell(False)
                else:
                    if neighbours_num == 3:
                        new_field.field[x][y] = Cell(True)
                neighbours_num = 0
        return new_field
