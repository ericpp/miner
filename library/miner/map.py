# The basic form of a Map...
# Should be general enough that it can fit all maps (unless there seems good reason to ignore this)
# Should be specific enough that it does a lot of the heavy lifting for Maps

import os

from dataset import Dataset

DATASET_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'datasets')

class Map(object):

	# URL for homepage of dataset (e.g. http://census.gov/)
	homepage = ''

	def get_dataset(self, name):
		path = os.path.join(DATASET_DIR, self.__class__.__name__)
		return Dataset(name, path, self.datasets[name])

	def get_datasets(self):
		for name in self.datasets.iterkeys():
			yield self.get_dataset(name)

	# These are the main methods used by maps
	def download(self):
		for name in self.datasets.keys():
			ds = self.get_dataset(name)
			ds.download()
