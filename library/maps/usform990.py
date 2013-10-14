"""
miner map for US Non-Profit Form 990 data
Data is released publicly by CitizenAudit
"""

from library.miner.map import Map

class USForm990(Map):
	description = 'US Non-Profit Form 990 Tax information released by CitizenAudit'
	homepage = 'http://www.citizenaudit.org'
	datasets = {
		'usform990': {
			'type': 'csv',
			'url': 'http://s3.citizenaudit.org/irs/bulk/manifest.csv.gz',
			'file': 'manifest.csv.gz',
			'columns': (
				( 'url', 'text' ), 
				( 'filename', 'varchar(255)' ), 
				( 'doctype', 'varchar(255)' ), 
				( 'year', 'year' ), 
				( 'ein', 'int(255)' ), 
				( 'name', 'text' ), 
				( 'formtype', 'int(255)' ), 
				( 'formdate', 'date' ), 
				( 'size', 'text' ), 
				( 'assets', 'int(255)' ), 
				( 'ocrstatus', 'text DEFAULT NULL' ), 
				( 'ocradded', 'datetime DEFAULT NULL' ), 
				( 'id', 'int(255)' )
			)
		}
	}
