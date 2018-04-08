
msgc=""

def main(k):
    global msgc
    if k<0 or k>231:
        print ("Error!")
        raise SystemExit
    Input = input("\n[*] Write the text:\n[text] >> ")
    for x in range(len(Input)):
        letter=Input[x]
        if letter.isupper():
            x=ord(letter)
            x=x+k
            msgc+=chr(x)
        if letter.islower():
            x=ord(letter)
            x=x+k
            msgc+=chr(x)
    crypt=open("text_crypt.txt","w")
    print("\nCrypt-text: "+msgc+"\n")
    crypt.write(msgc)
    crypt.close()

msgd=""

def dec1(k):
    global msgd
    if k<0 or k>231:
        print ("Error!")
        raise SystemExit
    decrypt_r=open("text_crypt.txt","r")
    read=decrypt_r.read()
    for x in range(len(read)):
        letter=read[x]
        if letter.isupper():
            x=ord(letter)
            x=x-k
            msgd+=chr(x)
        if letter.islower():
            x=ord(letter)
            x=x-k
            msgd+=chr(x)
    print("\n[*] Decrypted text:")
    print("[text] << "+str(msgd))
    answer=input("\n[*] Save decrypted text in the file?\n[y/n] > ")
    if answer=="y" or answer=="Y":
        decrypt_w=open("text_decrypt.txt","w")
        decrypt_w.write(msgd)
        decrypt_w.close()
        print("\n[+] File 'text_decrypt.txt' successfully saved! ")
    else:
        pass
    decrypt_r.close()

def dec2(k):
    global msgd
    if k<0 or k>231:
        print ("Error!")
        raise SystemExit
    Input = input("\n[*] Write the text:\n[text] >> ")
    for x in range(len(Input)):
        letter=Input[x]
        if letter.isupper():
            x=ord(letter)
            x=x-k
            msgd+=chr(x)
        if letter.islower():
            x=ord(letter)
            x=x-k
            msgd+=chr(x)
    print("\n[*] Decrypted text:")
    print("[text] << "+str(msgd))

print("1) Crypt the text")
print("2) Decrypt text from the file")
print("3) Decrypt text from the terminal\n")

ans1=int(input("[*] Write the number:\n[number] > "))
ans2=int(input("Write the [0-52] number-key: "))

if ans1==1:
    main(ans2)
elif ans1==2:
    dec1(ans2)
elif ans1==3:
    dec2(ans2)
else:
    print("Number is not defined!")
