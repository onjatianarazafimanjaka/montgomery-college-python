def card_hide():
    digits = input("Enter Credit Card Digits: ")
    strlength = len(digits)
    masked = strlength - 4
    slimstr = digits[masked:]
    print ("*" * masked + slimstr)
    return digits
card_hide()
