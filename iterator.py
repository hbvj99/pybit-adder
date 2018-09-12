import logicGates #import logic gates
from inputNumber import BinaryConversion #import BinaryConversion function

def totalSum(): #Total sum function
    global sumF #Make global
    global li1
    global li2
    sumF=[] #Create list
    cIn=0 #Initializing varibales carry in as 0
    li1, li2 = BinaryConversion() #Convert lil 1 and list 2 into binary conversion
    x1=len(li1)-1 #Minus -1 from list 1 and 2
    x2=len(li2)-1 
    #print(li1,li2) #Display lil1 and list 2
    
    for i in range(len(li1)): #For loop having length list 1 inside perimeter 
        x01=li1[x1] #Add in list xo1 and xo2 
        x02=li2[x2]
            
        xor1= logicGates.xor1Operation(x01,x02) #XOR gate return x01 and x02
        and1 = logicGates.and1Operation(x01,x02) #AND1 gate returns x01 and x02
        and2 = logicGates.and2Operation(xor1, cIn) #AND2 gate returns xor1 and carry in
        nor1 = logicGates.norOperation(and1, and2) #NOR1 gate returns AND1 and AND2 
        not1 = logicGates.notOperation(nor1) #NOT1 gate returns nor1, carry out
        nand = logicGates.nAndOperation(xor1, cIn) #NAND gate returns xor1 and carry in
        or1 = logicGates.or1Operation(xor1, cIn) #OR1 gate returns xor1 and carry in
        and3 = logicGates.and3Operation(or1, nand) #AND3 gate returns or1 and nand as sum, sum
        sumF.append(and3) #Add and3 to sumF

        x1=x1-1 #Minus 1
        x2=x2-1
        cIn = not1 #carry in 
            
    sumF.reverse() #Reverse the list as it print in descending order
 
    print("Sum:",sumF) #Print total sum
    
