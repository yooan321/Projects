library(dplyr)
library(ggplot2)

a = data.frame(x = 1:10, y = rnorm(10))
ggplot(a, aes(x = x, y = y)) + geom_point()