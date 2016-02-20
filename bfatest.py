import os

def fingerprint(array):
     pnf= 0
     nfs = [0]*256
     nfps = [0]*256
     ofps = [0]*256

     if (pnf == 0):
         for i in range(256)
             nfps[i] = array[i]
             ofps[0]=nfps[0]
             pnf+=1
     else:
         for i in range(256):
             nfps[i]=((ofps[i]*pnf) + array[i])/(pnf+1)
             ofps[i]=nfps[i]
             print(nfps[i])
             pnf+=1

     #for i in range (256):
        # print(nfps[i])


def normalize(arr):
    max=arr[0]
    for i in range(256):
       if arr[i]>max:
           max=arr[i]

    for i in range(256):
        assert max>0
        arr[i]=arr[i]/max

def testbfa():

    for root, dirs, files in os.walk("C:\\Users\\Sue_12\\Desktop\\pdf_test", topdown=False):
        arr = [0]*256
        for name in files:
           with open(os.path.join(root, name), 'rb') as f:
                byte = f.read(1)
                while len(byte) > 0:
                    index = ord(byte)
                    arr[index] += 1
                    byte = f.read(1)
                normalize(arr)
                print(arr)
                fingerprint(arr)

testbfa()