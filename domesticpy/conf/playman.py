
import os
import config
import domestic
import twc.EventLog as EventLog
import twc.dsmarshal as dsm


TWCDIR     = os.environ['TWCDIR']
TWCCLIDIR  = os.environ['TWCCLIDIR']
TWCPERSDIR = os.environ['TWCPERSDIR']

config.set('twcDir',               TWCDIR)
config.set('twcCliDir',            TWCCLIDIR)
config.set('twcPersDir',           TWCPERSDIR)

config.set('appName',              'playman')
config.set('channel',              'SystemEventChannel')
config.set('pluginRoot',           TWCPERSDIR + '/plugin')
config.set('resourceRoot',         '/rsrc')
config.set('pidFileName',          TWCPERSDIR + '/data/pid')

config.set('heatSafetyDataFile',   TWCPERSDIR + '/data/heatSafetyTips.data')
config.set('tempDir',              TWCPERSDIR + '/data/volatile/tmp')
config.set('productRoot',          TWCPERSDIR + '/products')
config.set('productPluginRoot',    TWCPERSDIR + '/plugin/playman/products')
config.set('playlistPluginRoot',   TWCPERSDIR + '/plugin/playman/playlists')
config.set('heuristicPluginRoot',  TWCPERSDIR + '/plugin/playman/heuristics')
config.set('configSet',            0)
config.set('preroll',              8*30)

d = twc.Data()
d.productTitle = ['air quality', 'forecast']
d.bkgImage = ('domestic', None)
d.actionDayPhrase = 'Ozone Action Day'
dsm.setDefault('Config.1.Local_AirQualityForecast', d)

d = twc.Data()
d.productTitle = ['almanac', None]
d.bkgImage = ('domestic', 'domesticAlmanac')
dsm.setDefault('Config.1.Local_Almanac', d)

d = twc.Data()
d.productTitle = ['almanac', None]
d.bkgImage = ('domestic', 'domesticAlmanac')
dsm.setDefault('Config.1.Local_Climatology', d)

d = twc.Data()
d.productTitle = ['current', 'conditions']
d.bkgImage = ('domestic', None)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_CurrentConditions', d)

d = twc.Data()
d.productTitle = ('daypart', 'forecast')
d.bkgImage = ('domestic', None)
d.titleFadeInDuration = 5
d.titleFadeOutDuration = 5
dsm.setDefault('Config.1.Local_DaypartForecast', d)

d = twc.Data()
d.productTitle = ['the week', 'ahead']
d.bkgImage = ('domestic', None)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_7DayForecast', d)

d = twc.Data()
d.productTitle = ['extended','forecast']
d.bkgImage = ('domestic', None)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_ExtendedForecast', d)

d = twc.Data()
d.productTitle = ['getaway', 'forecast']
d.titlePointerColor = (212, 212, 212, 0)
d.mapProduct = None
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_GetawayForecast', d)

d = twc.Data()
d.productTitle = ['heat safety', 'tips']
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_HeatSafetyTips', d)

d = twc.Data()
d.productTitle = ('current', 'conditions')
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_LocalObservations', d)

d = twc.Data()
d.productTitle = ['outdoor activity','forecast']
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_OutdoorActivityForecast', d)

d = twc.Data()
d.productTitle = ['school day','weather']
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_SchoolDayWeather', d)

d = twc.Data()
d.productTitle = ['local','forecast']
d.bkgImage = ('domestic', None)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_TextForecast', d)

d = twc.Data()
d.productTitle = ['radar', 'satellite']
d.activeVocal = 1
d.activeVocalCue = 1
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
dsm.setDefault('Config.1.Local_RadarSatelliteComposite', d)

d = twc.Data()
d.productTitle = ['satellite', None]
d.activeVocal = 1
d.activeVocalCue = 1
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
dsm.setDefault('Config.1.Local_Satellite', d)

d = twc.Data()
# productTitle is set dynamically by product
d.productTitle = [ None, None ]
d.activeVocal = 1
d.activeVocalCue = 1
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
dsm.setDefault('Config.1.Local_RegionalForecastMap', d)
dsm.setDefault('Config.1.Local_MetroForecastMap', d)

d = twc.Data()
d.productTitle = ['regional','radar']
d.activeVocal = 1
d.activeVocalCue = 1
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
# maps don't have backgrounds
d.bkgImage         = [ None, None, ]
d.titleFadeOutDuration = 0
dsm.setDefault('Config.1.Local_RegionalDopplerRadar', d)

d = twc.Data()
d.productTitle = ['local','radar']
d.activeVocal = 1
d.activeVocalCue = 1
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
# maps don't have backgrounds
d.bkgImage         = [ None, None, ]
d.titleFadeOutDuration = 0
dsm.setDefault('Config.1.Local_MetroDopplerRadar', d)

d = twc.Data()
d.productTitle = ['regional','forecast']
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_RegionalForecastMap', d)

d = twc.Data()
d.productTitle = ['current','conditions']
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_RegionalObservationMap', d)

# NOTE: We don't display MetroObservationMap today, but the
# client supports it.
d = twc.Data()
d.productTitle = ['current','conditions']
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_MetroObservationMap', d)

d = twc.Data()
d.productTitle = ['local','forecast']
# set text1 background color for _Title.rs since this is a map
d.text1BkgColor    = (20,20,20,255)
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_MetroForecastMap', d)

d = twc.Data()
d.productTitle = ['weather','bulletin']
d.bkgImage = ('domestic', 'domesticBulletin')
d.activeVocal = 1
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_NWSHeadlines', d)

d = twc.Data()
d.productTitle = ['traffic','report']
d.bkgImage = ('domestic', None)
d.activeVocal = 1
d.activeVocalCue = 1
d.maxPageDuration = 14
d.minPageDuration = 7
dsm.setDefault('Config.1.Local_TrafficReport', d)

d = twc.Data()
d.productTitle = ['traffic','flow']
d.bkgImage = ('domestic', None)
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_TrafficFlow', d)

d = twc.Data()
d.productTitle = ['traffic','overview']
d.bkgImage = ('domestic', None)
d.activeVocalCue = 1
dsm.setDefault('Config.1.Local_TrafficOverview', d)

d = twc.Data()
d.productTitle = ('record', 'temperature')
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_RecordHighLow', d)

d = twc.Data()
d.ccBkgImage = 'ccBg'
d.fcstBkgImage = 'fcstTextBg'
dsm.setDefault('Config.1.Local_SqueezebackFade', d)

d = twc.Data()
d.bkgImage = ('ccBg', None)
dsm.setDefault('Config.1.Cc_CurrentConditions', d)

d = twc.Data()
d.bkgImage = ('fcstTextBg', None)
d.bkgFade = (15,15)
dsm.setDefault('Config.1.Fcst_TextForecast', d)

d = twc.Data()
d.bkgImage = ('fcstTextBg', 'fcstDaypartBg')
d.bkgFade = (15,15)
dsm.setDefault('Config.1.Fcst_DaypartForecast', d)

d = twc.Data()
d.bkgImage = ('fcstTextBg', 'fcstExtendedBg')
d.bkgFade = (15,15)
dsm.setDefault('Config.1.Fcst_ExtendedForecast', d)

d = twc.Data()
d.bkgImage = ('fcstTextBg', None)
d.bkgFade = (15,15)
dsm.setDefault('Config.1.Fcst_Unavailable', d)

d = twc.Data()
dsm.setDefault('Config.1.Radar_LocalDoppler', d)

d = twc.Data()
d.fname = '/images/localDopplerBb'
d.ext = 'tif'
d.origin = (12, 12)
dsm.setDefault('Config.1.Radar_Billboard', d)

d = twc.Data()
d.productTitle = ['marine', 'forecast']
d.bkgImage = ('domestic', 'domesticMarine')
dsm.setDefault('Config.1.Local_MarineForecast', d)

d = twc.Data()
d.productTitle = ['welcome to', 'hell']
d.bkgImage = ('domestic', None)
dsm.setDefault('Config.1.Local_TestPage', d)

d = twc.Data()
d.productTitle = ['tides', None]
d.bkgImage = ('domestic', 'domesticMarine')
dsm.setDefault('Config.1.Local_Tides', d)

d = twc.Data()
d.crawlRate = 3
dsm.setDefault('Config.1.Ldl_HurricaneWatch', d)


###
### Default Playlists (one's not currently managed by SCMT)
###
d = twc.Data()
d.prodPrefix = "BackgroundMusic"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,[]),
    ("Null",0,100,100,100,1,2,0,[]),
]
dsm.setDefault('Config.1.Playlist.BackgroundMusic.bkgMusic1', d)

d = twc.Data()
d.prodPrefix = "Background"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.Background.defaultBkg1', d)

d = twc.Data()
d.prodPrefix = "Bulletin"
d.childPrefixes = ["Logo", "TimeTemp"]
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,["logo1", "timeTemp1",]),
    ("Null",0,100,100,100,1,2,0,["nullLogo1", "nullTimeTemp1",]),
]
dsm.setDefault('Config.1.Playlist.Bulletin.bulletin1', d)

d = twc.Data()
d.prodPrefix = "Bulletin"
d.childPrefixes = ["Logo", "TimeTemp"]
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,["logo1", "timeTempDbs1",]),
    ("Null",0,100,100,100,1,2,0,["nullLogo1", "nullTimeTemp1",]),
]
dsm.setDefault('Config.1.Playlist.Bulletin.bulletinDbs1', d)

d = twc.Data()
d.prodPrefix = "Tag"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prod,prod,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,[]),
    ("Null",   0,100,100,100,1,2,0,[]),
]
dsm.setDefault('Config.1.Playlist.Tag', d)


d = twc.Data()
d.prodPrefix = "Tag"
d.childPrefixes = [];
d.units = "seconds"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prod,prod,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("LASCrawl",0, 50,  50, 50, 1, 1, 0, []),
    ("Default", 0, 70, 120, 10, 1, 1, 0, []),
    ("Null",    0,  1, 120,  1, 1, 2, 0, []),
]
dsm.setDefault('Config.1.Playlist.Tag.tag1', d)

d = twc.Data()
d.prodPrefix = "TimeTemp"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,[]),
    ("Null",0,100,100,100,1,2,0,[]),
]
dsm.setDefault('Config.1.Playlist.TimeTemp.timeTemp1', d)

d = twc.Data()
d.prodPrefix = "TimeTemp"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("DbsClock",0,100,100,100,1,1,0,[]),
    ("Null",0,100,100,100,1,2,0,[]),
]
dsm.setDefault('Config.1.Playlist.TimeTemp.timeTempDbs1', d)

d = twc.Data()
d.prodPrefix = "TimeTemp"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Null",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.TimeTemp.nullTimeTemp1', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",];
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Null",0,100,100,100,1,1,0,["nullTimeTemp1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.nationalDown', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",];
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("Shortcast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("ExtendedForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("Shortcast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("ExtendedForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("PromotionalMessage",0,40,40,40,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("Shortcast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("ExtendedForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("Shortcast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("ExtendedForecast",0,4,12,4,0,1,0,["timeTemp1", "logo1",]),
    ("Void",0,1,240,1,1,1,0,["timeTemp1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.nationalLongformUp', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",];
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SummaryForecast",0,4,8,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SunriseSunset",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SummaryForecast",0,4,8,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SunriseSunset",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("PromotionalMessage",0,40,40,40,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SummaryForecast",0,4,8,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SunriseSunset",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SummaryForecast",0,4,8,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("SunriseSunset",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Void",0,1,240,1,1,1,0,["timeTemp1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.nationalDefaultUp', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",];
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,1,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TravelForecast",0,4,12,4,0,1,1,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",1,4,4,4,0,1,2,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TravelForecast",1,4,12,4,0,1,2,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("PromotionalMessage",0,40,40,40,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",2,4,4,4,0,1,3,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TravelForecast",2,4,12,4,0,1,3,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",3,4,4,4,0,1,4,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("AirQualityForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("UVForecast",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TravelForecast",3,4,12,4,0,1,4,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Void",0,1,240,1,1,1,0,["timeTemp1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.nationalMorningUp', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",];
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("PromotionalMessage",0,40,40,40,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1",]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("TrafficTripTimes",0,4,4,4,0,1,0,["timeTemp1", "logo1",]),
    ("AirportDelayConditions",0,8,24,8,0,1,0,["timeTemp1", "logo1",]),
    ("HourlyForecast",0,4,12,12,0,1,0,["timeTemp1", "logo1",]),
    ("NationalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1",]),
    ("Void",0,1,240,1,1,1,0,["timeTemp1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.nationalMorningSevereUp', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo", "Background"];
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(name,inst,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("LASCrawl",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("LocalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentDewpoint",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentPressure",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentCeiling",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentVisibility",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentMTDPrecip",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("LocalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentDewpoint",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentPressure",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentCeiling",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentVisibility",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentMTDPrecip",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("PromotionalMessage",0,40,40,40,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("LocalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentDewpoint",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentPressure",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentCeiling",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentVisibility",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentMTDPrecip",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("Date",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("HurricaneWatch",0,6,6,1,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("TornadoWatch",0,6,120,6,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("LocalStarIDMessage",0,10,10,10,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentSkyTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentWinds",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentGusts",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentHumidity",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentApparentTemp",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentDewpoint",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentPressure",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentCeiling",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentVisibility",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("CurrentMTDPrecip",0,4,4,4,0,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
    ("Void",0,1,120,1,1,1,0,["timeTemp1", "logo1", "defaultBkg1"]),
]
dsm.setDefault('Config.1.Playlist.Ldl.ldl1', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",];
d.units = "seconds"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("DbsMetroForecasts",0,144,144,4,0,1,0,["timeTempDbs1", "logo1",]),
    ("DbsAirportDelays",0,196,196,4,0,1,0,["timeTempDbs1", "logo1",]),
    ("DbsCurrentConditions",0,120,120,4,0,1,0,["timeTempDbs1", "logo1",]),
    ("Void",0,1,460,1,1,2,0,["timeTempDbs1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.nationalDbsUp', d)

d = twc.Data()
d.prodPrefix = "Ldl"
d.childPrefixes = ["TimeTemp", "Logo",]
d.units = "percent"
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("LASCrawl",0,2,100,1,0,1,0,["timeTempDbs1", "logo1",]),
    ("DbsCurrentConditions",0,100,100,0,1,1,0,["timeTempDbs1", "logo1",]),
    ("Void",0,50,100,0,1,2,0,["timeTempDbs1", "logo1",]),
]
dsm.setDefault('Config.1.Playlist.Ldl.dbs1', d)

d = twc.Data()
d.prodPrefix = "LocalAvail"
d.childPrefixes = [];
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(name,inst,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.LocalAvail', d)

d = twc.Data()
d.loadHeuristic = "loadPriorityOneOnly_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.prodPrefix = "Fcst"
d.childPrefixes = [];
d.units = "seconds"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("TextForecast.1",0,14,60,14,1,1,0,[]),
    ("TextForecast.2",0,14,60,14,1,1,0,[]),
    ("DaypartForecast",0,14,60,14,1,1,0,[]),
    ("ExtendedForecast",0,14,60,14,1,1,0,[]),
    ("Unavailable",0,1,60,1,1,2,0,[]),
]
dsm.setDefault('Config.1.Playlist.Fcst.fcst1', d)

d = twc.Data()
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.prodPrefix = "Radar"
d.childPrefixes = [];
d.units = "seconds"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Billboard",0,3,3,3,0,2,0,[]),
    ("LocalDoppler",0,55,58,55,1,1,1,[]),
    ("Null",0,58,58,58,0,1,1,[]),
]
dsm.setDefault('Config.1.Playlist.Radar.radar1', d)

d = twc.Data()
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.prodPrefix = "Cc"
d.childPrefixes = [];
d.units = "percent"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("CurrentConditions",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.Cc.cc1', d)

d = twc.Data()
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.prodPrefix = "Logo"
d.childPrefixes = [];
d.units = "percent"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Default",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.Logo.logo1', d)

d = twc.Data()
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.prodPrefix = "Logo"
d.childPrefixes = [];
d.units = "percent"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Null",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.Logo.nullLogo1', d)

d = twc.Data()
d.prodPrefix = "Local"
d.childPrefixes = ["Tag", "Ldl", "BackgroundMusic"]
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Null",0,60,60,60,0,1,0,["tag1", "dbs1","bkgMusic1",]),
]
dsm.setDefault('Config.1.Playlist.DefaultUS.60.0', d)
dsm.setDefault('Config.1.Playlist.DefaultUS.60.1', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.60.0', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.60.1', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.60.0', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.60.1', d)


d = twc.Data()
d.prodPrefix = "Local"
d.childPrefixes = ["Tag", "Ldl", "BackgroundMusic"]
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
#(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Null",0,90,90,90,0,1,0,["tag1", "dbs1","bkgMusic1",]),
]
dsm.setDefault('Config.1.Playlist.DefaultUS.90.0', d)
dsm.setDefault('Config.1.Playlist.DefaultUS.90.1', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.90.0', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.90.1', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.90.0', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.90.1', d)

d = twc.Data()
d.prodPrefix = "Local"
d.childPrefixes = ["Tag", "Ldl", "BackgroundMusic"]
d.units = "seconds"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
    #(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
("Null",0,120,120,120,0,1,0,["tag1", "dbs1","bkgMusic1",]),
]
dsm.setDefault('Config.1.Playlist.DefaultUS.120.0', d)
dsm.setDefault('Config.1.Playlist.DefaultUS.120.1', d)
dsm.setDefault('Config.1.Playlist.DefaultUS.120.2', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.120.0', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.120.1', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.120.2', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.120.0', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.120.1', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.120.2', d)

d = twc.Data()
d.prodPrefix = "Local"
d.childPrefixes = []
d.units = "percent"
d.loadHeuristic = "loadPriority_v1"
d.overHeuristic = "overPriority_v1"
d.underHeuristic = "underPriority_v1"
d.playlist = [
#(prodName,prodInstance,optimal,max,min,step,priority,exclusive,childPlaylists)
    ("Null",0,100,100,100,1,1,0,[]),
]
dsm.setDefault('Config.1.Playlist.DefaultUS.57.0', d)
dsm.setDefault('Config.1.Playlist.WestCoastUS.57.0', d)
dsm.setDefault('Config.1.Playlist.SouthernCalifornia.57.0', d)


###
### viewport config (listed in depth order so it's easier to read!)
### ABANDON HOPE ALL YE WHO ENTER HERE: Please note that all of these layer depths
### were painstakingly selected to achieve the desired effect, please realize what
### you are doing before you change these depths. You're best option: Don't mess
### with them!
###
### You should know that LDL, TimeTemp, and Logo are "special" layers that can
### change depths dynamically based on who is calling for them to run. So once
### again, don't mess with the depths!
###
d = twccommon.Data(depth=10, repeat=0, x=0, y=0, w=720, h=480, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.LocalAvail', d)

d = twccommon.Data(depth=10, repeat=0, x=0, y=0, w=720, h=480, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.BackgroundMusic', d)


# NOTE: The Video is HERE at depth 25

d = twccommon.Data(depth=30, repeat=0, x=0, y=0, w=720, h=480, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Background', d)

d = twccommon.Data(depth=40, repeat=0, x=0, y=140, w=216, h=340, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Cc', d)

d = twccommon.Data(depth=40, repeat=0, x=0, y=0, w=720, h=140, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Fcst', d)

# the -12 "shift" down and left is to compensate for the fact that the radar smoothing
# algorithm can't currently smooth the edge cases. And it just so happens that the
# widest smoothing 'kernel' width that we use today is 12 pixels wide so in the worst edge
# case we'll have to "hide" a 12 pixel width all the way around the map edges (outside the
# viewport) by shifting the image down and to the left. Note: Map size = 240, 137
d = twccommon.Data(depth=42, repeat=0, x=0, y=140, w=216, h=132, sx=1, sy=1, tx=-12, ty=-12)
dsm.setDefault('Config.1.viewport.Radar', d)

d = twccommon.Data(depth=50, repeat=0, x=0, y=0, w=720, h=480, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Local', d)

d = twccommon.Data(depth=51, repeat=0, x=0, y=0, w=720, h=140, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Ldl', d)

d = twccommon.Data(depth=52, repeat=0, x=458, y=57, w=262, h=23, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.TimeTemp', d)

d = twccommon.Data(depth=53, repeat=0, x=554, y=46, w=95, h=74, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Logo', d)

d = twccommon.Data(depth=60, repeat=0, x=0, y=0, w=720, h=480, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Tag', d)

d = twccommon.Data(depth=70, repeat=0, x=0, y=0, w=720, h=140, sx=1, sy=1, tx=0, ty=0)
dsm.setDefault('Config.1.viewport.Bulletin', d)
