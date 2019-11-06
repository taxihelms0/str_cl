 ______________     ________________    _______________
________________    ________________    ________________
______    ______    ________________    ______    ______
______                   ______         ______    ______
 ______________          ______         _______________
          ______         ______         _______________
______    ______         ______         ______    ______
________________         ______         ______    ______
 ______________          ______         ______    ______

STR V 0.1 - by Alex Ian Smith 2019 - alexiansmith.com

A command line script for altering the time domain of .wav
files.

You can use the following commands at any text prompt:
  - Quit Program: 'x', 'exit', 'q', 'quit'
  - View Readme:  'readme', 'man'

* Disclaimer *
  As STR is software that processes audio, its output can at
  times be extremely loud. At other times it can be extremely
  quiet. Please take care when setting your computer volume
  while Previewing or Playing audio with STR; especially while
  wearing headphones. Speaker and/or hearing damage are
  possible. Please use your own discretion.

Installation:

  STR requires the following packages:
  cffi==1.13.2
  numpy==1.17.3
  pycparser==2.19
  scipy==1.3.1
  sounddevice==0.3.14
  SoundFile==0.10.2

  In your python environment, you can install all these
  dependencies with the following command:
    $ pip install -r requirements.txt

Usage:

    $ python STR.py

  As a command line tool, you will be presented with prompts
  that will allow you to open, playback, set parameters, alter,
  and save .wav files.

  The distribution contains a folder titled '/wavs/' with several
  .wav files to get started. These are listed when you launch
  STR. You can obviously load your own wav files either by
  copying them into this folder, or following the instructions
  to change directories.

Parameters:

  The parameters are loosely named by not only how they affect
  the results, but also as they function within STR's
  algorithms. Each parameter in some way affect the time
  domain and may respond differently depending on the other
  parameters' values. So, they might not always do exactly what
  you expect. Don't read into that too much.

  Having said that. Here's somewhat of an explanation for the
  parameters:
    Factor:
        Factor by which the original is slowed down
    Buffer:
        Loops a section of the file in relation to the
        selected factor
    Offset:
        Amount to offset the buffer on each successive
        loop
    Start:
        Point in the original file to start reading
    End:
        Point in the original file to stop reading
        * STR currently won't work if you make Start
          larger than End. I hope to fix this in a
          future update.
    Max Length:
        The longest your output will be in Minutes
        * Important Note:
          Longer Max Lengths will result in significantly
          longer processing times.For times longer than a
          couple minutes, expect to let STR run for about 20
          seconds to a couple minutes. Really long Max Lengths
          (20 minutes and up) can take 15 - 30+ minutes to
          process. Your computer's fan might turn on. That just
          means it's working hard. You've been warned.

Randomize:

  STR also features a randomize function that will select random
  values for all parameters except Max Length. This gives you a
  bit of control over how long it will take to process the
  results. When you randomize the parameters, STR will print
  the values to the screen so you can remember them for next
  time if you like the results.

Enjoy!
