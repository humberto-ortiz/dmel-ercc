import cogent.parse.bowtie

data = cogent.parse.bowtie.BowtieOutputParser( "GSM517059_run29_s_1_ERCC_dm3_map.txt" )

count = 0
for row in data:
     print row
     count += 1
     if count > 10:
          break



