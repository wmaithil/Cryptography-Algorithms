def encrypyt(text,key):
	ct=""
	for i in text:
		ct+=chr(ord(i)+key)
	return ct

def decrypt(ct,key):
	pt=""
	for i in ct:
		pt+=chr(ord(i)-key)
	return pt

if __name__=="__main__":
	text=raw_input("Enter text")   #Enter plain text to be encrypted
	key=int(raw_input("Enter key"))    #Enter the key for encryption

	#Encrypted text
	et=encrypyt(text,key)
	print("The encrypyted text is {}".format(et))

	#Decrypted Text
	dt=decrypt(et,key)
	print("decrypted text is "+dt)

	print("Successfully executed")
