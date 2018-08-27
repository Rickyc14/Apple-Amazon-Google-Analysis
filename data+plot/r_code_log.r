library(Quandl)
library(quantmod)
library(plotly)
getSymbols(src="yahoo")
View(AAPL)
View(AAPL)
getSymbols("AAPL",from="2014-01-01")
getSymbols("AMZN",from="2014-01-01")
getSymbols("GOOG",from="2014-01-01")
View(AAPL)
ap =AAPL[,6] %>% log %>% diff
am =AMZN[,6] %>% log %>% diff
go =GOOG[,6] %>% log %>% diff
par(mfrow=c(3,1)
par(mfrow=c(3,1))
plot(ap,type="l")
plot(am,type="l")
plot(go, type="l")
savehistory("C:/Users/ricar/Downloads/R/returnsz/r_code_log.r")
