import requests
import re

mirs = ["hsa-miR-30c-1-3p","hsa-miR-30c-2-3p","hsa-miR-199a-5p","hsa-miR-199b-5p","hsa-miR-200b-3p","hsa-miR-200c-3p","hsa-miR-296-5p","hsa-miR-324-5p","hsa-miR-484","hsa-miR-491-5p","hsa-miR-625-5p","hsa-miR-744-5p"]
gses = ["GSE35602","GSE19783ER+","GSE26953","GSE19536","GSE38974","GSE38226","GSE21687","GSE32688","GSE42095","GSE28260","GSE34608","GSE17498","GSE19783ER-","GSE28544","GSE21032"]

for mir in mirs:
    r = requests.get('http://mirtarbase.mbc.nctu.edu.tw/php/getDrawChartData.php?geneid=PIN1&miRNA='+mir)
    f = open(mir, 'w')
    f.write(r.content)
    f.close()