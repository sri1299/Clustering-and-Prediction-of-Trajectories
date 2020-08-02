import os
import pandas as pd
import numpy as np

basedir = os.getcwd()+"/"
filedir = basedir+"data/"

files = os.listdir(filedir)

file.open('label.txt')

x = []
for f in files:
   if f.endswith('.tsv'):
        try:
            x = pd.read_csv(filedir+f,sep='\t')
            print("iterating thorough file .."+f+"..."),
		os.system("rm "+filedir+f)
        except pd.errors.EmptyDataError: 
            pass
#print(files[4])
#x = pd.read_csv(filedir+files[4],sep='\t')
#print(np.max(x.altitude_meters))

