import re
import os

#Generates fasta file of each gene/protein
def GetFasta(db,name,outdir):
    g = open(db,"r+")
    opt = re.findall(">" + name + r"[^>]+(?=>)",g.read(),re.MULTILINE)
    f = open(outdir+"/"+name+".fasta","w+")
    f.write(opt[0])
    f.close()
    g.close()

#Opens header file
with open("HeaderFile.txt") as g:
    DB = g.readlines()
#Opens file with gene names
with open("GeneNames.txt") as f:
    NameArr = f.readlines()
#Header file contains database/genome file name on the first line
#and output directery on the second line
for name in NameArr:
    GetFasta(DB[0].strip(),name.strip(),DB[1].strip())
