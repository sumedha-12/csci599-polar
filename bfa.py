import os

# def fingerprint(array):
#     if (pnf == 0):
#         nfps = nfs
#
#     else
#         for i in range(0,255):
#           nfps[i]=((ofps[i]*pnf) + array[i])/(pnf+1)
#
#     ofps=nfps
#     pnf+=1

def testbfa():

    for root, dirs, files in os.walk("C:\\Users\\Sue_12\\Desktop\\", topdown=False):
        arr = [0]*256
        for name in files:
            # print(o)
            print "sumedha3"    
            with open(os.path.join(root, name), 'rb') as f:
                print("sumedha2")
                byte = f.read(1)
                while len(byte) > 0:
                    index = ord(byte)
                    arr[index] += 1
                    byte = f.read(1)
                    print("sumedha1")
        max=arr[0]
        for i in range(0,255):
            if arr[i]>max:
                max=arr[i]

        for i in range(0,255):
            arr[i]=arr[i]/max
        
        print("sumedha")    
        print(arr)

    testbfa()