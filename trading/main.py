import os
import csv
import json
from os import write

with open("data.txt","r") as f:
    reader=csv.reader(f)
    data=[]
    for row in reader:
        data.append({'BANKNIFTY':row[0],'DATE':row[1],'TIME':row[2],'OPEN':row[3],'HIGH':row[4],'LOW':row[5],'CLOSE':row[6],'VOLUME':row[7],})
    print (data)

with open("newdata.json","w") as f:
    json.dump(data,f,indent=4)