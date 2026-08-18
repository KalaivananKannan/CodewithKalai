try:
    a=2
    b=5
    c=b
    b=a
    a=c
    f=open("yes.txt", "w")
    first=int(input("a = 2, Enter 5 to swap "))
    print("hi")
    f.close()
    second=int(input("b = 5, Enter 2 to swap "))

    if first!=5 or second!=2:
        print("Wrong swaps entered!")
    
    else:
        print("a=",first)
        print("b=",second)
    
except Exception as e:  # we can use this to capture all the errors. Exception is a class. "e" can be stored as error logs
    print("Invalid input. Please enter only numbers")

    # f=open("yes.txt", "w")
    # f.write(str(e))
    # f.close()
finally:  # if it is mandatory to exectue the code in the exception, we can use finally 
    print("finished")
    f.close()