import cv2
import numpy as np

from entity import Entity

class Actor(Entity):
	def __init__(self, pos):
		# set actor qualities
		self.name = "MISSING NAME";
		self.stats = [0, 0, 0]; # HP, Attack, Agility

		# set visual qualities inside each actor
		self.img = None;
		self.mask = None;
		self.layer = 2; # all actors default 2nd layer

		super().__init__(pos, self.img, self.mask, self.layer);

class Player(Actor):
	def __init__(self, pos, name, img_file, mask_file):
		super().__init__(pos);

		# set qualities
		self.name = name;
		self.stats = [5,2,2];
		self.vision = 4;

		# visual rep
		self.img = cv2.imread(img_file);
		self.mask = cv2.imread(mask_file);

		# action dict
		self.move_dict = {
			"left" : (-1,0),
			"right" : (1,0),
			"up" : (0,-1),
			"down" : (0,1),
		}

	# process movement words
	def move(self, direction_str):
		shift = self.move_dict[direction_str];
		self.pos[0] += shift[0];
		self.po1[1] += shift[1];
