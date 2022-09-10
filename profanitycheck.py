import re
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize,sent_tokenize

with open("profanewords.txt","r") as f:
    profane=f.read()
with open("tweets.txt","r") as f:
    tweet=f.read()
    

tokenize_prowords = word_tokenize(profane.lower())
print(tokenize_prowords)
white=list(filter(None,re.split(r'[,.!? "|();\n]',tweet.lower())))
count=0
for i in white:
    for j in tokenize_prowords:
        if i == j:
            count+=1

degree=count/len(white)
print(degree)