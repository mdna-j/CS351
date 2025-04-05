'''
BNF for var def code with format:

myvar= 5+6+2.3;

BNF:

exp -> id = math;
math -> int+math | float

Note that this is just a shortened example code for demostration only. The final tree misses internal nodes like int or float, since we are not doing word level BNF here.
'''

Mytokens = [
    ("id", "myvar"), ("op", "="), ("int", "5"), ("op", "*"), ("float", "4.3"),
    ("op", "+"), ("float", "2.1"), ("sep", ";")
]
inToken = ("empty", "empty")


def accept_token():
    global inToken
    print("     accept token from the list: " + inToken[1])
    if Mytokens:
        inToken = Mytokens.pop(0)


def math():
    global inToken
    print("\n----parent node math, finding children nodes:")

    if (inToken[0] == "float"):
        print("child node (internal): float")
        print("   float has child node (token): " + inToken[1])
        accept_token()
    elif (inToken[0] == "int"):
        print("child node (internal): int")
        print("   int has child node (token): " + inToken[1])
        accept_token()

        # Loop to handle multiple operations in the expression (e.g., +, *)
        while (inToken[1] in ["+", "*"]):
            print("child node (token): " + inToken[1])
            accept_token()
            if (inToken[0] in ["int", "float"]):
                print("child node (internal): " + inToken[0])
                print("   " + inToken[0] + " has child node (token): " + inToken[1])
                accept_token()
            else:
                print("error: math expects int or float after " + inToken[1])

    else:
        print("error: math expects float or int")


def exp():
    global inToken
    print("\n----parent node exp, finding children nodes:")
    typeT, token = inToken

    if typeT == "id":
        print("child node (internal): identifier")
        print("   identifier has child node (token): " + token)
        accept_token()
    else:
        print("error: expected identifier as the first element of the expression!")
        return

    if inToken[1] == "=":
        print("child node (token): " + inToken[1])
        accept_token()
    else:
        print("error: expected '=' as the second element of the expression!")
        return

    print("Child node (internal): math")
    math()


def main():
    global inToken
    if Mytokens:
        inToken = Mytokens.pop(0)
        exp()
        if inToken[1] == ";":
            print("\nparse tree building success!")
        else:
            print("error: expected ';' at the end")
    else:
        print("error: token list is empty")


# Run the main function to start parsing
main()