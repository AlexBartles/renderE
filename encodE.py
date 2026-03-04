import twc.dsmarshal as dsm
import requests as r
import domestic.wxdata as wxdata
import twccommon
import traceback
import sqlite3 as sql
import time

print("encodE by LeWolfYT")
print("LFRecord.db is from MARIENCODER!")
print("Make sure to support it too!")

db = sql.connect("LFRecord.db")

cver = dsm.get("configVersion")
obs = dsm.get(f"Config.{cver}.interestlist.obsStation")
coopid = dsm.get(f"Config.{cver}.interestlist.coopId")
primarycoop = dsm.get(f"primaryCoopId")
textfcstcoop = dsm.get(f"Config.{cver}.Local_TextForecast").coopId

cur = db.cursor()

windmap = {"Calm": 0, "N": 1, "NNE": 2, "NE": 3, "ENE": 4, "E": 5, "ESE": 6, "SE": 7, "SSE": 8, "S": 9, "SSW": 10, "SW": 11, "WSW": 12, "W": 13, "WNW": 14, "NW": 15, "NNW": 16, "Var": 17}

cidmap = {}

for cid in coopid:
    print(f"Searching for coopId {cid}")
    c2 = cur.execute("SELECT * FROM LFRecord WHERE coopId = ?", (cid,))
    res = c2.fetchone()
    if not res:
        print(f"Failure finding coopId {cid}!")
    else:
        print(f"Found coopId {cid}!")
        cidmap[cid] = (res[7], res[8])

for stat in obs:
    print(f"starting obs for {stat}!")
    try:
        dat = r.get(f"https://wx.lewolfyt.cc?icao={stat}").json()
        data = twccommon.Data()
        data.skyCondition = dat["current"]["info"]["narrationCode"]
        data.temp = dat["current"]["conditions"]["temperature"]
        data.humidity = dat["current"]["conditions"]["humidity"]
        data.dewpoint = dat["current"]["conditions"]["dewPoint"]
        data.altimeter = dat["current"]["conditions"]["pressure"]
        data.visibility = dat["current"]["conditions"]["visibility"]
        data.windDirection = windmap[dat["current"]["conditions"]["windCardinal"]]
        data.windSpeed = dat["current"]["conditions"]["windSpeed"]
        data.gusts = dat["current"]["conditions"]["windGusts"]
        data.heatIndex = dat["current"]["conditions"]["heatIndex"]
        data.windChill = dat["current"]["conditions"]["windChill"]
        data.pressureTendency = dat["current"]["conditions"]["pressureTendency"]
        #wxdata.setData(f"obs", stat, data, dat["current"]["info"]["expires"])
        dsm.set(f"obs.{stat}", data, dat["current"]["info"]["expires"])
    except:
        print(traceback.print_exc())
        print(f"obs failure for {stat}")
dsm.ds.commit()

curr_time = time.time()
y, m, d, H, M, S, wd, day, dst = time.localtime(curr_time)

times = []

#taken from TextForecast
if (H < 4):
    # Start with the 7PM yesterday to 7AM today data.
    # The window for the start of this data (7PM) begins yesterday
    # at noon (and extends to midnight).
    # So, we are looking for the UTC of yesterday at noon.
    times.append(time.mktime((y,m,d-1,12,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d,0,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d,12,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d+1,0,0,0,0,0,-1)))
elif (H < 16):
    # Start with the data for 7AM - 7PM today
    # This will be the UTC data of midnight today
    times.append(time.mktime((y,m,d,0,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d,12,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d+1,0,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d+1,12,0,0,0,0,-1)))
else: 
    # Start with the data for 7PM today to 7AM tomorrow
    # This will be the UTC data of noon today.
    times.append(time.mktime((y,m,d,12,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d+1,0,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d+1,12,0,0,0,0,-1)))
    times.append(time.mktime((y,m,d+2,0,0,0,0,0,-1)))
#i'm just gonna... lie!
print(times)
print("starting textfcst!")
try:
    textfcst = r.get(f"https://api.weather.com/v1/geocode/{'/'.join(cidmap[textfcstcoop])}/forecast/daily/10day.json?language=en-US&units=e&apiKey=e1f10a1e78da46f5b10a1e78da96f525").json()["forecasts"]

    done = 0
    ix = 0
    fcsts = []
    expiry = []
    while done < 4:
        if "day" in textfcst[ix]:
            fcsts.append(twccommon.Data(
                daypartName=textfcst[ix]["day"]["daypart_name"],
                audioCode=textfcst[ix]["day"]["vocal_key"],
                phrase=textfcst[ix]["day"]["narrative"]
            ))
            expiry.append(textfcst[ix]["expire_time_gmt"])
            done += 1
            if done == 4:
                break
            fcsts.append(twccommon.Data(
                daypartName=textfcst[ix]["night"]["daypart_name"],
                audioCode=textfcst[ix]["night"]["vocal_key"],
                phrase=textfcst[ix]["night"]["narrative"]
            ))
            expiry.append(textfcst[ix]["expire_time_gmt"])
            done += 1
            if done == 4:
                break
            ix += 1
        else:
            fcsts.append(twccommon.Data(
                daypartName=textfcst[ix]["night"]["daypart_name"],
                audioCode=textfcst[ix]["night"]["vocal_key"],
                phrase=textfcst[ix]["night"]["narrative"]
            ))
            expiry.append(textfcst[ix]["expire_time_gmt"])
            done += 1
            if done == 4:
                break
            ix += 1
    for fcst, tm, ex in zip(fcsts, times, expiry):
        dsm.set(f"textFcst.{textfcstcoop}.{round(tm)}", fcst, ex)
except:
    traceback.print_exc()
    print("TextForecast generation failed!")

dsm.ds.commit()

exit()
for cid in coopid:
    if cid not in cidmap:
        print(f"Skipping coopId {cid}'s data (not found earlier?)")
        continue
    try:
        dat = r.get(f"https://wx.lewolfyt.cc?geo={cidmap[cid]}").json()
        data = twccommon.Data()
        data.skyCondition = dat["current"]["info"]["narrationCode"]
        data.temp = dat["current"]["conditions"]["temperature"]
        data.humidity = dat["current"]["conditions"]["humidity"]
        data.dewpoint = dat["current"]["conditions"]["dewPoint"]
        data.altimeter = dat["current"]["conditions"]["pressure"]
        data.visibility = dat["current"]["conditions"]["visibility"]
        data.windDirection = windmap[dat["current"]["conditions"]["windCardinal"]]
        data.windSpeed = dat["current"]["conditions"]["windSpeed"]
        data.gusts = dat["current"]["conditions"]["windGusts"]
        data.heatIndex = dat["current"]["conditions"]["heatIndex"]
        data.windChill = dat["current"]["conditions"]["windChill"]
        data.pressureTendency = dat["current"]["conditions"]["pressureTendency"]
        #wxdata.setData(f"obs", stat, data, dat["current"]["info"]["expires"])
        dsm.set(f"obs.{stat}", data, dat["current"]["info"]["expires"])
    except:
        print(traceback.print_exc())
        print(f"obs failure for {stat}")