import enum
from dataclasses import dataclass


@dataclass
class Position:
	x: int
	y: int

	def as_tuple(self) -> tuple[int, int]:
		return (self.x, self.y)


class Color(enum.Enum):
	WHITE = enum.auto()
	BLACK = enum.auto()
	RED = enum.auto()
	GREEN = enum.auto()
	BLUE = enum.auto()
	GRAY = enum.auto()
