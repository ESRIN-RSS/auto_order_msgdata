today=$(date +"%Y%m%d")
f="order_list_${today}.txt"
g="_order_list_${today}.txt"
~/miniconda3/envs/selenium/bin/python /home/rssuser/autoorder_msgdata/get_order_list.py > $g
diff /home/rssuser/autoorder_msgdata/order_list $g | grep -E ">" | tr -d "> " > $f
cat $f >> /home/rssuser/autoorder_msgdata/order_list
curl -T $f ftp://user:pass@eogrid.esrin.esa.int/msgdata_missingslots/
rm -f $f $g