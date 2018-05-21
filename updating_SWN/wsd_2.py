from nltk.wsd import lesk
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

all_words = []
stop_words = set(stopwords.words('english'))
read_review = open("review_file.txt").read()
for line in read_review.split('\n'):
	words = word_tokenize(line)
	pos = nltk.pos_tag(words)
	for w in pos:
		if w[0] not in stop_words:
			print(w[0])
			print(w[1])
			if (lesk(line, w[0],w[1][0].lower())) is not None:
				all_words.append(lesk(line, w[0],w[1][0].lower()).name()[:-5])

set =[]
with open("SentiWordNet_3.0.0_20130122.txt") as f1:
    
    for line in f1:
        i= 0 
        l = line.split()
        score = 0
        for word in l:
            i = i + 1
            if word in all_words:
                #print('now score' + str(score))
                score = score + 1
        if score != 0:
        	set.append(( score / i , str(line)))

set = sorted(set, key =itemgetter(0), reverse = True)
f = open ("all_dictionary.txt",'w')
for element in set:
	print(element[0])
	f.write(element[1])
	print('\n')
f.close()
