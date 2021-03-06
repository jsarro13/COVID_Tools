from __future__ import print_function
#!/usr/bin/python
#Generate_Genbank_Submission.py 04-2021
#Written by Joseph Sarro
#This script generates a submission file for Genbank using the genbank submisison template .tsv from the Dragen run and another file contaiing the date of the survailance test.
#Edit 05-2021 change input file from Dragen index to State submission file to filter out bad samples 
import sys
import os
#import the name of the fasta file associated with these sequences
Fasta = sys.argv[1]
fasta = os.path.splitext(Fasta)[0]
#import the State csv file
temp = sys.argv[2]
f = Fasta
ff = open(temp,'r')
#output file to write to
gis= open(fasta+'_source_modifiers.tsv','w')
#print fasta
print("Sequence_ID	country	host	isolate	collection-date	isolation-source",file=gis)
first=True
for lines in ff:
	if first == True:
		first = False
	else:
		fields = lines.split(",")
		ID=fields[0]
		#field = Id.split("/")
		#ID=field[2]
		#Id = "hCoV-19/USA/IN-",ID,"/2021"
		Date=""
		#this file must contain UND ID in first column and date in second
		sur=open('/Users/joe/Covid_seq/Spreadsheets/Saliva_Case_Export_2021-07-0614_17_13.982120.csv','r')
		for linez in sur:
			fieldz = linez.split(",")
			IDZ=fieldz[0]
			#print ID + IDZ
			if ID == IDZ:
				Date=fieldz[1]
				print(ID,'	USA: Indiana, St. Joseph County	Homo sapiens	SARS-CoV-2/human/USA/',ID,'/2021	',Date,'	saliva',file=gis,sep='')
gis.close()
ff.close()
