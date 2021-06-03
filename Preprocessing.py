import pandas as pd
import re

#Reading dataset from file. Covert all to lowercase
df= pd.read_csv("sets\RandomSentencesDS.csv", error_bad_lines=False)['text'].dropna().str.lower()

#remove special characters by replacing them with an empty string. Keep letters, hyphens, and white space only
filtered_data= df.apply(lambda x: re.sub(r'[^a-z-\s]','',x))

#for word-word, replace - with white space because it's likely to improve detection accuracy
filtered_data= filtered_data.apply(lambda x: re.sub(r'[-]',' ',x))
filtered_data.replace(" ", float("NaN"), inplace=True)
filtered_data.replace("", float("NaN"), inplace=True)
filtered_data.dropna(inplace=True)

#remove spaces and save values in a new file with columns [input, output, original]
allData= pd.DataFrame(filtered_data.apply(lambda x: x.replace(" ","")))
allData["output"]=filtered_data.apply(lambda x: x.split())      #expected word segmentation output ["hey","whats","up"]
allData.rename(columns={'text':'input'},inplace=True)           #compact sentence "heywhatsup"
allData["original"]=filtered_data                               #original sentence after preprocessing "hey whats up" -> used for testing with a library

allData.to_csv('sets\myDataSet.csv')