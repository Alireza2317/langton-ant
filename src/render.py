import sys

import pygame as pg

from src.config import cfg
from src.types import Color, Position


class PGRenderer:
	def __init__(self, caption: str) -> None:
		pg.init()
		pg.display.set_caption(caption)
		self.screen: pg.Surface = pg.display.set_mode(cfg.screen_size)
		self.clock: pg.time.Clock = pg.time.Clock()
		self.fps: int = cfg.fps
		self.text_screen: pg.Surface = pg.Surface((150, 25))

		self.font: pg.font.Font = pg.font.Font(
			pg.font.get_default_font(), size=cfg.font_size
		)

		self.screen.fill(self.to_pg_color(cfg.bg_color))
		self.text_screen.fill(self.to_pg_color(Color.GRAY))

		self.update()

	def update(self) -> None:
		self.screen.blit(self.text_screen, (0, 0))
		pg.display.update()

	@staticmethod
	def to_pg_color(color: Color) -> pg.Color:
		color_map: dict[Color, pg.Color] = {
			Color.WHITE: pg.Color(255, 255, 255),
			Color.BLACK: pg.Color(0, 0, 0),
			Color.RED: pg.Color(255, 0, 0),
			Color.GREEN: pg.Color(0, 255, 0),
			Color.BLUE: pg.Color(0, 0, 255),
			Color.GRAY: pg.Color(70, 70, 70),
		}
		return color_map[color]

	def get_coords(self, pos: Position) -> tuple[int, int]:
		return (
			cfg.cell_size * pos.x + int(cfg.screen_size[0] * 0.9),
			cfg.cell_size * pos.y + int(cfg.screen_size[1] * 0.3),
		)

	def draw_square(self, pos: Position, color: Color) -> None:
		pg.draw.rect(
			self.screen,
			self.to_pg_color(color),
			rect=(*self.get_coords(pos), *(cfg.cell_size,) * 2),
		)

	def put_text(self, text: str, coordinate: Position, color: Color) -> None:
		self.text_screen.fill(self.to_pg_color(Color.GRAY))
		self.text_screen.blit(
			self.font.render(f"{text}", True, self.to_pg_color(color)),
			(coordinate.x, coordinate.y),
		)

	def handle_events(self) -> None:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_q:
					pg.quit()
					sys.exit()
				if event.key == pg.K_UP:
					self.fps = min(self.fps + 1, 150)
				if event.key == pg.K_DOWN:
					self.fps = max(self.fps - 1, 1)

	def clear(self) -> None:
		self.screen.fill(self.to_pg_color(cfg.bg_color))

	def step(self) -> None:
		self.handle_events()

		self.update()
		self.clock.tick(self.fps)
