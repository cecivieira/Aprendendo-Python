library("caret")

setwd("/home/ceferra@upvnet.upv.es/Descargas/")
train<-read.csv("train.csv")
summary(train)
trainf<-train[,c("SaleType","SaleCondition","YrSold","YearBuilt","HouseStyle","OverallQual","SalePrice")]
summary(trainf)
fitControl <- trainControl(## 10-fold CV
  method = "repeatedcv",
  number = 10,
  ## repeated ten times
  repeats = 10)
model <- train(SalePrice ~ ., data = trainf, 
                 method = "lm", 
                 trControl = fitControl,
                 verbose = FALSE)

test<-read.csv("test.csv")
testf<-test[,c("SaleType","SaleCondition","YrSold","YearBuilt","HouseStyle","OverallQual")]
testf[1030,1]<-testf[1031,1] ### Tapar un NA
testf$SalePrice<-predict(model,testf)
testf$Id<-test$Id
write.csv(testf[,c("Id","SalePrice")],file="preds.csv",row.names =FALSE)
