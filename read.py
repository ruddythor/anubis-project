import time
import os
import json
def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, 2)
    
    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(0.1)
            continue

        yield line


class LogLine:

    now = ""
    message = 0
    aircraft = []


class aircraftt:
    def __init__(self, lat="", lon=""):
        self.lat = lat
        self.lon = lon
    lat = ""
    lon = ""
    hexi = ""
    typ = ""
    flight = ""
    alt = ""

def readfile(filename=""):
    with open("/run/readsb/aircraft.json") as myjsonfile:
        data = json.load(myjsonfile)
    for aircraft in data['aircraft']:
        print("\n======\n")
        print(aircraft)
        if 'lat' in aircraft.keys() and 'lon' in aircraft.keys():
            craft = aircraftt(lat=aircraft['lat'], lon=aircraft['lon'])
            print(vars(craft).items())



if __name__ == '__main__':
    readfile("")
    time.sleep(1)
    readfile("")
    while True:
        readfile("")
        time.sleep(1)


#{"hex":"a01bbc","type":"adsb_icao","flight":"RPA4643 ","alt_baro":9100,"alt_geom":9300,"gs":331.0,"track":90.87,"baro_rate":-64,"squawk":"3617","emergency":"none","category":"A3","nav_qnh":1009.6,"nav_altitude_mcp":9024,"nav_modes":["autopilot","vnav","tcas"],"lat":39.018317,"lon":-76.993042,"nic":8,"rc":186,"seen_pos":24.885,"r_dst":6.439,"r_dir":134.4,"version":0,"nic_baro":1,"nac_p":8,"nac_v":2,"sil":2,"sil_type":"unknown","alert":0,"spi":0,"mlat":[],"tisb":[],"messages":147,"seen":2.4,"rssi":-5.0},

#{"hex":"a94b0a","type":"mode_s","alt_baro":9275,"alert":0,"spi":0,"mlat":[],"tisb":[],"messages":16,"seen":0.3,"rssi":-7.8},

#{"hex":"a2313f","type":"mode_s","alt_baro":32025,"alt_geom":32975,"version":0,"nac_p":8,"sil":2,"sil_type":"unknown","alert":0,"spi":0,"mlat":[],"tisb":[],"messages":99,"seen":3.5,"rssi":-3.5},

#{"hex":"a349be","type":"mode_s","alt_baro":36000,"mlat":[],"tisb":[],"messages":10,"seen":35.7,"rssi":-8.9},

#{"hex":"aa6d3f","type":"mode_s","flight":"FDX1630 ","alt_baro":22275,"alt_geom":22975,"gs":420.1,"track":253.12,"baro_rate":1408,"category":"A4","lastPosition":{"lat":39.179901,"lon":-77.318732,"nic":8,"rc":186,"seen_pos":105.555},"nac_v":1,"sil_type":"perhour","alert":0,"spi":0,"mlat":[],"tisb":[],"messages":571,"seen":4.4,"rssi":-7.6},

#{"hex":"a01097","type":"mode_s","alt_baro":10650,"sil_type":"unknown","mlat":[],"tisb":[],"messages":23,"seen":31.7,"rssi":-8.8},

#{"hex":"a1ff90","type":"mode_s","alt_baro":34000,"mlat":[],"tisb":[],"messages":12,"seen":49.2,"rssi":-7.2},

#{"hex":"a50cb7","type":"mode_s","alt_baro":32000,"version":0,"nac_p":8,"sil":2,"sil_type":"unknown","alert":0,"spi":0,"mlat":[],"tisb":[],"messages":26,"seen":0.4,"rssi":-8.0},

#{"hex":"aa55c0","type":"mode_s","alt_baro":11175,"alt_geom":11375,"gs":291.0,"track":270.79,"baro_rate":1216,"nav_qnh":1008.8,"nav_altitude_mcp":16992,"nav_heading":284.77,"version":0,"nic_baro":1,"nac_p":7,"nac_v":1,"sil":2,"sil_type":"unknown","alert":0,"spi":0,"mlat":[],"tisb":[],"messages":39,"seen":3.6,"rssi":-3.8}
