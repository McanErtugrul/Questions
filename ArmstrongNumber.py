def IsArmstrongNumber(_listValue):
    count=0
    for i in range (0,len(_listValue)):
        count+=_listValue[i]**len(_listValue)
    return count



inputValue=int(input("Value:"))
listValue=[int(x) for x in str(inputValue)]
list(listValue)
result=IsArmstrongNumber(listValue)
if(inputValue==result):
    print("This is a Armstrong Number!")
else:
    print("This isn't a Armstrong Number!")