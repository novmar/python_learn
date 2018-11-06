### 1. Make a list of pets. You will need it in later exercises. Known pets are: 'dog', 'cat', 'rabbit', 'snake'

pets = [ 'dog', 'cat', 'rabbit', 'snake',]



### 2. Write a functon that returns the name of pets (list given as the argument) that are shorter than 5 leters.
def fiveless (mypets):
    pets5 = []
    for pet in mypets:
        if len(pet)<5 :
            pets5.append(pet)
    return(pets5)

### 3. Write a functon that returns the names of pets (list given as the argument) that begin with 'd'.
def dstarted (mypets):
    dstart = []
    for pet in mypets:
        if pet[0] == "d":
            dstart.append(pet)
    return dstart


### 4. Write a functon that gets a word and detects if it's in the pet list. “Detects” means that the functon returns True or False.
def ispet(tryit):
    if tryit in pets: return True
    else: return False



### 5. Write a functon that gets two lists of animal names and returns three lists:
### (a) the animals that are on both lists (common ones),
### (b) animals which are only in the frst list,
### (c) animals that are only in the second list
### Write the test to verify that it works properly.

def comparelists(one,two):
    both = [] # Prepare "both"
    o = list(set(one))    # clear duplications
    t = list(set(two))    # clear duplications
    print(one,o,"\n",two,t,"\n")
    for i in one:
        if i in t:
            both.append(i)
            t.remove(i)
            o.remove(i)
    return o,t,both


### 6. Write a program that sorts the list of pets by alphabet.
def normalsort(list):
    return sorted(list)

### 7. Write a functon that sorts the animals alphabetcally, but ignores the frst leter
### Returns: ['rabbit', 'cat', 'snake', 'dog']
def weirdsort(list):
    prelist={}
    key=[]
    ws=[]
    for i in list:
        prelist[i[1:]]= i
        key.append(i[1:])
    for i in sorted(prelist):
        ws.append(prelist[i])
    return ws


### Results

### 1.
#print(pets)
### 2.
#print(fiveless(pets))
### 3.
#print(dstarted(pets))
### 4.
#print(ispet("dog"))
#print(ispet("cat"))
#print(ispet("morce"))
### 5.

f=["ahoj","aneta","nema","nohy","aneta"]
s=["zdar","aneta","nova","nema","zadny","ruce"]
#print ("vysledky:",comparelists(f,s))

f=["ahoj","aneta","nema","nohy"]
s=["zdar","aneta","nova","nema","zadny","ruce"]
#print ("vysledky:",comparelists(f,s),"\n\n")

f=["oba1","oba2","oba3","prvni1","prvni1"]
s=["druha12","oba1","oba2","oba3","druha1"]
#print ("vysledky:",comparelists(f,s))
### 6.
#print (normalsort(pets))
### 7.
#print(weirdsort(pets))
