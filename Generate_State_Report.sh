######Generate_State_Report.sh#######
######04-2021 Joseph Sarro###########
#####edited 5-2021 to add date and pangloin version and remove osx created files
######Generate table to submit to state. Three report files are needed from panglolin, GISAID, and Nextclade.
###parse pangolin.csv
awk -F ',' '{print $1","$2}' pangolin.csv > pangolin.tmp.csv
sort pangolin.tmp.csv > pangolin.tmp.sorted.csv
rm pangolin.tmp.csv
###Parse gisaid table

###this file name will change with each run*********
cp ../1620229268386.metadata.tsv metadata.working.tsv
##########******************************************
sed -i -e 's/hCoV-19\/USA\/IN-//g' "metadata.working.tsv"
sed -i -e 's/\/2021//g' "metadata.working.tsv"
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
join -t , state.merge.1.csv nextclade.filt.tmp.sorted.csv >>  state.merge.2.csv
rm state.merge.1.csv
rm nextclade.filt.tmp.sorted.csv
###Parse date files in Gisaid submission
awk -F ',' '{print $6","$27}' 4-27-21_EpiCoV_BulkUpload.csv > date.tmp.csv
sort -t , -k2 date.tmp.csv > date.sorted.csv
rm date.tmp.csv

#########edit date in output file for each run############
echo "Barcode,Lineage,GISAID_ID,Clade,Date,Pangloin_Version" >  4-27-2021_test.state.csv
join -t , -2 2 state.merge.2.csv date.sorted.csv >>  4-27-2021_test.state.csv
rm state.merge.2.csv
rm date.sorted.csv
sed -i -e '2,$s/$/,v2.3.8/g' "4-27-2021_test.state.csv"
#####remove duplicate files due to sed osx extension
rm *-e
#Done!
