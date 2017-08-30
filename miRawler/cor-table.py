import requests
import re

co = {}
al = {}
mirs = ["hsa-miR-30c-1-3p","hsa-miR-30c-2-3p","hsa-miR-199a-5p","hsa-miR-199b-5p","hsa-miR-200b-3p","hsa-miR-200c-3p","hsa-miR-296-5p","hsa-miR-324-5p","hsa-miR-484","hsa-miR-491-5p","hsa-miR-625-5p","hsa-miR-744-5p"]
gses = ["GSE35602","GSE19783ER+","GSE26953","GSE19536","GSE38974","GSE38226","GSE21687","GSE32688","GSE42095","GSE28260","GSE34608","GSE17498","GSE19783ER-","GSE28544","GSE21032"]

for mir in mirs:
    r = requests.get('http://mirtarbase.mbc.nctu.edu.tw/php/getDrawChartData.php?geneid=PIN1&miRNA='+mir)
    f = open(mir, 'w')
    f.write(r.content)
    f.close()

for mir in mirs:
    f = open(mir, 'r')
    datas = re.sub(r":{[^\{]*\}", "", f.read())
    datas = datas.replace("{","")
    datas = datas.replace("}","")
    datas = datas.replace("::5300","")
    datas = datas.split('","')
    for data in datas:
        row = data.replace('"','').split('::')
        row[0] = row[0].replace('\n','')
        row[0] = row[0].replace(' ','')
        if not co.has_key(row[0]):
            co[row[0]] = {}
        if not co[row[0]].has_key(mir):
            co[row[0]][mir] = {}
        co[row[0]][mir] = row[2]
		
f = open("cor.csv",'w')
f.write('\t'.join(mirs)+'\n')
for gse in gses:
    f.write(gse+'\t')
    for mir in mirs:
        if co[gse].has_key(mir):
            f.write(co[gse][mir]+'\t')
        else:
            f.write('NA\t')
    f.write('\n')
f.close()
