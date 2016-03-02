import json
import os
import math
from os import listdir
from os.path import isfile, join


def initialize(arr):
    for i in range(256):
        arr[i]=0
    return


def read_directory_recur(path, filelist):
    if not os.path.exists(path):
        print(" Specified path {pathname} does not exist!".format(pathname=path))
        sys.exit()
    for f in listdir(path):
        if isfile(join(path, f)):
            # print(join(path,f))
          filelist.append(join(path, f))
        else:
            read_directory_recur(join(path, f), filelist)
    return


def update_correlation(co_relation, number_of_files):
    for i in range(256):
        corelation[i] = (corelation[i]*number_of_files +co_relation[i])/(number_of_files+1)

def read_bytes(filename, fingerprint):
    max=1
    if not os.path.exists(filename):
        print(" File \"{filen}\" could not be found".format(filen=filename))
        print(" Skipping !")
        return
    if (os.path.getsize(filename) == 0):
        print(" Empty file is {fname}".format(fname=filename))
    # Add a try catch to save file reads
    with open(filename, "rb") as input_file:
        try:
            bytes_from_file = input_file.read(8192)
            while bytes_from_file:
                for b in bytes_from_file:
                    # print("read byte: {byte}".format(byte = b))
                    fingerprint[b] += 1
                bytes_from_file = input_file.read(8192)
        finally:
			input_file.close
	#normalize the fingerprint
	for i in range(256)
		if max < fingerprint[i]:
			max = fingerprint[i]
	for i in range(256):
		fingerprint[i] =  fingerprint[i]/max
	return





def compute_bfa(filelist, global_fingerprint):
	for i in range(len(filelist)):
		pointer_fingerprint = {}
		file =  filelist[i]
		read_bytes(file, pointer_fingerprint)
		co_relation = cal_corelation(fp,global_fingerprint)
		if (i == 1):
			corelation = co_relation
		else:
			update_corelation(co_relation,corelation,i)
		update_fingerprint(pointer_fingerprint,global_fingerprint,i+1)
	return global_fingerprint




def testbfa():
    filelist = []
    global_fingerprint = {}
    corelation = {}
    initialize(global_fingerprint)
    read_directory_recur(path,filelist)
    global_fingerprint = compute_bfa(filelist,global_fingerprint, corelation)
    # Dump the fingerprint and Co-relation as a JSON to a file
    print(json.dumps(global_fingerprint,indent=4))
