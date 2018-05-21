a = []
t = []
with open("SentiWordNet_3.0.0_20130122.txt") as f1:
    try: 
        for line in f1:        
            l = line.split()
            for word in l:            
                if '#' in word:
                    
                    if word[-2]=='1' or word[-2]=='2' :
                       t.append(word[:-3])
                       a.append((word[:-3]+ '\t\t' +line))

                    if int(word[-1]) > 1 and word[-2]=='#':
                        t.append(word[:-2])
                        a.append((word[:-2]+ '\t\t' +line))
                    
                    if word[:-2] in t:
                        a.append((word[:-2]+ '\t\t' +line))
                    
    except IndexError:
                    pass
a= sorted(a)
f = open ("all_dictionary.txt",'w')
for element in a:
    f.write(element)
    print (element)
f.close()

#f.write (word[:-3]+ '\t\t' +line)
#print(word[:-3]+ '\t\t' +line)
#f.write(word[:-2]+ '\t\t' +line)
#print(word[:-2]+ '\t\t' +line)