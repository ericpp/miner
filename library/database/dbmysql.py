#########################
# DATABASE ABSTRACTIONS #
#########################

import mysql.connector
from db import DB

class DBMySQL(DB):
	# Function to connect to database
	# Abstract this eventually to make more DB options available
	def __init__(self, config):
		self.config = config

	def connect(self):
		self.conn = mysql.connector.connect(**self.config)

	def close(self):
		self.conn.close()

	def install_map(self, map):
		cursor = self.conn.cursor()

		db_name =  map.__class__.__name__

		cursor.execute("DROP DATABASE IF EXISTS ?;", db_name)
		cursor.execute("CREATE DATABASE IF NOT EXISTS ?", db_name)
		cursor.execute("USE ?", db_name)

		self.conn.commit()

		for dataset in map.get_datasets():
			self.install_dataset(dataset)

		self.conn.commit()
		cursor.close()


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
