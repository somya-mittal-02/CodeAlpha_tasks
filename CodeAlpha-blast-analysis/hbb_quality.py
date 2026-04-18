#CHECKING THE QUALITY OF PROTEIN 
from Bio import SeqIO
from collections import Counter
record= SeqIO.read("hbb.fasta", "fasta")
seq= record.seq
length= len(seq)
aa_count= Counter(seq)

print("Sequence ID:", record.id)
print("Sequence Length:", length)
print("Amino Acid Composition:")

for aa, count in aa_count.items():
    print(f"{aa}: {count}")