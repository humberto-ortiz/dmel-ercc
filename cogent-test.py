import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mapfile", help="filename of mapfile")
args = parser.parse_args()

import cogent.parse.bowtie

data = cogent.parse.bowtie.BowtieOutputParser( args.mapfile )

count = 0
for row in data:
     print row
     count += 1
     if count > 20:
          break



