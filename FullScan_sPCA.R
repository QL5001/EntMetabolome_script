#Sparse principal component analysis (sPCA) of the full-scan LC-MS profiling of the exometabolomes of four groups of samples
#Begin#

library(knitr)
library(mixOmics)
library(dplyr)

ent4 = read.csv(file = file.choose(), sep = ",", header = TRUE, stringsAsFactors = FALSE)  #open file csv file for LC-MS data extracted by MarkerView
X = ent4[, 1:307]    
X_mean = apply(X, 2, mean)
X_center = scale(X, center = X_mean, scale = FALSE)
Y = ent4$Group   #UTI89 and the mutants

spca.ent = spca(X_center, ncomp = 10, center = FALSE, scale = FALSE)

ev = spca.ent$explained_variance   #explained_variance
write.csv(ev, "ent4_SPCA_ExplainedVariance.csv")

sco = spca.ent$variates   #prinicipal component values
write.csv(sco, "ent4__SPCA_PrincipleComponent.csv")

loa = data.frame(spca.ent$loadings$X)   #loading values
peak_name = colnames(X)   #peak names
loa_PC1 = data.frame(peak = peak_name, PC1loa = loa[, 1])   #create a dataframe with peak names, and their loading values associated with PC1
write.csv(loa_PC1, "ent4_SPCA_loa_PC1.csv")
loa_PC2 = data.frame(peak = peak_name, PC2loa = loa[, 2])   #create a dataframe with peak names, and their loading values associated with PC2
#write.csv(loa_PC2, "ent4_SPCA_loa_PC2.csv")

par(mar=c(5,4,4,2)+0.1)
png(filename = "ent4_sPCA_ScorePlot.png", width = 600, height = 400)  #sPCA score plot
plotIndiv(spca.ent, comp = c(1,2), group = ent4$Group, pch = c(15, 16, 17, 18), cex = 4, col = rainbow(4), ellipse = FALSE, ind.names = FALSE, legend = TRUE, size.legend = 15, size.xlabel = 18, size.ylabel = 18, size.axis = 15, title = "ent4_SPCA_ScorePlot")

graphics.off()

#Exported csv files are used for further data analyses and drawing figures in Excel, Prism, and R programming
#End#
