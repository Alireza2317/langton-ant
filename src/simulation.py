from typing import Literal

from src.ant import Ant, Direction
from src.config import cfg
from src.render import PGRenderer
from src.types import Color, Position


class Simulation:
	def __init__(self) -> None:
		self.renderer = PGRenderer("Langton's Ant Simulation")
		self.ant = Ant(Position(x=0, y=0))
		self.steps: int = 0

		self.world: dict[tuple[int, int], Literal[Color.WHITE, Color.BLACK]] = {}

	def flip_color(self, pos: Position) -> None:
		current_color: Color = self.world.get(pos.as_tuple(), Color.BLACK)
		self.world[pos.as_tuple()] = (
			Color.BLACK if current_color == Color.WHITE else Color.WHITE
		)

	def run(self) -> None:
		while True:
			self.steps += 1

			self.renderer.put_text(f"Step {self.steps}", Position(3, 3), Color.WHITE)

			current_cell_color: Color = self.world.get(
				self.ant.pos.as_tuple(), Color.BLACK
			)

			# Rules
			if current_cell_color == Color.BLACK:
				self.ant.turn(Direction.LEFT)
			elif current_cell_color == Color.WHITE:
				self.ant.turn(Direction.RIGHT)

			self.flip_color(self.ant.pos)

			self.renderer.draw_square(self.ant.pos, self.world[self.ant.pos.as_tuple()])

			self.ant.move()

			self.renderer.draw_square(self.ant.pos, cfg.ant_color)

			self.renderer.step()
