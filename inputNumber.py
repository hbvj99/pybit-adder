print("Welcome to Decimal to Binary Converter!") #Welcome message
def BinaryConversion():
    print("---------------------------------------") #Seprates the codes when run
    i = False
    while not i:
        i1 = input("Enter First Decimal Number?") #Input integer i1
        i2 = input("Enter Second Decimal Number?") #Input integer i2
        n1=list(i1) #Creates new list
        n2=list(i2)
        nos=['0','1','3','2','4','5','6','7','8','9'] #Values inside nos list
        for each in n1: #Check n1
            if each not in nos: #Not in nos list
                print("---------------------------------------") #Seprates the codes when run
                print("Error! Please enter valid number") #Print error
                break
        else:
            for each in n2: #check n2
                if each in nos: #this loop doesn't block invalid input
                    i=True #run loop
                else:
                    print("---------------------------------------") #Seprates the codes when run
                    print("Error! Please enter valid number") #display error
                    break #break loop
            
    no3=int(i1) #adding no3 and no3 int 
    no4=int(i2)

    if int(no3)<=128 and int(no3)>=0 and int(no4)<=128 and int(no4)>=0:#check condition
        db1=bin(no3) #Conversion of integer to binary number
        db2=bin(no4)

        l1=list(db1) #Adding binary number in db1 and db2 list
        l2=list(db2)

        l1F=l1[2::] #Display numbers after 2nd list order
        l2F=l2[2::]

        while len(l1F) < 8: #Adding two zeroes values if list is less than 8 to match 8 bit binary numbers
            l1F.insert(0,0)
        while len(l2F) <8:
            l2F.insert(0,0)
            
        list1=[] #Creating list1 and list2
        list2=[]

        for i in range(len(l1F)):
            l=int(l1F[i]) #Converting string values to Integer
            m=int(l2F[i])
            list1.append(l) #Adding Integer in list
            list2.append(m)

        #print("First Binary:",list1) #Display list1 and list2
        #print("Second Binary:",list2)
           
    else : #Display error message if input doesn't match if loop condition
            print("ERROR! The value must not exceed or less than the actual size of byte-coded integer 0 and 255")
            print("Enter number between 0 and 128!!")
            print(BinaryConversion())
    return list1, list2 #Returns list1 and list 2
