import folium
import csv 
import os
import sys

x=sys.argv[1]
filename1= "predictedtrajectories/train/"+x
filename2= "predictedtrajectories/predict/"+x
filename3= "predictedtrajectories/test/"+x
  
# initializing the titles and rows list 
fields = []
rows = [] 
rows1 = [] 
rows2 = []
  
# reading csv file 
with open(filename1, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

with open(filename2, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows1.append(row) 

with open(filename3, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows2.append(row) 

latlon = rows
latlon1 = rows1
latlon2 = rows2
mapit = folium.Map( location=[latlon1[0][1],latlon1[0][2]], zoom_start=8 )
# mapit = folium.Map( [22.1399,77.4126], zoom_start=5 )
for i in range(max(len(latlon),len(latlon1),len(latlon2))):
    if i<len(latlon):
        folium.CircleMarker( location=[ latlon[i][1], latlon[i][2] ],fill=True, fill_color='#0000ff',color='#0000ff',radius=1 ).add_to( mapit )
    if i<len(latlon1):
        folium.CircleMarker( location=[ latlon1[i][1], latlon1[i][2] ],fill=True, fill_color='#ff0000',color='#ff0000', radius=1 ).add_to( mapit )
    if i<len(latlon2):
        folium.CircleMarker( location=[ latlon2[i][1], latlon2[i][2] ],fill=True, fill_color='#00ff00',color='#00ff00', radius=1 ).add_to( mapit )    
fn=x+".ejs"
fn=fn.replace(".csv","")
mapit.save("views/predictedmaps/"+fn)
# mapit.save("demo.ejs")
