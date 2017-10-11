#!/usr/bin/python3

import os
import shutil

from debugLog import debugLog
from p7zip  import compress
from CMDLINE import optline
from upload import upload

def main():
    result = setinputandoutdir()
    if (0 != result) and (result < 0):
        debugLog.debuglog("Set Input & Out Dir failed, errNo:%d" %(result))
        exit(1)
    else:
        debugLog.debuglog("Set input/out dir para success")

    compress.compressNormal(optline.cmdPara['inputFile'], optline.cmdPara['outFile'])
    upload.uploadfilenormalTest(optline.cmdPara['outFile'], '/TMP')


def setinputandoutdir():
    #输入本地待备份目录
    inputfilepath = input("Input Local File Path:")
    #判断路径是否存在
    if os.path.exists(inputfilepath):
        print("inputfilepath:%s is valid" %(inputfilepath))
    else:
        print("inputfilepath:%s is invalid, please check it" %(inputfilepath))
        return -1
    #输入输出目录
    outfilepath = input("Out File Path:")
    #判断输出目录是否存在
    if os.path.exists(outfilepath):
        choice = input("do you want to replace:[Y/N]")
        if "Y" != choice:
            return 1
        else:
            shutil.rmtree(outfilepath)
    else:
        print("Ready to create dir:%s" %(outfilepath))

    os.mkdir(outfilepath)
    print ("InputFile:%s, outfilepath:%s" %(inputfilepath, outfilepath))
    optline.cmdPara['inputFile'] = inputfilepath

    if ('/' != outfilepath[len(outfilepath)-1]):
        outfilepath += '/'
    optline.cmdPara['outFile'] = outfilepath + os.path.basename(inputfilepath) + ".7z"
    return 0

if '__main__' == __name__:
    main()
