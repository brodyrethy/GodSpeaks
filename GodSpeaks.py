import random

keywords = ["yes", "yep", "sure","yeah","yuh","Yes","Yep","Sure","Yeah","Yuh"]

def main():
    with open("Happy.TXT") as f:
        gdWrds = f.read().splitlines()

    print(end="God says... ")

    for x in range(0, 30):
        wrds = random.choice(gdWrds)
        print(wrds, end=" ")

    wrds = random.choice(gdWrds)
    print(wrds + ".\n")




while True:
    main()
    for x in range(0, 3):
        main()

    var = input('display more?')


    if any(keyword in var for keyword in keywords):
        main()
    else:
        exit()
