import random
n=100
primelist=[]    #list to maintain a list of prime numbers
for i in range(2,n):    #load prime numbers till 100 in primelist
    flag=0
    for j in range(2,i):
        if(i%j!=0):
            flag +=1
        else:
            break
    if(flag==(i-2)): #if prime number is found! flag will always be equal to n-2
        primelist.append(i)

print primelist

#Public key
g=random.choice(primelist)
print " g is",g
# Select the modulus factor
n=random.choice(primelist)
print " n is",n

#Input private of Bob and Alice Private key
x=int(raw_input("Enter Alice private key")) #select private key of Alice
y=int(raw_input("Enter bob private key"))   #select private key of Bob

#generating sharing keys
A=(g**x)%(n)

B=(g**y)%(n)
#generating k1 and k2
K1=(B**x)%(n)

K2=(A**y)%(n)

print "The 1st private key generated is : ",K1
print "The 2nd private key generated is : ",K2

#comparing keys
if(K1==K2):
    print "Access granted"
else:
    print "Access denied"


