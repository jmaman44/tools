#!/bin/bash

#Load blast and prepare dataset
module load blast/2.7.1+
makeblastdb -in Fusarium_oxysporum.FO2.pep.all.fa  -dbtype prot
#For each file in a folder runs protein blast to the desired dataset
#The number after 'filename:' is the length of the path up to the filename
for filename in DSUp/outdir/*.txt; do
	blastp -query $filename -db Fusarium_oxysporum.FO2.pep.all.fa  -out DSUp/Results/${filename:16}
done