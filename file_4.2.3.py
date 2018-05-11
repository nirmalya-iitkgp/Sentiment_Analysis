f = open ("all_dictionary.txt",'w')
a = []
with open("SentiWordNet_3.0.0_20130122.txt") as f1:
    for l in f1:
        l = l.split()
        for word in l:
            if '#' in word:
                a.append((word[:-2],l[0],l[1],l[2],l[3]))
                print((word[:-2],l[0],l[1],l[2],l[3]))
                f.write ("\n")
                f.write(''.join((word[:-2])))
f.close() 

'''f = open ("neg_dictionary.txt",'w')
b = []
with open("SentiWordNet_3.0.0_20130122.txt") as fp:
    for l in fp:
        l = l.split()
        for word in l:
            if '#' in word:
                b.append((word[:-2],l[0],l[1],l[3]))
                print((word[:-2],l[0],l[1],l[3]))
                f.write ("\n")
                f.write('\n'.join('{} {} {} {}'.format(''.join(x[0]),''.join(x[1]),''.join(x[2]),''.join(x[3])) for x in b))  
f.close()  '''         




