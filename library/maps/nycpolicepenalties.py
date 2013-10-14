""" 
miner map for NYC Police Department Penalties data
Data is released publicly by the City of New York
"""

from library.miner.map import Map

class NYCPolicePenalties(Map):
	description = 'US Non-Profit Form 990 Tax information released by CitizenAudit'
	homepage = 'http://data.cityofnewyork.us'
	datasets = {
		'nycpolicepenalties': {
			'type': 'csv',
			'url': 'https://data.cityofnewyork.us/api/views/ns22-2dcm/rows.csv',
			'sha1': '5196b33fbda7287e3985844e5cd24ba779063660',
			'file': 'rows.csv',
			'columns': (
				( 'year', 'year' ),
				( 'penalties', 'text' ),
				( 'officer_count', 'integer' )
			)
		}
	}

