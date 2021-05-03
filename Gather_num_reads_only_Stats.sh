#Created by Joe Sarro 04-2021
#pulls info from fastqc report and prints number of reads in a csv file
for i in *R1*_fastqc.zip
do
echo "Unziping $i"
unzip $i
done
echo "Unzip complete"
echo "Getting sequence info for"
grep  "Total Sequences" */fastqc_data.txt >> totalseq.R1.txt
echo "Sequence info complete"
#base=$(basename ${i} .zip)
#echo "zipping $base"
#*zip $base
echo "Cleaning up..."
rm -r *_fastqc
sed -i -e  's/\/fastqc_data.txt:/\t/g' "totalseq.R1.txt"
sed -i -e  's/Total Sequences\t//g' "totalseq.R1.txt"
sed -i -e 's/_S[0-9]\+_R[0-9]_001_fastqc//g' "totalseq.R1.txt"
sort totalseq.R1.txt>totalseq.R1.sort.txt
rm totalseq.R1.txt
sed -i -e 's/\t/,/g' "totalseq.R1.sort.txt"
echo "Done!"
