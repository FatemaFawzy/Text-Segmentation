#function takes the compact sentence (st) and the unigram probabilities and returns the segmented sentence
def segmentation(st, unigramProb) :

  #if the input is an empty string, return an empty list
  if st == "" or st== "nan":
    return []

  n=len(st)
  words=[]        #list of identified words to be returned
  maxProb=[]      #list of probabilities of word sequences -> maxProb[i] is the maxProb probability of word at index i

  #initialize probabilities and words
  for i in range (0,n+1) :
    maxProb.append(0.0)
    words.append("")
  maxProb[0]=1.0

  #fill the lists
  for i in range(1,n+1) :   #i: index of last character in a word in the input string
    for j in range(0,i) :   #j: index of first character in a word in the input string
      
      word= st[j:i]         #formulate a word to test
      w= len(word)          #get the word's length
      
      #for every i (index of last char in a word), we check all sizes of previous words (incrementing j decrements size)
      #if the probability of the word*P(prev word) is larger than the current maxProb,
      #update maxProb to take the highest probability and take this word as a token
      if word in unigramProb and unigramProb[word]*maxProb[i-w] >= maxProb[i] :
        maxProb[i]= unigramProb[word]*maxProb[i-w]
        words[i]=word

  #Order words according to their probabilities
  resultTokens=[]
  i= n
  while i > 0 :
    resultTokens.append(words[i])
    #print(i)
    i-=len(words[i])

  #return reversed list for correct order
  return resultTokens[::-1]