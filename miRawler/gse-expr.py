import requests
import re
import json

co = {}
al = {}
mirs = ["hsa-miR-30c-1-3p","hsa-miR-30c-2-3p","hsa-miR-199a-5p","hsa-miR-199b-5p","hsa-miR-200b-3p","hsa-miR-200c-3p","hsa-miR-296-5p","hsa-miR-324-5p","hsa-miR-484","hsa-miR-486-3p","hsa-miR-491-5p","hsa-miR-625-5p","hsa-miR-744-5p","hsa-miR-873-5p","hsa-miR-1185-5p","hsa-miR-1255a","hsa-miR-1255b-5p","hsa-miR-1275","hsa-miR-429"]
gses = ["GSE14794","GSE35602","GSE19783ER+","GSE26953","GSE21849","GSE19536","GSE38974","GSE38226","GSE21687","GSE32688","GSE42095","GSE28260","GSE34608","GSE17306","GSE27834","GSE17498","GSE19783ER-","GSE19350","GSE15076","GSE28544","GSE21032"]


for mir in mirs:
    f = open(mir, 'r')
    tmp = f.read()
    datas = json.loads(tmp)
    for key in datas.keys():
        value = datas[key]
        gse = key.split('::')[0].replace(' ','').replace('\n','')
        if not co.has_key(gse):
            co[gse] = {}
            al[gse] = []
        if not 'PIN1' in al[gse]:
            al[gse].append('PIN1')    
        al[gse].append(mir)
        for kv in value.keys(): 
            if not co[gse].has_key(kv):
                co[gse][kv] = {}
            co[gse][kv][mir] = value[kv][0]
            if not co[gse][kv].has_key('PIN1'):
                co[gse][kv]['PIN1'] = value[kv][1]

for gse in gses:
    data = co[gse]
    f = open("exp"+gse+".csv",'w')
    f.write('\t'.join(al[gse])+'\n')
    keys = data.keys()
    keys.sort()
    for key in keys:
        exp = data[key]
        for mir in al[gse]:
            if exp.has_key(mir):
                f.write(str(exp[mir])+'\t')
            else:
                f.write('NA\t')    
        f.write('\n')
    f.close()
