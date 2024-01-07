import random_gen

n = int(input("n : "))

arr = [25] * 20 # araye az mizan pool har fard

rnd = random_gen.rand()

while (n > 0) :
    n -= 1 # yeki az n kam shavad ta while daghighan n bar ejra shavad
    e = [] # araye az pool jadid har fard
    k = 0
    while (k < len(arr)) : # copy kardan pool ha az arr be e
        e.append(arr[k])
        k += 1
    t = len(arr)
    while (t > 0) : # halghe pool dadan va gereftan
        t -= 1
        
        if (e[t] == 0) :
            continue
        
        person = rnd.rand_int(0, len(arr) - 1)
        while (person == t) :
            person = rnd.rand_int(0, len(arr) - 1)
        
        e[t] -= 1
        e[person] += 1
    
    arr = []
    t = 0
    while (t < len(e)) : # faghat anhayee ke pooleshan 0 nist ra negah dar
        if (e[t] != 0) :
            arr.append(e[t])
        t += 1


print(arr)