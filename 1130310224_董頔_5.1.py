alli=[]                                 #Make empty lists 
repeat=[]                               #for later use.
raw={}                                  #To store every word user input.
words=[]                                   #To convenience's sake, use this to help to print.
for i in range(100):
    x=raw_input()
    y=x.split()                         #Get every word from what user has input with every raw.                     #Make those words in every raw into a list
    for v in y:
        if v in raw:
            if i + 1 not in raw[v]:
                raw[v].append(i+1)
        else:
            raw[v] = [i + 1]

ordered_list=sorted(raw.iteritems(),key=lambda asd:asd[0])        #Make word to be display into dictionary order

for items in ordered_list:
    temp = list(items[1])
    temp.sort()
    print items[0]+':',str(temp)[1:-1]                        #Print Inverted Index.

while True:                                            #For user to search
    tuplei=[]
    AND=[]                                          #For the position-set list.
    e=raw_input()
    if e == '':
        break                                       #If input return, end loop and end program.
    else:                                           #Make input into lower case.
        d=e.split()                                 #Get word user want to search.
        for el in d:
            if not raw.has_key(el):
                print 'None'
                conti=False
                break
            else:
                tuplei.append(el)
                conti=True                          #If there is no such word user input in the former list, print None, else, make them into a list.
        if conti==True:
            for needs_done in tuplei:
                a = raw[needs_done]
                AND.append(a)
               #Get the position of word showed up.
            all_lst = [i for i in range(1,101)]
            allset=set(all_lst)
            for n in AND:
                allset=allset & set(n)
            if len(allset)==0:
                print 'None'                        #Get the public position.
            else:
                out =list(allset)
                out.sort()
                print str(out)[1:-1]       #Display the result.