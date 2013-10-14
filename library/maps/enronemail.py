"""
miner map for Enron Emails
Data is released publicly by CitizenAudit
"""

from library.miner.map import Map

class EnronEmail(Map):
	description = 'Enron Company Emails released by CALO Project'
	homepage = 'http://www.cs.cmu.edu/~enron/'
	datasets = {
		'emails': {
			'type': 'mbox',
			'url': 'http://www.cs.cmu.edu/~enron/enron_mail_20110402.tgz',
			'files': 'enron_mail_20110402/maildir/*/*/*',
			'columns': (
				( 'message_id', 'varchar(255)' ), 
				( 'from' 'varchar(255)' ), 
				( 'to' 'varchar(255)' ), 
				( 'subject' 'varchar(255)' ), 
				( 'folder' 'varchar(255)' ), 
				( 'date' 'datetime' )
			)
		}
	}
