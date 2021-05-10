######Generate_State_Report.sh#######
######04-2021 Joseph Sarro###########
######Generate table to submit to state. Three report files are needed from panglolin, GISAID, and Nextclade.
###parse pangolin.csv
awk -F ',' '{print $1","$2}' pangolin.csv > pangolin.tmp.csv
sort pangolin.tmp.csv > pangolin.tmp.sorted.csv
rm pangolin.tmp.csv
###Parse gisaid table

###this file name will change with each run*********
cp ../1620229268386.metadata.tsv metadata.working.tsv
##########******************************************
sed -i -e  's/hCoV-19\/USA\/IN-//g' "metadata.working.tsv"
sed -i -e  's/\/2021//g' "metadata.working.tsv"
awk -F '\t' '{print $1","$3}' metadata.working.tsv > metadata.tmp.csv
sort metadata.tmp.csv > metadata.tmp.sorted.csv
rm metadata.working.tsv
rm metadata.tmp.csv
join -t , pangolin.tmp.sorted.csv metadata.tmp.sorted.csv > state.merge.1.csv 
rm pangolin.tmp.sorted.csv 
rm metadata.tmp.sorted.csv
###parse nextclad table
awk -F ',' '{print $1","$2}' nextclade.filt.csv > nextclade.filt.tmp.csv
sort nextclade.filt.tmp.csv > nextclade.filt.tmp.sorted.csv
rm nextclade.filt.tmp.csv

#########edit date in output file for each run############
echo "Barcode,Lineage,GISAID_ID,Clade" >  4-14-2021_resub.state.csv
join -t , state.merge.1.csv nextclade.filt.tmp.sorted.csv >>  4-14-2021_resub.state.csv  
rm state.merge.1.csv
rm nextclade.filt.tmp.sorted.csv
#Done!
