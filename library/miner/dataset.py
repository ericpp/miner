import os
import urllib2
import tempfile
import hashlib
import urlparse
import tarfile
import zipfile
import gzip

import fnmatch
import csv

class Dataset(object):
	def __init__(self, name, path, dataset):
		self.name = name
		self.path = path
		self.type = dataset['type']
		self.url = dataset['url']
		#self.files = dataset['files']
		self.columns = dataset['columns']

	def get_filepath(self):
		urlinfo = urlparse.urlparse(self.url)
		filename = os.path.basename(urlinfo.path)
		return os.path.join(self.path, filename)

	# Downloads the dataset to the dataset directory
	def download(self):
		if not os.path.exists(self.get_filepath()):
			u = urllib2.urlopen(self.url)
			f = tempfile.NamedTemporaryFile()
			h = hashlib.sha1()
			dest_path = self.get_filepath()

			meta = u.info()
			file_size = meta.getheaders("Content-Length")

			# TODO: use these to check for new versions of files
			last_modify = meta.getheaders("Last-Modified") # Last modify date of file
			etag = meta.getheaders("ETag") # File fingerprint

			file_size_int = None
			file_size_dl = 0
			block_sz = 8192

			if file_size and file_size[0] != '':
				file_size_int = int(file_size[0])

			print "Downloading: "

			while True:
				buffer = u.read(block_sz)

				if not buffer:
					break

				file_size_dl += len(buffer)
				h.update(buffer)
				f.write(buffer)

				print " %d bytes" % file_size_dl,

				if file_size_int is not None:
					print " %d%%" % ((file_size_dl * 100) / file_size_int)

			f.flush()

			file_sha1 = h.hexdigest()

			print "sha1: %s" % file_sha1

			if hasattr(self, 'sha1') and self.sha1 != file_sha1:
				raise "SHA1 Mismatch!"

			# create container directory
			if not os.path.exists(os.path.dirname(dest_path)):
				os.makedirs(os.path.dirname(dest_path))

			# copy file to dataset directory
			print "copying file to: %s" % dest_path

			with open(dest_path, 'wb') as dest:
				f.seek(0)
				dest.write(f.read())

			f.close()

		return True

	def get_files(self):
		filepath = self.get_filepath()

		if not os.path.exists(filepath):
			yield None

		fn, extension = os.path.splitext(filepath)

		if tarfile.is_tarfile(filepath):
			f = tarfile.open(filepath, 'r')
			finf = f.next()
			while finf:
				yield f.extractfile(finf.name)
				finf = f.next()
		elif zipfile.is_zipfile(filepath):
			f = zipfile.open(filepath)
			for fname in f.namelist():
				yield f.open(fname)
		elif extension == ".gz":
			f = gzip.open(filepath, 'rb')
			yield f
		else:
			yield open(filepath, 'rb')

	def get_column_names(self):
		return [ col[0] for col in self.columns ]

	def get_rows(self):
		for csvfile in self.get_files():
			csvreader = csv.reader(csvfile)
			for row in csvreader:
				yield row
