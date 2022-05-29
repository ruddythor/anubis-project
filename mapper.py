import matplotlib.pyplot as plt
# import osmium
# from pyrosm import OSM
# from pyrosm import get_data
import geopandas
from cartopy import crs as ccrs
from cartopy.io.img_tiles import OSM
import urllib.request
import json
from matplotlib import animation
import PySimpleGUI as sg
from datetime import datetime



# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
# path = geopandas.datasets.get_path('naturalearth_lowres')
# df = geopandas.read_file(path)
# # Add a column we'll use later
# df['gdp_pp'] = df['gdp_md_est'] / df['pop_est']

#python C:\Users\slosh\Documents\liveplotter\mapper.py
print("hello world")
#df.plot()
# newdf = geopandas.read_file("D:\\north-america-latest.osm.pbf")
# fp = OSM('north-america-latest.osm.pbf')
# print(fp)
# custom_filter = {"shop":True, "amenity":["bar", "cafe", "fast_food", "ice_cream", "pub", "cinema"]}
# help(fp)
# print(fp.tile_bbox(10000, 10000, 100))
# pois = fp.get_boundaries(boundary_type="administrative")
# fp = get_data('north-america-latest.osm.pbf')
# print(fp)



# fig, ax = plt.subplots()
ax=plt.axes(projection=ccrs.PlateCarree())
ax.set_ylim(40.6051,40.6825)
ax.set_xlim(-73.8288,-73.7258)

# #ADD OSM BASEMAP
osm_tiles=OSM()
ax.add_image(osm_tiles,13) #Zoom Level 13
# #PLOT JFK INTL AIRPORT
# ax.text(-73.778889,40.639722,'JFK Intl',horizontalalignment='right',size='large')
ax.plot([-73.778889],[40.639722],'bo')

# #PLOT TRACK
track, = ax.plot([], [],'ro')

# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]

# #UPDATE FUNCTION
# def update(self):
#     #SEND QUERY
#     fp=opener.open('http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=40.639722&lng=-73.778889&fDstL=0&fDstU=20')
#     mybyte=fp.read()
#     mystr=mybyte.decode("utf8")
#     js_str=json.loads(mystr)
#     fp.close()
#     lat_list=[]
#     long_list=[]
#     op_list=[] #OPERATOR LIST
    
#     for num,flight_data in enumerate(js_str['acList']):
#         lat=flight_data['Lat']
#         lon=flight_data['Long']
#         lat_list.append(lat)
#         long_list.append(lon)
#         op_list.append(flight_data['Op']) #STORE OPERATOR DATA INTO LIST
        
#     track.set_data(long_list,lat_list)
    
#     # LABELING
    
#     #REMOVE LABEL
#     for num, annot in enumerate(anotation_list):
#         annot.remove()
#     anotation_list[:]=[]
    
#     #CREATE LABEL CONTAINER
#     for num,annot in enumerate(js_str['acList']):
#         annotation=ax.annotate('text',xy=(0,0),size='smaller')
#         anotation_list.append(annotation)
    
#     # UPDATE LABEL POSITION AND OPERATOR
#     for num,ano in enumerate(anotation_list):
#         ano.set_position((long_list[num],lat_list[num]))
#         ano.xy = (long_list[num],lat_list[num])
#         txt_op=str(op_list[num])
#         ano.set_text(txt_op)
        
#     return track,ano,
                         
# #UPDATING EVERY SECOND
# anim = animation.FuncAnimation(fig, update,interval=1000, blit=False)

plt.show()