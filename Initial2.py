import sys
import numpy as np

file=sys.argv[1]
##add loop for looping thru files.
##check if file length is smaller thn header or trailer lengths.
##add another loop for  trailer

##fingerprint=[0 for i in range(256)]
fingerprint=[[0]*256 for i in range(4)]
fingerprintnum=np.array(fingerprint)
prevfile=0.0
oldfingrpri=[[0]*256 for j in range(4)]
oldfinnum=np.array(oldfingrpri)
print "oldfinnum"
print oldfinnum
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
filenum=np.array(filelist)
print "filenum"
##filenum=filenum*3
##print filenum[3]
fingerprintnum=((oldfinnum*prevfile)+filenum)/float(prevfile+1)
oldfinnum=fingerprintnum
prevfile+=1
print "fingerprintnum"
##print fingerprintnum[0]
##print fingerprintnum[1]
##print fingerprintnum[2]
##print fingerprintnum[3]

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
filepanganum=np.array(filepanga)
score=0.0
denom=0.0
i=0
for h in storebyte:
    score+=fingerprintnum[i][ord(h)]
    denom+=filepanganum[i][ord(h)]
    i+=1
score=float(score)/float(denom)










