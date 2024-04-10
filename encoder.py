



def encoder():
    unencoded = input("Please enter your password to encode: ")
    encoded = ""
    for i in unencoded:
        num = int(i)+3
        if num > 10:
            num -=10
        encoded = encoded + str(num)
    print("Your password has been encoded and stored!")
    return encoded

def decoder(password):
    x = [int(y) for y in str(password)]
    y = ""
    for i in range(len(x)):
        x[i] -= 3
        if x[i] < 0:
            x[i] += 10
        y += str(x[i])
    print(f"The encoded password is {password}, and the original password is {y}.")

def main():
    stored = ""
    while True:
        print("Menu:")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        entered = int(input("Please enter an option: "))
        
        match entered:
            case 1: stored = encoder()
            case 2: decoder(stored)
            case 3: exit(200)


if __name__ == "__main__":
    main()




