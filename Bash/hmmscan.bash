#!/bin/bash

#load hmmer
module load hmmer/3.1b2
#For each file in a folder runs protein blast to the desired dataset
#The number after 'filename:' is the length of the path up to the filename
for filename in /project/uma_lijun_ma/JM_TF/Hmmscan/outdir/*.txt; do
	/share/pkg/hmmer/3.1b2/bin/hmmscan --tblout /project/uma_lijun_ma/JM_TF/Hmmscan/Results/${filename:43} /project/uma_lijun_ma/JM_TF/Pfam-A.hmm $filename
done