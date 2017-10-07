#!/usr/bin/python3

import os
from debugLog import debugLog


def main():
    result = setinputandoutdir()
    if 0 != result:
        debugLog.debuglog("Set Input & Out Dir failed, errNo:%d" %(result))
    else:
        debugLog.debuglog("Set input/out dir para success")

def setinputandoutdir():
    inputfilepath = input("Input Local File Path:")

    if os.path.exists(inputfilepath):
        print("inputfilepath:%s is valid" %(inputfilepath))
    else:
        print("inputfilepath:%s is invalid, please check it" %(inputfilepath))
        return 1

    outfilepath = input("Out File Path:")
    if os.path.exists(outfilepath):
        print("outfilepath:%s is exist" %(outfilepath))
        choice = input("do you want to replace:[Y/N]")
        if "Y" != choice:
            return 2
        else:
            os.rmdir(outfilepath)
    else:
        print("Ready to create dir:%s" %(outfilepath))

    os.mkdir(outfilepath)
    print ("InputFile:%s, outfilepath:%s" %(inputfilepath, outfilepath))
    return 0

if '__main__' == __name__:
    main()
