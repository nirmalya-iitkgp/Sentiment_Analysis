from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import random
import pickle
import nltk

read_reviews = open("review_file.txt").read()
all_words = []
documents = []

allowed_word_types_1 = ["V", "R", "N", "J"]

for p in read_reviews.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types_1:
            all_words.append(w[0].lower())

dictionery = []			
for a in all_words:
    for synset in wordnet.synsets(a):
        for lemma in synset.lemmas():
            dictionery.append( (lemma.name(), synset.definition(), synset.examples()))
		

f = open ("new_dictionary.txt","a+")
f.write('\n'.join('{} ::: {} ====== {}'.format(x[0],x[1], x[2]) for x in dictionery))

f.close()
