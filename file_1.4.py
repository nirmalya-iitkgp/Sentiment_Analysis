from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
import random
import pickle
import nltk

read_reviews = open("battery-life_netbook_1005ha.txt").read()
all_words = []
documents = []

#taking only nouns, verbs and adjectives
allowed_word_types_1 = ["V", "R", "N", "J"]
for p in read_reviews.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[0] not in all_words:
            if w[1][0] in allowed_word_types_1:
                all_words.append(w[0].lower())

all_words = nltk.FreqDist(all_words)
#print(all_words[:3000])

f = open ("pos_dictionary_name.txt","a+")

for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).pos_score() > swn.senti_synset(synset.name()).neg_score():
            for lemma in synset.lemmas():
                f.write(''.join(str(e) for e in(lemma.name())))
                f.write ("\n")
   
f.close()   

f = open ("pos_dictionary_definition.txt","a+")

for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).pos_score() > swn.senti_synset(synset.name()).neg_score():
            for lemma in synset.lemmas():
                f.write(''.join(str(e) for e in(synset.definition())))
                f.write ("\n")
   
f.close()   
   
f = open ("pos_dictionary_examples.txt","a+")

for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).pos_score() > swn.senti_synset(synset.name()).neg_score():
            for lemma in synset.lemmas():
                f.write(''.join(str(e) for e in(synset.examples())))
                f.write ("\n")
  
f.close()

f = open ("neg_dictionary_name.txt","a+")

for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).neg_score() > swn.senti_synset(synset.name()).pos_score():
            for lemma in synset.lemmas():
                f.write(''.join(str(e) for e in(lemma.name())))
                f.write ("\n")
   
f.close()   

f = open ("neg_dictionary_definition.txt","a+")

for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).neg_score() > swn.senti_synset(synset.name()).pos_score():
            for lemma in synset.lemmas():
                f.write(''.join(str(e) for e in(synset.definition())))
                f.write ("\n")
   
f.close()   
   
f = open ("neg_dictionary_examples.txt","a+")

for a in all_words:
    for synset in wordnet.synsets(a):
        if swn.senti_synset(synset.name()).neg_score() > swn.senti_synset(synset.name()).pos_score():
            for lemma in synset.lemmas():
                f.write(''.join(str(e) for e in(synset.examples())))
                f.write ("\n")
  
f.close()



