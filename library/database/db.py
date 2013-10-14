"""
DATABASE ABSTRACTIONS
"""

class DB(object):
	# Function to connect to database
	# Abstract this eventually to make more DB options available
	'''
	config = {
		'user': 'specialuser',
		'password': 'specialpass',
		'host': 'localhost',
		'raise_on_warnings': False,
	}
	'''
	def connect(self):
		raise NotImplementedError("connect is not implemented")

	def close(self):
		raise NotImplementedError("close is not implemented")

	def install_map(self, map):
		raise NotImplementedError("install_map is not implemented")

	## NEED TO FIX ERROR HANDLING HERE

	# except db.Error as err:
	#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	#     print("Something is wrong with your user name or password")
	#    elif err.errno == errorcode.ER_BAD_DB_ERROR:
	#      print("Database does not exist")
	#    else:
	#      print(err)
	#  else:
	#    cnx.close()


	# from mysql.connector import errorcode
	# try:
	#   cnx = mysql.connector.connect(**config)
	#   return cnx
	# except mysql.connector.Error as err:
	#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	#     print("Something is wrong with your user name or password")
	#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
	#     print("Database does not exist")
	#   else:
	#     print(err)
	# else:
	#   cnx.close()