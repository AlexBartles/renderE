#removes intro data
def scmtRemove(key):
    try:
        dsm.remove(key)
    except:
        pass
scmtRemove("Config.1.Local_Intro")