from dataclasses import dataclass

from src.types import Color


@dataclass
class Config:
	# Colors
	ant_color: Color = Color.RED
	bg_color: Color = Color.BLACK

	cell_size: int = 5
	screen_size: tuple[int, int] = 1700, 1000

	font_size: int = 18

	fps: int = 20


cfg: Config = Config()
