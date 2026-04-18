#EXTRACTING TOP 5 HITS
from Bio.Blast import NCBIXML
with open("hbb_result.xml") as b:
    blast_record= NCBIXML.read(b)

for i in blast_record.alignments[0:5]:
    print("title:", i.title)
    print("length of sequence:", i.length)
    for a in i.hsps:
        print("E VALUE:", a.expect)
        print("ALIGNMENT SCORE:", a.score)
        print("SUBJECT SEQUENCE:", a.sbjct)
        print("--"*30)