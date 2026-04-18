from Bio.Blast import NCBIXML
with open("hbb_result.xml") as a:
    blast_result= NCBIXML.read(a)

print("Number of similar sequences/alignments:", len(blast_result.alignments))
print("--"*30)
print("SIMILAR SEQUENCES AND DETAIL:")
print("=="*30)
for i in blast_result.alignments:
    print("Title:", i.title)
    print("No. of Nucleotides:", i.length)
    for a in i.hsps:
        print("Number of Amino Acid match:", a.identities, "(INDENTITY)")
        print("E VALUE:", a.expect)
        print("Alignment Score:", a.score)
        print("Subject Range:", a.sbjct_start, "-", a.sbjct_end)
        print("Matched/Subject Sequence:", a.sbjct)
        print("--"*30)
