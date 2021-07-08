from __future__ import print_function
#!/usr/bin/python
#Generate_GISAID_Submission.py 04-2021
#Written by Joseph Sarro
#This script splits generates a submission file for GISAID using the table genrated from the Dragen run and another file contaiing the date of the survailance test.
import sys
import os
#import the name of the fasta file associated with these sequences
Fasta = sys.argv[1]
fasta = os.path.splitext(Fasta)[0]
#import the Dragen csv file
Dragen = sys.argv[2]
f = Fasta
ff = open(Dragen,'r')
#output file to write to
gis= open(fasta+'_EpiCoV_BulkUpload.csv','w')
#print fasta
#print >> gis, "submitter,fn,covv_virus_name,covv_type,covv_passage,covv_collection_date,covv_location,covv_add_location,covv_host,covv_add_host_info,covv_sampling_strategy,covv_gender,covv_patient_age,covv_patient_status,covv_specimen,covv_outbreak,covv_last_vaccinated,covv_treatment,covv_seq_technology,covv_assembly_method,covv_coverage,covv_orig_lab,covv_orig_lab_addr,covv_provider_sample_id,covv_subm_lab,covv_subm_lab_addr,covv_subm_sample_id,covv_authors,covv_comment,comment_type"
print("submitter,fn,covv_virus_name,covv_type,covv_passage,covv_collection_date,covv_location,covv_add_location,covv_host,covv_add_host_info,covv_sampling_strategy,covv_gender,covv_patient_age,covv_patient_status,covv_specimen,covv_outbreak,covv_last_vaccinated,covv_treatment,covv_seq_technology,covv_assembly_method,covv_coverage,covv_orig_lab,covv_orig_lab_addr,covv_provider_sample_id,covv_subm_lab,covv_subm_lab_addr,covv_subm_sample_id,covv_authors,covv_comment,comment_type",file=gis)
first=True
for lines in ff:
	if first == True:
		first = False
	else:
		fields = lines.split(",")
		ID=fields[0]
		Cov=fields[8]
	#	print ID +" " + Cov
		Date=""
		#this file must contain UND ID in first column and date in second
		sur=open('/Users/joe/Covid_seq/Spreadsheets/Saliva_Case_Export_2021-07-0614_17_13.982120.csv','r')
		for linez in sur:
			fieldz = linez.split(",")
			IDZ=fieldz[0]
			#print ID + IDZ
			if ID == IDZ:
				Date=fieldz[1]
				#print ID + Date
				#print >> gis, 'jsarro,',Fasta,',hCoV-19/USA/',ID,'/2021,betacoronavirus,Original,',Date,',North America/USA/Indiana/St. Joseph County,NA,Human,NA,NA,unknown,unknown,unknown,saliva,NA,NA,NA,Illumina NextSeq,DRAGEN COVID Lineage,',Cov,'x,Notre Dame COVID Response and Testing Laboratory,"University of Notre Dame, B33 McCourtney Hall, Notre Dame, IN 46556",',ID,',Notre Dame Genomics & Bioinformatics Core Facility,"University of Notre Dame, 019 Galvin Life Science Bldg, Notre Dame, IN 46556",',ID,',"Michael Pfrender, Joseph Sarro, Melissa Stephens",,' 
				print('jsarro,',Fasta,',hCoV-19/USA/',ID,'/2021,betacoronavirus,Original,',Date,',North America/USA/Indiana/St. Joseph County,NA,Human,NA,NA,unknown,unknown,unknown,saliva,NA,NA,NA,Illumina NextSeq,DRAGEN COVID Lineage,',Cov,'x,Notre Dame COVID Response and Testing Laboratory,"University of Notre Dame, B33 McCourtney Hall, Notre Dame, IN 46556",',ID,',Notre Dame Genomics & Bioinformatics Core Facility,"University of Notre Dame, 019 Galvin Life Science Bldg, Notre Dame, IN 46556",',ID,',"Michael Pfrender, Joseph Sarro, Melissa Stephens",,',file=gis,sep='')
gis.close()
ff.close()
