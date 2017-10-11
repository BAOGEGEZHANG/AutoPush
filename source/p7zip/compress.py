#!/usr/bin/python3

import os

from upload import upload


def compressNormal(filePath, outFilePath):
    cmdline = upload.makecmdline('7zr','a',outFilePath, filePath)
    os.system(cmdline)

def compressTest(inputFile, outFile):
    print("compressTest input:%s out:%s" %(inputFile, outFile))


if "__main__" == __name__:
    compressNormal("/tmp/hello", "/tmp/hello.7z")


