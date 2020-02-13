today=$(date +"%Y%m%d")
f="msg_missing_slots_links_${today}.txt"
wget ftp://user:pass@eogrid.esrin.esa.int/msgdata_missingslots/$f

while read p; do
   ~/miniconda3/envs/selenium/bin/python /home/rssuser/autoorder_msgdata/order.py "$p"
done <$f

rm -f $f