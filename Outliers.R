install.packages("readr")

library(readr)

boston <- read.csv(file.choose())
View(boston)
##### check for NAvalues
sum(is.na(boston)) 


boxplot(boston$crim) #boxplot to check the outlier

quantile(boston$crim) 

##### use subset function to treat the outlier
boston1 <- subset(boston,boston$crim <= 0.25) 

boxplot(boston1$crim) # boxplot plot to check for further outlier


boxplot(boston$zn) 

quantile(boston$zn) 

boston2 <- subset(boston,boston$zn <12.5)  

boxplot(boston2$zn)  


boxplot(boston$indus) 
##### no outlier


boxplot(boston$rm) 

quantile(boston$rm)

boston3 <- subset(boston,boston$rm <= 4.5)  

boxplot(boston3$rm) 


boxplot(boston$age) 
#####   no outlier


boxplot(boston$dis) 

quantile(boston$dis)  

boston4 <- subset(boston,boston$dis <8.7) 

boxplot(boston4$dis)  

boxplot(boston$rad) 
##### no outlier

boxplot(boston$tax) 
##### no outlier

boxplot(boston$ptratio) 

quantile(boston$ptratio)  

boston5 <- subset(boston,boston$ptratio >13) 

boxplot(boston5$ptratio) 

boxplot(boston$black)

quantile(boston$black)

boston6 <- subset(boston,boston$black >385)

boxplot(boston6$black)

boxplot(boston$lstat)

quantile(boston$lstat)

boston7 <-subset(boston,boston$lstat <30)

boxplot(boston7$lstat)

boxplot(boston$medv)

quantile(boston$medv)

boston8 <- subset(boston, boston$medv <=6.9)

boxplot(boston8$medv)
