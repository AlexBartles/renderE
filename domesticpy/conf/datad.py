
import os
import twc.embedded.datad.config


TWCPERSDIR = os.environ['TWCPERSDIR']
config = twc.embedded.datad.config.Config()

config.setPidFileDir(TWCPERSDIR + '/data/pid')
config.setAppName('datad')

# name of the main data file 
config.setDataFileName(TWCPERSDIR + '/data/datastore/ds.dat')
config.setStaticFileName(TWCPERSDIR + '/data/datastore/ds.stat')

# name of the file that logs transactions made between the
# times that the main data file is updated
config.setLogFileName(TWCPERSDIR + '/data/datastore/ds.log')

# max size of an outstanding transaction, i.e. the max. number of
# commands allowed before an update or a commit
config.setMaxTransactionSize(10000)

# how often an attempt is made to look for and delete expired entries
config.setExpirationFrequency(30)

# Set the max number of expired items that will be deleted in one attempt. 
# The idea is to keep this low to avoid deleting a lot of entries at once
# so that the main job of servicing query/modification requests will
# not be starved.
config.setExpirCheckLimit(2000)

# how often the main data file is updated and the log file is truncated
config.setLogTruncateFrequency(60)

