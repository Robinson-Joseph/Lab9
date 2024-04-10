



def encoder():
    unencoded = input("Please enter your password to encode: ")
    encoded = ""
    for i in unencoded:
        encoded = encoded + str(int(i)+3)
    print("Your password has been encoded and stored!")
    return encoded

def decoder(password):
    x = [int(y) for y in str(p)]
    y = ""
    for i in range(8):
        x[i] -= 3
        if x[i] < 0:
            x[i] += 10
        y += str(x[i])
    return y

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




