#########################
# DATABASE ABSTRACTIONS #
#########################

import sqlite3
from db import DB

class DBSQLite3(DB):
	def __init__(self, config):
		self.config = config

	def connect(self):
		self.conn = sqlite3.connect(**self.config)

	def close(self):
		self.conn.close()

	def install_map(self, map):
		for dataset in map.get_datasets():
			self.install_dataset(dataset)

	def install_dataset(self, dataset):
		cursor = self.conn.cursor()

		col_defs = [ ' '.join(col) for col in dataset.columns ]
		col_names =  [ col[0] for col in dataset.columns ]
		col_qs = ['?'] * len(col_names)

		cursor.execute('DROP TABLE IF EXISTS ' + dataset.name)
		cursor.execute('CREATE TABLE ' + dataset.name + ' (' + ', '.join(col_defs) + ')')

		query = 'INSERT INTO ' + dataset.name + ' (' + ', '.join(col_names) + ') VALUES (' + ', '.join(col_qs) + ')'
		cursor.executemany(query, dataset.get_rows())

		self.conn.commit()
		cursor.close()