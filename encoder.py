



def encoder():
    unencoded = input("Please enter your password to encode: ")
    encoded = ""
    for i in unencoded:
        encoded = encoded + str(int(i)+3)
    print("Your password has been encoded and stored!")
    return encoded

def main():
    while True:
        print("Menu:")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        entered = int(input("Please enter an option: "))
        stored = ""
        match entered:
            case 1: stored = encoder()
            case 2: decoder()
            case 3: exit(200)


if __name__ == "__main__":
    main()




