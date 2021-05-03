#!/usr/bin/python
#SplitFasta 04-2021
#Written by Joseph Sarro
#This script splits a multifasta file to filter out seqeucnes that have been flagged as bad. Two arguments are needed 1) a fasta file 2) a comma seperated list of seqeunces to ommit
import sys
import os
#import fasa and genrate list of names
Fasta = sys.argv[1]
#print Fasta
seqs = sys.argv[2]
Seqs=seqs.split(",")
#print Seqs
#sc=Seqs.count('1')
#print sc
fasta = os.path.splitext(Fasta)[0]
f = open(Fasta, 'r')
ff = open(fasta+'.final.fa','w')
df= open(fasta+'.failed.fa','w')
firstline=True
keep=True
for lines in f:
	if firstline==True:
		firstline=False
		if ">" in lines:
			#print lines
			#hit = [ele for ele in Seqs if(ele in lines)]
			hit = any(ele in lines for ele in Seqs )
			#print hit
			if hit == True:
				#print str(bool(hit))
				keep = False
				print >> df, lines.rstrip("\n")
			else:
			#	print str(bool(hit))
				keep=True
				print >> ff, lines.rstrip("\n")
		else:
			print "Fasta file must be in correct format"
	else:
		if ">" in lines:
                        #print lines
                        #hit = [ele for ele in Seqs if(ele in lines)]
                        hit = any(ele in lines for ele in Seqs )
			#print hit
                        if hit == True:
                                #print str(bool(hit))
                                keep = False
                                print >> df, lines.rstrip("\n")
                        else:
                        #       print str(bool(hit))
                                keep=True
                                print >> ff, lines.rstrip("\n")
		elif keep == True:
			print >> ff, lines.rstrip("\n")
		else:
			print >> df, lines.rstrip("\n")
f.close()
df.close()
ff.close()
