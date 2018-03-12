rm(list=ls())
getwd()
setwd('~/Desktop/Edwisor/Predictive analysis using R and Python/Basic/data01s2l1/')
df=read.csv('IMDB_data.csv',header = T,fileEncoding="latin1",skip=0)
df=df[-c(2),]
rownames(df)=c(1:3389)

b=table(df$Genre)
b=data.frame(b)

df$imdbRating=as.numeric(df$imdbRating)
df$imdbVotes=as.numeric(df$imdbVotes)
df$Year=as.numeric(df$Year)
df$imdbID=as.numeric(df$imdbID)

df=df[order(df$Genre),]

df$newVar=(df$imdbRating - df$imdbVotes)^2
