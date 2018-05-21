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




