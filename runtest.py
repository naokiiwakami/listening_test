#!/usr/bin/env python

#
# runtest.py
# Test Run script.
# Note this program runs only on windows.
# Also note this program does not run from Cygwin.
# Invoke the script directly from Python 3.
# The easiest way to do is to drag and drop the
# test list file to this script.

import string
import winsound
import time
from msvcrt import getch
import sys
import traceback
import errno
import os
import time

def runtest(infile):
    # initialization
    ins = open(infile, "r")
    fileTokens = os.path.basename(infile).split('.')
    if len(fileTokens) == 2:
        outfile = fileTokens[0] + "_result." + fileTokens[1]
    else:
        outfile = infile + ".result"
    outfile_pathname = os.path.dirname(infile) + "\\" + outfile
    try:
        fd = os.open(outfile_pathname, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    except OSError as e:
        if e.errno == errno.EEXIST:
            print("Result file", outfile, "exists.  Rename or remove.")
            return
        else:
            raise
    out = os.fdopen(fd, "w")
    # out = open(outfile, "w")

    full_path = os.path.realpath(infile)
    path = os.path.dirname(full_path)
    os.chdir(path)

    for line in ins:
        line = line.strip()
        data = []
        data = line.split("\t")
        time.sleep(2)
        winsound.PlaySound("start_mark.wav", winsound.SND_FILENAME)
        time.sleep(1)
        winsound.PlaySound(data[0], winsound.SND_FILENAME)
        time.sleep(1)
        winsound.PlaySound(data[1], winsound.SND_FILENAME)
        time.sleep(1)
        winsound.PlaySound("end_mark.wav", winsound.SND_FILENAME)

        answered = False
        while not answered:
            key = ord(getch())
            if key == 224: # special keys (arros, f keys, ins, del, etc.)
                key = ord(getch())
                if key == 75: # left
                    data.append("0")
                    answered = True
                elif key == 77: # right
                    data.append("1")
                    answered = True
                # comment out following if you allow answer "identical"
                # elif key == 80: # down
                #     data.append("x")
                #     answered = true

        out.write(str(data))
        out.write("\n")

    # terminate the test
    ins.close
    out.close
    time.sleep(2)
    winsound.PlaySound("finish_mark.wav", winsound.SND_FILENAME)


def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: runtest.py <pairs_file>")
            print("Result will be written to file <pairs_file>.result\n")
        else:
            start = time.time()
            runtest(sys.argv[1])
            end = time.time()
            elapsed = end - start
            mins = int(elapsed / 60)
            secs = int(elapsed - mins * 60)
            print("elapsed time =", mins, "mins", secs, "secs")
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        traceback.print_exc(file=sys.stdout)

    print("\npress ESC to exit")
    key = 0
    while key != 27: # ESC
        key = ord(getch())

main()

