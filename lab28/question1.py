#thrl = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
#Print its length, its GC content as a percentage (2 decimal places), its translation with
#and without to stop=True, the number of times ACC occurs, its last codon, and the first
#12 bases of its reverse complement.
import Bio
from Bio.Seq import Seq

thrl= Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
print("length",len(thrl))
#for gc percentage
gc=(thrl.count("G")+thrl.count("c"))/len(thrl)*100
print("GC content:{:.2f}%".format(gc))
#translation with stop=True
print("Translation with stop=True:",thrl.translate(to_stop=True))
#translation without stop=True
print("Translation with stop=True:",thrl.count("ACC"))
#last codon
print("Lastcodon:",thrl[-3:])
#first 12 bases of reverse complement
print("Reverse complement:",thrl.reverse_complement()[:12])