ls ../1A0535p262/P0314316/ | awk '{print "python make_hxmt_sub.py HXMT_analysis_2.04_2020.py /home/kongld/Data/HXMT/1A0535p262/1A0535p262/P0314316/"$1"  /home/kongld/Data/HXMT/1A0535p262/work_new/results/"$1" 1A0535p262_"$1}' > run_tmp_1.sh
ls ../1A0535p262/P0304099/ | awk '{print "python make_hxmt_sub.py HXMT_analysis_2.04_2020.py /home/kongld/Data/HXMT/1A0535p262/1A0535p262/P0304099/"$1"  /home/kongld/Data/HXMT/1A0535p262/work_new/results/"$1" 1A0535p262_"$1}' > run_tmp_2.sh
