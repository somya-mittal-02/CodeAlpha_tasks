#SEARCHING FOR SIMILAR SEQUENCES FROM NCBI 
from Bio import SeqIO
from Bio.Blast import NCBIWWW
Record= SeqIO.read("hbb.fasta", "fasta")
Result= NCBIWWW.qblast(
    program= "blastp",
    database= "nr",
    sequence= Record.seq
)
with open("hbb_result.xml", "w") as b:
    b.write(Result.read())

print("BLAST SUCCESSFUL")