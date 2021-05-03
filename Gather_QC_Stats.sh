for i in *_fastqc.zip
do
echo "Unziping $i"
unzip $i
done
echo "Unzip complete"
echo "Getting sequence info for"
grep  "Total Sequences" */fastqc_data.txt >> totalseq.txt
grep "Overrepresented sequences" */summary.txt >> overrepseq.txt
echo "Sequence info complete"
#base=$(basename ${i} .zip)
#echo "zipping $base"
#*zip $base
echo "Cleaning up..."
rm -r *_fastqc
sed -i -e  's/\/fastqc_data.txt:/\t/g' "totalseq.txt"
sed -i -e  's/\/summary.txt:/\t/g' "overrepseq.txt"
sed -i -e  's/Total Sequences\t//g' "totalseq.txt"
sed -i -e  's/Overrepresented sequences.*//g' "overrepseq.txt"
sort totalseq.txt>totalseq.sort.txt
sort overrepseq.txt >overrepseq.sort.txt
join -t \t totalseq.sort.txt overrepseq.sort.txt > Stats.txt
sed -i -e  's/\dtqc//g' "Stats.txt"
#rm overrepseq*
#rm totalseq*
echo "Done!"
