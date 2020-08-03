import csv
import os
import sys

x=sys.argv[1]
filename1= "predictedtrajectories/train/"+x
filename2= "predictedtrajectories/predict/"+x
filename3= "predictedtrajectories/test/"+x

fields = []
rows=[] 
rows1=[]
rows2=[]
  
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

newrow=[]

for i in range(max(len(rows),len(rows1),len(rows2))):
    tmprow=[]
    if(i<len(rows)):
        tmprow.append(rows[i][1])
        tmprow.append(rows[i][2])
        tmprow.append(rows[i][3])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    if(i<len(rows1)):
        tmprow.append(rows1[i][1])
        tmprow.append(rows1[i][2])
        tmprow.append(rows1[i][3])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    if(i<len(rows2)):
        tmprow.append(rows2[i][1])
        tmprow.append(rows2[i][2])
        tmprow.append(rows2[i][3])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    newrow.append(tmprow)

with open("predictedtrajectories/"+x, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["lat", "lon", "alt", "latp", "lonp", "altp", "latt", "lont", "altt"])
    for r in newrow: 
        writer.writerow(r)