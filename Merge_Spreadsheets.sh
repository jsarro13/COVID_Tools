###parse Dragen info
cp Dataexport.csv Dataexport.working.csv
sed -i -e  's/"//g' "Dataexport.working.csv"
sed -i -e  's/(coverage)(amplicons)//g' "Dataexport.working.csv"
sort -t , Dataexport.working.csv > Dataexport.sorted.csv
rm Dataexport.working.csv
###Parse Ct info
join -t , Dataexport.sorted.csv ../RNA_Var_sorted.parsed.csv > merge1.csv
###parse probe info
awk -F ',' '{print $1","$2","$5,","$6","$9","$12,","$13}' probes.csv > probes.parsed.csv
sed -i -e  's/"//g' "probes.csv"
sort -t , probes.parsed.csv > probes.sorted.csv
rm probes.parsed.csv
join -t , merge1.csv probes.sorted.csv > merge2.csv 
rm probes.sorted.csv
rm merge1.csv
###parse read depth
join -t , merge2.csv totalseq.R1.sort.txt > All_fields_merged.csv 
rm merge2.csv
