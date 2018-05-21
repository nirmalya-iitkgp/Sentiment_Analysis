import nltk
from nltk.tokenize import word_tokenize
from operator import itemgetter

test_file = open("test_file.txt").read()
all_words = []
allowed_word_types_1 = ["V", "R", "N", "J"]
for p in test_file.split('\n'):
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types_1:
        	if w[0] not in all_words:
        		all_words.append(w[0])

set =[]
with open("SentiWordNet_3.0.0_20130122.txt") as f1:
    i=0
    for line in f1:
        i= i + 1 
        l = line.split()
        score = 0
        for word in l:
            if word in all_words:
                #print('now score' + str(score))
                score = score + 1
        set.append(( i, score, str(line)))

set = sorted(set, key =itemgetter(1), reverse = True)
f = open ("all_dictionary.txt",'w')
for element in set:
	print(element)
	f.write(element[2])
	print('\n')
f.close()