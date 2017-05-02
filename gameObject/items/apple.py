import pygame

from gameObject.items import item
from utils import utility
from utils.setting import DEFAULT_ITEM_SIZE, APPLE


class Apple(item.Item):
	def __init__(self, itemGenerator, location, size = DEFAULT_ITEM_SIZE, image = None):
		self.location = location
		self.image_size = size
		if image is None:
			self.image = utility.loadImage("apple")
		else:
			self.image = image
		self.image = utility.resizeImage(image, (self.image_size, self.image_size))
		item.Item.__init__(self, itemGenerator, self.image, location)
		self.type = APPLE

	def effect(self, score, snake):
		point = 100
		score.up(point)
		snake.addLength()