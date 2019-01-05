import random
primelist=[]
n=100

for i in range(2,n):
    flag=0
    for j in range(2,i):
        if(i%j == 0):
            break
        else:
            flag+=1
    if(flag==(i-2)):
        primelist.append(i)
print("Generated prime list is :")
print(primelist)

p=int(random.choice(primelist))
q=int(random.choice(primelist))

N=p*q
print "N :"+str(N)
N1=(p-1)*(q-1)

sf=0
for i in range(3,N1):
    if((p-1)%i==0 or (q-1)%i==0):
        break
    else:
        sf=i
        break

e=sf
print "Public key e is {}".format(e)

d=int(gmpy2.invert(e,N1))
print "Private key d is {}".format(d)
if __name__=="__main__":
    pt=int(raw_input("Enter plain text"))
    ct=(pt**e)%N
    print("Encrypted key is {}".format(ct))
    dt=(ct**d)%(N)
    print("Decrypted key is {}".format(dt))
