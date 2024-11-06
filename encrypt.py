def encrypt(string,shift):
    cihper=" "
    for char in string:
        if char=='':
            cihper = cihper +char
        elif char.isupper():
            cihper = cihper + chr((ord(char)+shift-65) % 26+65)
        else:
            cihper = cihper + chr((ord(char)+shift-97) % 26+97)
    
    return cihper

text=input("Enter a String : ")
shift=int(input("Enter a Shift :"))
print("Original Text",text)
print("Encrypted Text",encrypt(text,shift))
