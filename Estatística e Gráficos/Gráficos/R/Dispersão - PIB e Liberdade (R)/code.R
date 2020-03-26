#Correlação entre liberdade econômica e PIB per Capita
#Dados do World Bank e Heritage Found
libercsv <- read.csv(file = "index.csv", header = FALSE, sep = ";", dec=",")
x <- data.frame(libercsv)
plot(x, xlab="Escore de Liberdade Econômica", ylab="PIB Per Capita (US$, 2017)")



