#ipython RXTE_analysis.py $ldkong/RXTE/GRO_J1655-40/90019-02-01-00 $ldkong/work/GRO_J1655-40/result3/90019-02-01-00 pca
import os
import sys
proname=sys.argv[1]#RXTE_analysis.py
indir=sys.argv[2]#$ldkong/RXTE/GRO_J1655-40
outdir=sys.argv[3]#/sharefs/hbkg/data/tmp/kongld/MAXIJ1535_571/results/P0114535020
name=sys.argv[4]#hxmt_sub

src_ra='84.7274'#J2000 RA
src_dec='26.3158'#J2000 DEC
dt=0.001
stem='1A0535p262'

dirlis=os.listdir('%s' %(indir))
Long=len(dirlis)

i=0
n=0
while i < Long:
    f1=dirlis[i]
    if "P" in f1:
        f=open('%s_%s' %(name,n),'w+')
        print('python %s %s/%s %s/%s -clean -stem %s -bary -src_ra %s -src_dec %s -HElcBin %s -MElcBin %s -LElcBin %s' %(proname,indir,f1,outdir,f1,stem,src_ra,src_dec,dt,dt,dt), file=f)
        f.close()
        n+=1
        i+=1
    else:
        i+=1
print("finish %s" %(indir))
