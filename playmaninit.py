import rendereglobals as rg
import os
import domesticpy.plugin.playman.playCmd.local as pmlc
import domesticpy.plugin.playman.playCmd.pm as pm
import domesticpy.plugin.playman.playCmd.ldl as pmldl
import domesticpy.plugin.playman.playCmd.bulletin as pmbl
import twccommon.embedded

twccommon.embedded.runconfpy(os.path.join(os.path.dirname(__file__), "domesticpy", "conf", "playman.py"))

pm.init(rg.configs["playman"])
pmlc.init(rg.configs["playman"])
pmldl.init(rg.configs["playman"])
pmbl.init(rg.configs["playman"])