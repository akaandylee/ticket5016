def encrypt(text,s):
    result = ""
    # traverse text
    for i in range(len(text)):
    char = text[i]
    #Encrypt Uppercase characters in plain text else if (char.isupper()):

result +=\
    chr((ord(char)+s-97)% 26+97)
return result text = "HAIL CAESAR OUR HERO"
s = 4

print ("text : " + text)

Print ("shift : " + str (s))
print ("Cipher: "+encrypt(text,s))