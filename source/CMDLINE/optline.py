#!/usr/bin/python3

import sys
import getopt

shortargs = 'ht:'
longargs = ['help','test=']

cmdPara = {'inputFile':None,'outFile':None,'test':None}

def usage():
    print("Usage:./main.py [OPTIONS] ")
    print("-h\t\t\t\tAsk Message for Help")
    print("--help\t\t\t\tAsk Message for Help")
    print("-a\t\t\t\tTest Options Not use")
    print("--a [args]\t\t\tTest Options Not use")

def initCmdLine():
    opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)

    for opt, val in opts:
        if opt in ('-h', "--help"):
            usage()
            continue
        if opt in ('-t', '--test'):
            cmdPara['test'] = val
            continue


if "__main__" == __name__:
    initCmdLine()

