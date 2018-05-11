import nltk
from nltk.tokenize import word_tokenize

f = open ("pos_dictionary.txt",'w')
a = []
with open("SentiWordNet_3.0.0_20130122.txt") as f1:
    for l in f1:
        l = l.split()
        for word in l:
            if '#' in word:
            	if l[2] > l[3]:
	                a.append((word[:-2],l[0],l[1],l[2]))
	                print((word[:-2],l[0],l[1],l[2]))
	                f.write ("\n")
	                f.write(''.join(word[:-2]))
f.close() 

f = open ("neg_dictionary.txt",'w')
b = []
with open("SentiWordNet_3.0.0_20130122.txt") as fp:
    for l in fp:
        l = l.split()
        for word in l:
            if '#' in word:
            	if l[3] > l[2]:
	                b.append((word[:-2],l[0],l[1],l[3]))
	                print((word[:-2],l[0],l[1],l[3]))
	                f.write ("\n")
	                f.write(''.join(word[:-2])) 
f.close()           


test_file = open("test_file.txt").read()
allowed_word_types_1 = ["V", "R", "N", "J"]
for p in test_file.split('\n'):
    score = 0
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
    	if w[1][0] in allowed_word_types_1:
    		if w in a[:][0]:
    			score = score + 1
    		elif w in b[:][0]:
    			score = score - 1
    print(score)

