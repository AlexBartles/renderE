# Send Domestic iStar logs to some StarLogging system via the backchannel.

import sys
import time
from twc.Archives import *
from twc.FileSet  import *
from twc.BackchannelJobs import *
import twc.dsmarshal as dsm
import twc.DataStoreInterface as ds

# shell command to produce a histogram of Thunderstorm frame drifts
cntFd = "grep -Z 'frame time drift' /var/log/clientlog.0.gz | cut -d' ' -f7 | sort -n | uniq -c"

# Pick a distinct temp directory in which to stash files for the Archive.
tarDir =  '/tmp/backchannel/daily'

# The value of the control flag must be set in the datastore.
# Its current value gets re-checked every time the script is run.
flag = 'productionMachine'
ds.init()
backchannelLogFlag = dsm.defaultedGet(flag, 0)
ds.uninit()

if backchannelLogFlag == 0:
    Log.warning('%s =0 at startup. Backchannel logs will NOT be sent' % flag)
else:
    Log.info('%s is set at startup. Backchannel logs WILL be attempted' % flag)

# Specify the sets of files and put them in the tar-dir
uptm     = FileSetCmd('/usr/bin/uptime',      'uptime.log')
pkgs     = FileSetCmd('/usr/sbin/pkg_info',   'pkg.log')
procs    = FileSetCmd('/bin/ps -xO start',    'proc.log')
irdStats = FileSetCmd('/usr/twc/digi/util/runomni /usr/twc/digi/util/getIrdInfo.pyc', 'irdStats.log')
uname    = FileSetCmd('/usr/bin/uname -sr',   'uname.log')

# always send a histogram of _yesterday's_ frame drifts
drift  = FileSetCmd(cntFd,   'frameDrift.log')

datastoreFileName = 'datastore.vals'
pers   = FileSetDatastore(['personality',], datastoreFileName )
keys   = FileSetDatastoreIndirect('backchannKeyList', datastoreFileName )

asrun  = FileSetRunLogs('/twc/data/volatile/eventlogs/runlog_*.log')

# explicitly send only the clientlog from yesterday
clilog = FileSetEncrypt(['/var/log/clientlog.0.gz',] )

# Create an Archive Job to handle the transmission.
# (archive jobs schedule themselves randomly in the 3 hrs after midnight)
archiv = Archive(tarDir)
archiv.addFileSets([uptm, pkgs, procs, uname, irdStats, drift, pers, keys, asrun, clilog])

bjob = BackchannelJob(archiv, 'BackchannDaily', 120, 3)

# For testing, uncomment the 2 lines below:  (do not 'reschedule')
#Log.info('replacing initially scheduled run-time with job-script override')
#bjob.scheduleIn(10)
