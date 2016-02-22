import sys
import numpy as np

file=sys.argv[1]
##add loop for looping thru files.
##check if file length is smaller thn header or trailer lengths.
##add another loop for  trailer

##fingerprint=[0 for i in range(256)]
fingerprint=[[0]*256 for i in range(4)]
prevfile=0
oldfingrpri=[[0]*256 for j in range(4)]
##forloop for number of files
with open(file,"rb") as f:
    byte=f.read(4)
filelist=[]
for b in byte:
    filerow=[]
    for i in range(256):
        filerow.append(0)
    filerow[ord(b)]=1
    filelist.append(filerow)
print "filelist"
print filelist
for t in filelist:
    t=[item*prevfile for item in t]
fingerprint=((oldfingrpri*prevfile)+filelist)/(prevfile+1)
oldfingrpri=fingerprint
prevfile+=1

##Testing the function
filetotest=sys.argv[2]
with open(filetotest,"rb") as filtotest:
    storebyte=f.read(4)
filepanga=[]
for g in storebyte:
    filerowpanga=[]
    for u in range(256):
        filerowpanga.append(0)
    filerowpanga[ord(u)]=1
    filepanga.append(filerowpanga)









