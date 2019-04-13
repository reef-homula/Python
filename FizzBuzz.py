for i in range(1, 101):
    outnum = i
    if i % 3 == 0 and i % 5 == 0:
        outnum = "FizzBuzz"
    elif i % 3 == 0:
        outnum = "Fizz"
    elif i % 5 == 0:
        outnum = "Buzz"
    
    print(outnum)