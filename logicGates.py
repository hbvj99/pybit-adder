 
def xor1Operation(c, d): #XOR gate operation
    if c == 0 and d == 0:
        x1 = 0
    elif c == 1 and d == 1:
        x1 = 0
    elif c == 0 and d == 1:
        x1 = 1
    elif c == 1 and d == 0:
        x1 = 1
    return x1


def and1Operation(c, d): #AND gate operation
    if c == 0 and d == 0:
        a1 = 0
    elif c == 0 and d == 1:
        a1 = 0
    elif c == 1 and d == 0:
        a1 = 0
    elif c == 1 and d == 1:
        a1 = 1
    return a1


def or1Operation(x1, cIn): #OR gate operation
    if x1 == 0 and cIn == 0:
        o1 = 0
    elif x1 == 0 and cIn == 1:
        o1 = 1
    elif x1 == 1 and cIn == 0:
        o1 = 1
    elif x1 == 1 and cIn == 1:
        o1 = 1
    return o1

def and2Operation(x1, cIn): #AND2 gate operation
    if x1 == 0 and cIn == 0:
        a2 = 0
    elif x1 == 0 and cIn == 1:
        a2 = 0
    elif x1 == 1 and cIn == 0:
        a2 = 0
    elif x1 == 1 and cIn == 1:
        a2 = 1
    return a2


def nAndOperation(x1, cIn): #NAND operation gate
    if x1 == 0 and cIn == 0:
        nan1 = 1
    elif x1 == 0 and cIn == 1:
        nan1 = 1
    elif x1 == 1 and cIn == 0:
        nan1 = 1
    elif x1 == 1 and cIn == 1:
        nan1 = 0
    return nan1

def norOperation(a1, a2): #NOR gate operation
    
    if a1 == 0 and a2 == 0:
        nor1 = 1
    elif a1 == 0 and a2 == 1:
        nor1 = 0
    elif a1 == 1 and a2 == 0:
        nor1 = 0
    elif a1 == 1 and a2 == 1:
        nor1 = 0
    return nor1

def and3Operation(o1, nan1): #AND3 gate operation
    if o1 == 0 and nan1 == 0:
        su = 0
    elif o1 == 0 and nan1 == 1:
        su = 0
    elif o1 == 1 and nan1 == 0:
        su = 0
    elif o1 == 1 and nan1 == 1:
        su = 1
    return su


def notOperation(nor1): #Function having nor1 gate as perimeter
    if nor1 == 0: #If nor1 is 0 carry out 1
        cOut = 1
    elif nor1 == 1:
        cOut = 0 #Else carry out as 0
    return cOut #Return carry out


            

