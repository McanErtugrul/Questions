def GCDCalculator(_inputValue1, _inputValue2):
    i = 1
    GCD = 1
    while (i <= inputValue1 and i <= inputValue2):
        if (not (_inputValue1 % i) and not (_inputValue2 % i)):
            GCD = i
        i += 1

    return GCD


inputValue1 = int(input("1. Value: "))
inputValue2 = int(input("2. Value: "))
print("GCD : {}".format(GCDCalculator(inputValue1, inputValue2)))
