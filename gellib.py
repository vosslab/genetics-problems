
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

### ugly code, but works

class GelClass(object):
	def __init__(self):
		self.row = 0
		self.img = None
		self.factor = 13
		self.max_distance = None
		pass

	def initImage(self):
		if self.max_distance is not None:
			width = self.max_distance * self.factor + 500
		else:
			width = 2048
		self.img = Image.new("RGB", (width,4096), (212,212,212))

	def drawLane(self, subindex, text=""):
		if self.img is None:
			self.initImage()
		self.row += 1
		sub_band_tree = self.indexToSubSet(self.band_tree, subindex)
		height = 22 * self.factor
		rowgap = 5 * self.factor
		draw1 = ImageDraw.Draw(self.img, "RGB")
		miny = int((self.row-1)*height + rowgap)
		maxx = int((self.row)*height)
		xshift = 350
		fnt = ImageFont.truetype('/Users/vosslab/Library/Fonts/LiberationSansNarrow-Regular.ttf', 8*self.factor)
		draw1.text((rowgap, miny+20), text, font=fnt, fill="black")
		for band_dict in sub_band_tree:
			start = xshift+band_dict['start']*self.factor
			end = start + band_dict['width']*self.factor
			draw1.rectangle(((start, miny), (end, maxx)), fill="blue", outline="black")

	def blankLane(self):
		self.row += 0.3

	def saveImage(self, filename):
		self.img.save(filename, "PNG")

	def getRandomSubSet(self, setsize, subsize):
		subindex = random.sample(xrange(setsize), subsize)
		return set(subindex)

	def indexToSubSet(self, mylist, indices):
		newlist = []
		for i in indices:
			newlist.append(mylist[i])
		return newlist

	def createBandTree(self, total_bands=12):
		min_band_width = 2
		max_band_width = 12
		min_gap = 3
		max_gap = 8
		self.band_tree = []
		start_point = 2
		for i in range(total_bands):
			width = random.randint(min_band_width, max_band_width+1)
			gap = random.randint(min_gap, max_gap+1)
			start_point += gap
			band_dict = {
				'width': width,
				'start': start_point,
			}
			start_point += width
			self.max_distance = start_point + gap
			self.band_tree.append(band_dict)
		return self.band_tree




