# The Actual Stretch Function used with str.py
# alex ian smith

import time
import numpy as np
import sys


def stretch0(indata, infs, factor, bufsize, offset, start, end,
max):
    # calculate length of indata
    indatalen = len(indata)

    # temp buffers and vars
    temp = []
    negfact = 0
    smoothbuf = int(bufsize/128)
    if smoothbuf < 1 and bufsize == 0:
        smoothbuf = 10
        bufsize = 1

    print("processing...", end='\r')

    # main loop
    try:
        # factor != 0
        if factor == 0:
            factor = 1
        # convert negative factor into positive
        if factor < 0:
            factor = abs(factor)
            negfact = 1     # Negative Factor Flag
        # iterate with loop buffer
        if bufsize > 0:
            for i in range(int(start), int(end)):
                for j in range(int(factor)):
                    for k in range(int(bufsize)):
                        if i + k < int(end):
                            try:
                                # write data from indata to temp
                                temp.append(indata[i + k])
                            except:
                                print(i, k, (i+k))
                                print("stretch:error: can't append?", end='\r')
                            else:
                                # write data from indata to temp
                                temp.append(indata[i])
                            if i + int(offset) < int(end):
                                # apply offset
                                i = i + int(offset)
                        # apply offset
                        if negfact == 1:
                            if i + int(offset) < int(end):
                                i = i + int(offset)
                            else:
                                i = int(offset) - i
                    # apply offset
                    if negfact == 0:
                        if i + int(offset) < int(end):
                            i = i + int(offset)
                        else:
                            i = int(offset) - i
                    # stop iterating if max length reached
                    if len(temp) >= max:
                        i = int(end)
                        k = int(bufsize)
                        j = int(factor)
                        print(f"i {i}. j {j}. k {k} max {max}. int(end) {int(end)}, len(temp {len(temp)})", end='\r')
                        print("reached max!", end='\r')
                        break
                # stop iterating if max length reached
                if len(temp) >= max:
                    i = int(end)
                    k = int(bufsize)
                    j = int(factor)
                    print(f"i {i}. j {j}. k {k} max {max}. int(end) {int(end)}, len(temp {len(temp)})", end='\r')
                    print("reached max!", end='\r')
                    break

        # iterate with no loop buffer
        else:
            for i in range(int(start), int(end)):
                for j in range(int(factor)):
                    # write indata to temp
                    temp.append(indata[i])
                    if i + int(offset) < int(end):
                        # apply offset staying in range of endpoint
                        i = i + int(offset)
                    else:
                        break
                    # apply offset
                if negfact == 0:
                    if i + int(offset) < int(end):
                        i = i + int(offset)
                    else:
                        i = int(offset) - i
                # break when max reached
                if len(temp) >= max:
                    i = int(end)
                    j = int(factor)
                    print("lentemp after max reached", len(temp))
                    print("reached max!")
                    break

        print("stretch: done processing")
    except ValueError:
        print("stretch: couldn't iterate")
        raise ValueError()

    # write to numpy array
    processed = []
    try:
        processed = (np.asarray(temp, dtype="int16"))
    except:
        print("stretch: couldn't write buffer to numpy")
    print(len(processed))
    print(type(processed))
    return (processed, infs)

    # close and del buffers
    try:
        sf.SoundFile(infile).close()
        del temp[:]
        del processed[:]
    except:
        print("couldn't close/del buffers")
