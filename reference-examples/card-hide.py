def card_hide(digits):
    digits = input("Enter Credit Card Digits: ")
    strlength = len(digits)
    masked = strlength - 4
    slimstr = digits[masked:]
    print ("*" * masked + slimstr)
card_hide(0)
