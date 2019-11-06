# Stretch Version 0.1.0
# Command Line Version
# © Alex Ian Smith 2019

import os
import ntpath
from stretch import stretch0
from scipy.io.wavfile import write
import time
import random
import sounddevice as sd
import soundfile as sf
import sys

def user_cmd(inpt):
    # function that watches inpt field for commands
    # quit == 'q'/'quit'/'x'/'exit'
    # manual == 'man'/'readme'
    inpt = str.lower(inpt)    # ignore case
    if inpt == 'q' or inpt == 'quit' or inpt == 'x' or inpt == 'exit':
        print("bye")
        sys.exit(0)
    elif inpt == 'man' or inpt == 'readme':
        inpt = False
        # open and print readme.md
        readme = open('readme.md', 'r')
        readme_lines = readme.readlines()
        for rline in readme_lines:
            if rline in {'Installation:\n', 'Usage:\n', 'Parameters:\n', 'Randomize\n'}:
                x = input('|| press enter to continue...')
                x = user_cmd(x)
            print(f"|| {rline}", end="")
            time.sleep(0.02)
        readme.close()
        print()
    return inpt


def yesorno_query(param, message):
    # yes or no user input
    while True:
        # automatically appends '[y/n]' to end of message
        query = input(message + ' [y/n]: ')
        query = str.lower(query) # ignore case
        # checks for quit commands
        query = user_cmd(query)
        if query == False:    # don't pass entry when returning from readme
            continue

        # drop 'e' and append 'ing' so 'randomize' becomes 'randomizing' etc.
        if 'random' in param:
            param = 'randomizing'
        if 'save' in param:
            param = 'saving'
        if 'play' in param:
            param = 'playing'
        if 'preview' in param:
            param = 'previewing'

        # check for and process 'y' or 'n' response
        try:
            if query == 'y':
                query = True
                print(param)
                return query
                break
            elif query == 'n':
                query = False
                print("not " + param)
                return query
                break
            else:
                print("please respond with 'y' or 'n'")
        except:
            print("please respond with 'y' or 'n'")


def list_files(dir):
    # open wavs directory and list files
    files = os.listdir(dir)
    print(f"\nlooking for .wavs in {dir}...", end="\n\n")
    wavs = False
    for i in files:
        if '.wav' in i or '.WAV' in i:
            wavs = True
            print(i)
            time.sleep(0.02)
    print()
    if wavs == False:
        print("no .wav files found")


def main():
    dir = './wavs/' # default distribution directory

    # open and print header
    header = open('readme.md', 'r')
    header_lines = header.readlines()
    for i in range(26):
        print(header_lines[i], end="")
        time.sleep(0.02)

    # main application loop
    while True:
        # list files in directory
        list_files(dir)
        # user input to select and load wav file
        while True:
            infile = input("select a file or type 'cd' to change to a different directory: ")
            infile = user_cmd(infile)
            if infile == False:    # don't pass entry when returning from readme
                continue
            if infile == 'cd':
                # user input for new directory path
                while True:
                    dir = input("new directory: ")
                    if dir.endswith('/') == False:
                        dir = dir + '/'
                    dir = user_cmd(dir)
                    if dir == False:    # don't pass entry when returning from readme
                        continue
                    try:
                        list_files(dir)
                        break
                    except:
                        print("couldn't load directory, make sure it's a real path")

            else:
                infile = dir + infile
                print("infile:", infile)
                try:
                    indata, infs = sf.read(infile, dtype='int16')
                    print(f"{infile} loaded to memory")
                    break
                except:
                    print("Not a valid wav file")

        # close infile and header
        sf.SoundFile(infile).close()
        header.close()

        # calculate length of wav file
        indatalen = len(indata)

        # query user to playback wav file
        playquery = yesorno_query('play', 'Would you like to listen to your selected file?')
        if playquery == True:
            sd.play(indata, infs)
            sd.wait()

        # query user to randomize
        randquery = yesorno_query('randomize', 'would you like to select random parameters?')

        if randquery == True:
            # random loop
            while True:
                # randomize params
                factor = int(random.uniform(-99, 99))
                bufsize_in = random.uniform(0.000, 5.000)
                bufsize = int(float(bufsize_in) * float(indatalen)) / 100
                offset = random.uniform(0.000, 1.000)
                startpoint_in = random.uniform(0, 99)
                startpoint = int((startpoint_in * indatalen) / 100)
                endpoint_in = random.uniform(startpoint_in, 99)
                endpoint = int((endpoint_in * indatalen) / 100)

                # print params
                print("factor:", factor)
                print("offset:", offset)
                print("bufsize:", bufsize_in)
                print("startpoint:", startpoint_in)
                print("endpoint:", endpoint_in)
                acceptrand_query = yesorno_query('accept', "Accept Random Params?")
                if acceptrand_query == True:
                    break
                else:
                    print("randomizing again...")
                    time.sleep(0.2)
        else:
            # user input Params
            # Factor
            while True:
                factor = input("factor(whole number between -100 and 100): ")
                factor = user_cmd(factor)
                if factor == False:    # don't pass entry when returning from readme
                    continue
                try:
                    factor = int(factor)
                    if factor <= 100 and factor >= -100:
                        if factor == 0:
                            factor = 1
                        print("Factor accepted")
                        break
                    else:
                        print("Error: not a valid Factor")
                except:
                    print("Error: not a valid Factor")
            # Buffer size
            while True:
                bufsize = input("Loop Buffer Size(number between 0 and 99): ")
                bufsize = user_cmd(bufsize)
                if bufsize == False:    # don't pass entry when returning from readme
                    continue
                try:
                    bufsize = float(bufsize)
                    if bufsize <= 99 and bufsize >=0:
                        print("Loop Buffer accepted")
                        break
                    else:
                        print("Error: not a valid Loop Buffer")
                except:
                    print("Error: not a valid Loop Buffer")
            # Offset
            while True:
                offset = input("offset(number between 0 and 1): ")
                offset = user_cmd(offset)
                if offset == False:    # don't pass entry when returning from readme
                    continue
                try:
                    offset = float(offset)
                    if offset <=1 and bufsize >=0:
                        print("Offset accepted")
                        break
                    else:
                        print("Error: not a valid Offset")
                except:
                    print("Error: not a valid Offset")
            # startpoint
            while True:
                startpoint_in = input("Start(number between 0 and 99): ")
                startpoint_in = user_cmd(startpoint_in)
                if startpoint_in == False:    # don't pass entry when returning from readme
                    continue
                try:
                    startpoint_in = float(startpoint_in)
                    if startpoint_in >= 0 and startpoint_in <= 99:
                        startpoint = int((startpoint_in * indatalen) / 100)
                        print("Startpoint accepted")
                        break
                    else:
                        print("Error: not a valid Startpoint")
                except:
                    print("Error: not a valid Startpoint")
            # Endpoint
            while True:
                endpoint_in = input(f"End(number between {startpoint_in} and 99): ")
                endpoint_in = user_cmd(endpoint_in)
                if endpoint_in == False:    # don't pass entry when returning from readme
                    continue
                try:
                    endpoint_in = float(endpoint_in)
                    if endpoint_in > startpoint_in and endpoint_in <= 99:
                        endpoint = int((endpoint_in * indatalen) / 100)
                        print("Endpoint accepted")
                        break
                    else:
                        print("Error: not a valid Endpoint")
                except:
                    print("Error: not a valid Endpoint")

        # Randomize doesn't affect max size to avoid HUGE output files
        # Max Length User Input
        while True:
            max = input("Maximum length(in minutes): ")
            max = user_cmd(max)
            if max == False:    # don't pass entry when returning from readme
                continue
            try:
                max = float(max)
                if max > 0 and max < 60:
                    pass
                    break
                elif max > 60:
                    print("Maximum Length limited to 60 min or less")
                else:
                    print("Error: Not a valid Maximun Length")
            except:
                print("Error: Not a valid Maximum Length")
            if max >= 3 and max <= 60:
                # Query user to ensure large output
                print("Careful...\nmore than a couple minutes can take extremely long to process")
                maxquery = input(f"are you sure you want to output {max} minutes? (y/n) ")
                maxquery = user_cmd(maxquery)
                if maxquery == False:    # don't pass entry when returning from readme
                    continue
                if len(maxquery) == 1 and 'y' in maxquery:
                    print(f"Maximum Length accepted: {max} seconds")
                    break
                elif len(maxquery) == 1 and 'n' in playquery:
                    pass

        # calculate max into seconds
        try:
            max = infs * 60 * float(max)
            print(f"MAX: {max} seconds")
        except:
            print("stretch: couldn't calculate max")

        # calculate offset
        # try:
        offset = int(offset * 1000)
        # Constrain offset !> bufsize
        if offset > bufsize and bufsize > 0:
            offset = offset % bufsize
        # constrain offset !> endpoint - startpoint
        if offset > abs(endpoint - startpoint):
            offset = offset % abs(endpoint - startpoint)
        # constrain offset !> max
        if offset > max:
            offset = offset % max
        else:
            offset = offset
        # except:
            # print("couldn't calculate offset")

        # call stretch0 function with given parameters
        try:
            write_buffer, infs = stretch0(indata, infs, factor, bufsize, offset, startpoint, endpoint,
            max)
            print("stretched!")
        except:
            print("error: couldn't stretch")
            break

        # check for data written to write_buffer
        try:
            # mono data
            writeval = any(write_buffer)
        except:
            # stereo data
            writeval = any(write_buffer[0])

        # write_buffer contains data
        if writeval == True:
            # query user to preview results
            playquery = yesorno_query("preview", "Would you like to preview the results?")
            if playquery == True:
                sd.play(write_buffer, infs)
                sd.wait()

            # query user to save a new wave file
            savequery = yesorno_query("save", "Would you like to save this to a new wav file?")

            # Save loop
            while True:
                if savequery == True:
                    outfile = input("Save Filename: ")
                    writeFlag = True    # write flag
                    outfile = user_cmd(outfile)
                    if outfile == False:    # don't pass entry when returning from readme
                        continue

                    # ensure outfile ends in '.wav'
                    if len(outfile) > 3 and outfile[len(outfile)-1] == 'v' and outfile[len(outfile)-2] == 'a' and outfile[len(outfile)-3] == 'w' and outfile[len(outfile)-4] == '.':
                        # define output folder for saved wavs
                        outfile = './output/' + outfile

                        # check if filename exists
                        if os.path.isfile(outfile):
                            writeFlag = yesorno_query("save", f"{outfile} exists. Overwrite?")
                        else:
                            writeFlag = True
                        if writeFlag == True:
                            # Write outfile
                            write(outfile, infs, write_buffer)
                            print(f"{outfile} saved")
                            time.sleep(0.5) # little pause for visual effect
                            break
                    else:
                        print(f"error: Filename must end in '.wav'")
                else:
                    break
        else:
            # write_buffer empty, try again
            print("Error: write_buffer is empty")
            print("Try again with different parameters\nrestarting stretch...")
            time.sleep(0.5) # little pause for visual effect
        print("restarting")
        time.sleep(0.5)     # little pause for visual effect

if __name__ == '__main__':
    main()
