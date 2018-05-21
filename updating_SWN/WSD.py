import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from operator import itemgetter

read_reviews = open("review_file.txt").read()
all_words = []
documents = []

allowed_word_types_1 = ["V","N","R","J"]
allowed_word_types_2 = ["E", "D", "F", "I", "P","C"]
lemmatizer = WordNetLemmatizer()
for p in read_reviews.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types_1:
            if w[1][0] != 'J':
                word = lemmatizer.lemmatize(w[0], pos=w[1][0].lower())
                if word not in all_words:
                    print(word)
                    all_words.append(word)
            else:
                word = lemmatizer.lemmatize(w[0], pos='a')
                if word not in all_words:
                    print(word)
                    all_words.append(word)
                word = lemmatizer.lemmatize(w[0], pos='s')
                if word not in all_words:
                    print(word)
                    all_words.append(word)    

        elif w[1][0] not in allowed_word_types_2:
            word = lemmatizer.lemmatize(w[0])
            if word not in all_words:

                all_words.append(word)


all_words = sorted(all_words,key=all_words.count,reverse=True)



stop_words = set(stopwords.words('english')) 
filtered_words = []
for w in all_words: 
    if w not in stop_words: 
        filtered_words.append(w)


set =[]
with open("SentiWordNet_3.0.0_20130122.txt") as f1:
    
    for line in f1:
        i= 0 
        l = line.split()
        score = 0
        for word in l:
            i = i + 1
            if word in filtered_words:
                #print('now score' + str(score))
                score = score + 1
       	set.append(( score / i , str(line)))

set = sorted(set, key =itemgetter(0), reverse = True)
f = open ("all_dictionary.txt",'w')
for element in set:
	print(element[0])
	f.write(element[1])
	print('\n')
f.close()