import pysam
samfile = pysam.Samfile( "test.sam", "r" )

for alignedread in samfile.fetch('2L', 100, 120):
     print alignedread

samfile.close()
