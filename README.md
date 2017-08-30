# ALZoMetrics

## Introduction

This repository is a supplementary of the project ALZoMetrics--a computational approach to investigate key roles in Alzheimer’s Disease(AD).
In this project, our primary goal is to integrate and analyze biological data in order to, firstly, find out the most important components in AD, afterwards, if possible,suggest theraputics for AD, as well.  

## Motivation

More information about our research and our motivation can be found [here](https://docs.google.com/presentation/d/1I902EtO0Hp1yQ8RNlqNbEcGUDQ_bYnb4q6HtiNKlWnY/edit?usp=sharing).

## miRawler

We developed a code in python & R - called miRawler - by which facilitate crawling [mirTarBase](http://mirtarbase.mbc.nctu.edu.tw/) online database. The crawler is programmed to
* find proper GEO data series containing expression profile for target genes and candidate miRNAs.
* fetch expression levels in each data series,
* fetch the calculated correlation matrix for each data series,
* draw the heatmap of correlation matrix, and
* draw linear plot for each dataseries.<br>

The source code of miRawler can be found in miRawler folder.
              
