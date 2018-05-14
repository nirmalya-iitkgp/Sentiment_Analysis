from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn

f = open ("pos_dictionary_name.txt","a+")

pos_words = []
for ss in swn.all_senti_synsets():
    if ss.pos_score() > ss.neg_score ():
        pos_words.append (ss.synset)
        f.write(ss.synset.name()[:-5])
        f.write ("\n")

f.close()


f = open ("neg_dictionary_name.txt","a+")

neg_words = []
for ss in swn.all_senti_synsets():
    if ss.neg_score() > ss.pos_score ():
        neg_words.append (ss.synset)
        f.write(ss.synset.name()[:-5])
        f.write ("\n")

f.close()
