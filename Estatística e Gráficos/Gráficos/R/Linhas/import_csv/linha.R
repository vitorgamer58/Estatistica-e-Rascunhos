#Gr√°fico de linhas
ipca <- read.csv(file = "IPCA.csv", header = T, sep = ";", dec=",")
x <- 1:67
dataframe <- data.frame(x, ipca)
plot(dataframe, xlab="MÍs (a partir de Jan/2014", ylab="IPCA Mensal", main ="IPCA", type="l")