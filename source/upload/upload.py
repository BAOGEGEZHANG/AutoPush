#!/usr/bin/python3

import os
import string

testFlag = False

def makecmdline(*tuplepara):
    cmdline = ''
    for para in tuplepara:
        cmdline += ' ' + str(para)
    return cmdline

def execcmdline(cmdline):
    if testFlag == False:
        os.system(cmdline)
    else:
        print(cmdline)


def autologin(username, passwold):
    cmdline = makecmdline('baidupcs','--username',username, '--passwold=', passwold)
    execcmdline(cmdline)


def uploadfilenormal(inpath, outpath):
    cmdline = makecmdline('baidupcs','upload', inpath, outpath)
    os.system(cmdline)

def uploadfilenormalTest(inpath, outpath):
    testFlag = True
    uploadfilenormal(inpath, outpath)


if "__main__" == __name__:
    uploadfilenormal('/tmp/hello.7z', '/TMP')