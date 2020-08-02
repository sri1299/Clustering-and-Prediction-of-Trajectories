import csv

fields = []
rows=[] 
r1 = [] 
r2 = []
r3 = []
r4 = []
r5 = []
# reading csv file 
with open('tsne_2d_plot.csv', 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

for i in rows:
    if i[3]=='0':
        r1.append([i[0],i[1],i[2]])
    elif i[3]=='1':
        r2.append([i[0],i[1],i[2]])
    elif i[3]=='2':
        r3.append([i[0],i[1],i[2]])
    elif i[3]=='3':
        r4.append([i[0],i[1],i[2]])
    elif i[3]=='4':
        r5.append([i[0],i[1],i[2]])

newrow=[]

for i in range(max(len(r1),len(r2),len(r3),len(r4),len(r5))):
    tmprow=[]
    if(i<len(r1)):
        tmprow.append(r1[i][0])
        tmprow.append(r1[i][1])
        tmprow.append(r1[i][2])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    if(i<len(r2)):
        tmprow.append(r2[i][0])
        tmprow.append(r2[i][1])
        tmprow.append(r2[i][2])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    if(i<len(r3)):
        tmprow.append(r3[i][0])
        tmprow.append(r3[i][1])
        tmprow.append(r3[i][2])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    if(i<len(r4)):
        tmprow.append(r4[i][0])
        tmprow.append(r4[i][1])
        tmprow.append(r4[i][2])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    if(i<len(r5)):
        tmprow.append(r5[i][0])
        tmprow.append(r5[i][1])
        tmprow.append(r5[i][2])
    else:
        tmprow.append('')
        tmprow.append('')
        tmprow.append('')
    newrow.append(tmprow)

with open('new2d.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["x1", "y1", "f1", "x2", "y2", "f2", "x3", "y3", "f3", "x4", "y4", "f4", "x5", "y5", "f5"])
    for r in newrow: 
        writer.writerow(r)
    
