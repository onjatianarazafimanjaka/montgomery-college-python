
def cypher(text, key):
    testing = test(text, key)
    encryption(text, key)

def test(t, k):
    testAlph = t.isalpha() 
    testInt = k.isnumeric()

    if testAlph == True:
        return t   
    else:
        print("Text has to be part of the alphabet")

    if test_integer == True:
        return k
    else:
        print("Key has to be an integer")

def encryption(text, key):
    #to be completed

cypher("abcd", 265)
    

