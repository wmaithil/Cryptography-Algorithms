li1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 's', 'u', 'v', 'w', 'x', 'y', 'z']
li2 = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']

def encrypt(pt):
    ct=''
    for i in pt:
        ct+= li2[li1.index(i)]
    return ct

def decrypt(ct):
    pt=''
    for i in ct:
        pt+=li1[li2.index(i)]
    return pt

if __name__ == '__main__':
    pt=raw_input("Enter Plain text")

    et=encrypt(pt)
    print "Encrypted text is "+et

    dt=decrypt(et)
    print "Decrypted text is"+dt




