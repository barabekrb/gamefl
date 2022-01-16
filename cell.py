from typing import Optional, List


class Cell:
    def __init__(self, value: Optional[bool] = None) -> None:
        self.value: bool = value or False

    def __bool__(self) -> bool:
        return self.value


    def __repr__(self) -> str:
        return '■' if self.value else '□'
