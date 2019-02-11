#!/usr/bin/env Rscript
#install.packages("RColorBrewer")
#library("RColorBrewer")

args <- commandArgs(TRUE)
fname <- args[1]
colIndexName <- args[2]

t<-read.table(fname, sep='\t', header=TRUE)

rownames(t) <- t[, colIndexName]
t <- t[, !(names(t) %in% c(colIndexName))]
m <-  data.matrix(t)

#m <- log(m)
#data=as.matrix(mtcars)

#head(m)
hm <- heatmap(m, Rowv=NA, Colv=NA, col=colorRampPalette(c("red", "yellow", "green"))(n = 50), scale="column")
