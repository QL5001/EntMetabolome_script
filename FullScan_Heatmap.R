#Draw the heatmap containing the iron-responsive enterobactin-associted sub-exometabolome identified by sPCA loading analysis for the five group of samples
#Begin#

library(RColorBrewer)
library(knitr)
library(mixOmics)
library(dplyr)
library(gplots)
library(pheatmap)
library(viridis)

ent4HM = read.csv(file = file.choose(), sep = ",", header = TRUE, stringsAsFactors = FALSE)  #Open the csv file containing the iron-responsive enterobactin-associted sub-exometabolome identified by sPCA loading analysis for the five group of samples
data_1 = as.matrix(ent4HM[1:10, 1:23])

par(mar=c(2,7,4,2)+0.1)
png(filename = "FullScan_Heatmpa.png", width = 1100, height = 500)
heatmap.2(data_1, Colv = NA, Rowv = NA, scale = "none",  cexCol = 1.5, cexRow = 1.5, col = magma(100, direction = -1), colsep = 0:ncol(data_1), rowsep = 0:nrow(data_1),  sepwidth=c(0.000005, 0.000005), sepcolor='grey', trace = "none", key = TRUE, keysize = 1.0, density.info = "none",  srtCol=90)
graphics.off()

#End#
