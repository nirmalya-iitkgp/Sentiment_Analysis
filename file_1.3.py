from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
import random
import pickle
import nltk

read_reviews = open("battery-life_netbook_1005ha.txt").read()
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

pos_dictionery = []			
for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).pos_score() > 0.5:
            for lemma in synset.lemmas():
                pos_dictionery.append( (lemma.name(), synset.definition(), synset.examples()))
		

f = open ("pos_dictionary.txt","a+")
f.write('\n'.join('{} ::: {} ====== {}'.format(x[0],x[1], x[2]) for x in pos_dictionery))

f.close()

neg_dictionery = []			
for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).neg_score() > 0.5:
            for lemma in synset.lemmas():
                neg_dictionery.append( (lemma.name(), synset.definition(), synset.examples()))
		

f = open ("neg_dictionary.txt","a+")
f.write('\n'.join('{} ::: {} ====== {}'.format(x[0],x[1], x[2]) for x in neg_dictionery))

f.close()
