book = {}
a=[]
with open("SentiWordNet_3.0.0_20130122 - Copy.txt") as f:
    for l in f:
        l = l.split()
        for i,word in enumerate(l):
            if '#' in word:
                try: 
                    if book[word[:-2]] < l[2]:
                        t = (word[:-2],l[0],l[1],l[2])
                        a.append(t)
                        print(t)
                        book[word[:-2]] = l[2]
                except KeyError:
                    t = (word[:-2],l[0],l[1],l[2])
                    a.append(t)
                    print(t)
                    book[word[:-2]] = l[2]