#SEQUENCE FLITERATION AND IDENTIFICATION
from Bio import SeqIO
valid_aa= set("ACDEFGHIKLMNPQRSTVWY")

record= SeqIO.read("hbb.fasta", "fasta")
seq= str(record.seq)

if len(seq)<50:
    print("Sequence too short for analysis")
    exit()

invalid= [aa for aa in seq if aa not in valid_aa and aa!= "X"]
if invalid:
    print("Invalid amino acids found:", set(invalid))
    exit()

x_count= seq.count("X")
x_percent= (x_count/len(seq))*100

if x_percent>10:
    print("too many unknown amino acids (X):", x_percent, "%")
    exit()

print("Sequence is valid for Downstream analysis")
print("Length:", len(seq))
print("Unknown AA%:", x_percent)