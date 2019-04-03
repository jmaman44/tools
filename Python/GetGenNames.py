import re
import os

#Generates a file with the name of each gene/protein from the fasta file.
#This is made for Fusarium oxysporum 4287 but can be altered for other organisms.
def GetNames(db):
    g = open(db,"r+").read()
    opt = re.findall(r'(?<=>)FOXG_\d{5}',g)
    txt = "\n".join(opt)
    f = open("gnames.txt","w+")
    f.write(txt)
    f.close()

#Opens header file with name of fasta file in the first row.
with open("HeaderFile.txt") as g:
    DB = g.readlines()
GetNames(DB[0].strip())
