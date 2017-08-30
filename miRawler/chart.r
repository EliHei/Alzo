library(Biobase)
library(GEOquery)
library(limma)
library(plyr)
library(reshape2)
library(DESeq2)
library(ggplot2)
library(data.table)
library(reshape2)
library(ggplot2)
library(pheatmap)

setwd("E:/edu/term 2/advnc bio/report/python/")

data = read.table("expGSE14794.csv",as.is = TRUE)
colnames(data) = data[1,]
data = data[-1,]
data$sample = 1:nrow(data)

mirs = c("sample","PIN1","hsa-miR-199a-5p","hsa-miR-199b-5p","hsa-miR-200b-3p","hsa-miR-200c-3p","hsa-miR-296-5p","hsa-miR-429","hsa-miR-30c-1-3p","hsa-miR-30c-2-3p","hsa-miR-484")
cc = intersect(mirs,colnames(data))
m = melt(data[,cc],'sample',value.name='expr',variable.name='miRNA')
m[,3] = as.numeric(m[,3])
ggplot(m,aes(y = expr, x = sample, colour = miRNA),size=1.5) + geom_line()
