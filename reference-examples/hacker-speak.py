def hacker_speak(a):
    a = input("Enter text: ")
    b = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',}
    for x,y in b.items():
        a = a.replace(x, y)
    print(a)
hacker_speak("This is a test")
