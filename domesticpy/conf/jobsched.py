import twccommon.Log as Log

level = Log.INFO      # one of: DBG, INFO, WARN, ERR, CRIT

Log.setLevel(level)
Log.info('JobSched logging level set to %s' % level)
