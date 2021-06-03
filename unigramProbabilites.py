#loading word counts file and compute their total count
unigramProb={}
totalCount=0
with open('sets\count_1w.txt','r') as f:
  for line in f:
    line=line.split()
    if len(line) ==2 :
      unigramProb[line[0]]=int(line[1])
      totalCount+=int(line[1])

#calculate unigram probabilities   
for word,count in unigramProb.items():
  unigramProb[word]=count/totalCount
