import folium
import csv 
import os
import sys

x=sys.argv[1]
filename = "trajectories/"+x
  
# initializing the titles and rows list 
fields = []
rows=[] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 


latlon = rows
mapit = folium.Map( location=[ latlon[0][1], latlon[0][2]], zoom_start=5 )
# mapit = folium.Map( [22.1399,77.4126], zoom_start=5 )
for i in range(len(latlon)):
   folium.CircleMarker( location=[ latlon[i][1], latlon[i][2] ],fill=True, fill_color='#43d9de',color='#43d9de', radius=1 ).add_to( mapit )
fn=x+".ejs"
fn=fn.replace(".csv","")
mapit.save("views/maps/"+fn)
# mapit.save("demo.ejs")
