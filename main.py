import pandas as pd
import re
import nltk
from nltk.tokenize import RegexpTokenizer
#nltk.download('punkt')        #uncomment this line for the first run only
from Segmentation import *
from unigramProbabilites import *

#read data file
data= pd.read_csv('sets\myDataSet.csv')

#For accuracy percentage calculations
totalCasesCount=len(data)
algoCorrectCount=0
libCorrectCount=0
#for precision and recall
truePos=0
trueNeg=0
falsePos=0
falseNeg=0

#iterate on dataframe rows
for index,row in data.iterrows() :
  tp=0
  #segment input text using algorithm
  result= segmentation(str(row['input']), unigramProb)
  #compare result with correct output
  if str(result) == row['output']:
    algoCorrectCount+=1

  #segment original input using library
  libraryResult= nltk.tokenize.word_tokenize(row['original'])
  #compare result with correct output
  if str(libraryResult) == row['output']:
    libCorrectCount+=1
  
  #calculating precision and recall
  for word in result :
    if word in row['output'] :
      truePos+=1
      tp+=1
    elif word not in row['output'] :
      falsePos+=1
  falseNeg+=len(row['output'].strip('][').split(', '))-tp
  
#calculate and print accuracy, precision, recall
accuracy=((truePos+trueNeg)/(truePos+falsePos+falseNeg+trueNeg))*100
precision=((truePos)/(truePos+falsePos))*100
recall=((truePos)/(truePos+falseNeg))*100

print("\nMETHOD 1 (GLOBAL)\n")
print("Accuracy=",accuracy,"%")
print("Precision=",precision,"%")
print("Recall=",recall,"%\n")
print("--------------------------\n")
#print both accuracies for comparison
print("METHOD 2 (LIST DIFFERENCE):\n")
algoAccuracy= (algoCorrectCount/totalCasesCount)*100
print("Accuracy=",algoAccuracy,"%\n")
print("--------------------------\n")
print("METHOD 3 (LIBRARY):\n")
libraryAccuracy= (libCorrectCount/totalCasesCount)*100
print("Accuracy=",libraryAccuracy, "%\n")