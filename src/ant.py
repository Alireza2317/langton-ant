import enum
from typing import Literal

from src.types import Position


class Direction(enum.Enum):
	UP = enum.auto()
	RIGHT = enum.auto()
	DOWN = enum.auto()
	LEFT = enum.auto()


class Ant:
	def __init__(self, pos: Position) -> None:
		self.pos: Position = pos
		self.dir: Direction = Direction.RIGHT

	def turn(self, dir: Literal[Direction.RIGHT, Direction.LEFT]) -> None:
		offset: int = 1 if dir == Direction.RIGHT else -1
		directions = list(Direction)
		self.dir = directions[(directions.index(self.dir) + offset) % 4]

	def move(self) -> None:
		match self.dir:
			case Direction.UP:
				self.pos.y -= 1
			case Direction.RIGHT:
				self.pos.x += 1
			case Direction.DOWN:
				self.pos.y += 1
			case Direction.LEFT:
				self.pos.x -= 1
