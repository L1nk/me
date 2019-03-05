#!/usr/bin/env python
import sys
import urllib

outfile = sys.argv[2]
infile = sys.argv[1]

print("Opening {INFILE} for reading...".format(INFILE=infile))
i = open(infile, "r")

print("Opening {OUTFILE} for writing...".format(OUTFILE=outfile))
o = open(outfile, "w")

print("Writing to and replacing contents of {OUTFILE} ...".format(OUTFILE=outfile))
o.write( urllib.quote(i.read().strip()) )

print("Done.")

sys.exit()
