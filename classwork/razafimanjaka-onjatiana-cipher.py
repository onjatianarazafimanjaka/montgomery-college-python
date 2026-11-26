

def cypher(text,key):
    result = ""

   # transverse the plain text
    for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain 
      if (char.isupper()):
         result += chr((ord(char) + key-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + key-97) % 26 + 97)
      return result
      
      
#check the above function
text = "a"
key = 4

print("Plain Text : ", text)
print("Shift pattern : ", str(key))
print("Cipher: ", cypher(text,key))

