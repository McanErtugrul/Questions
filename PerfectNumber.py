def IsPerfectNumber(value):
    count=0
    for i in range (1,value):
        if(value%i==0):
            count+=i

    if(value==count):
        print("This is a Perfect Number.")
    else:
        print("This isn't a Perfect Number.")


inputValue=int(input("Value:"))
IsPerfectNumber(inputValue)