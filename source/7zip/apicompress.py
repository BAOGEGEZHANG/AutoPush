#!/usr/bin/python3

import os


def compressNormal(filePath):
    OutFile = filePath + '.7z'
    cmdline = '7zr a ' + OutFile + " " + filePath
    os.system(cmdline)


if "__main__" == __name__:
    compressNormal("/tmp/hello")


