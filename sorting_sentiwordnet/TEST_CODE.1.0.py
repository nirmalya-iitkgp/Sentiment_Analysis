from nltk.tokenize import word_tokenize
import nltk

dic_file_pos = open("pos_dictionary.txt").read()
dic_file_neg = open("neg_dictionary.txt").read()
test_file = open("test_file.txt").read()

pos_list = dic_file_pos.split('\n')
print(len(pos_list))
neg_list = dic_file_neg.split('\n')
print(len(neg_list))

SCORE = 0
net = 0

allowed_word_types_1 = ["V", "R", "N", "J"]
for p in test_file.split('\n'):
    
    score = 0
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types_1:
                if w[0] in neg_list:
                    score = score - 1
                    
    for w in pos:
        if w[1][0] in allowed_word_types_1:
                if w[0] in pos_list:
                    score = score + 1
                    
    if score > 0:
        print("review positive")
        SCORE = SCORE + 1

    elif score < 0:
        print("review negative")
        SCORE = SCORE - 1

    net = net + 1

print (SCORE)
print (net)
print (SCORE / net)
    
    
    

