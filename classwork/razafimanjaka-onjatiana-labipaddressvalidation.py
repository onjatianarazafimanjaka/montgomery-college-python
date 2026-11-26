def IPv4(ip_address):
    
    portions = ip_address.split(".")

    if len(portions) != 4:
        print("{} is not a valid IPv4 address.".format(ip_address))
        return False

    for portion in portions:
        if not isinstance(int(portion), int):
            print("{} is not a valid IPv4 address.".format(ip_address))
            return False

        if int(portion) < 0 or int(portion) > 255:
            print("{} is not a valid IPv4 address.".format(ip_address))
            return False

        if int(portions[3]) == 0:
            print("{} is not a valid IPv4 address.".format(ip_address))
            return False
        

    print("{} is a valid IPv4 address.".format(ip_address))
    return True

IPv4(input("Enter IPv4 address: "))