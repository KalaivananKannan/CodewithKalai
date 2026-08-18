def gift_wrapper(a):
    print("Happy Birthday")
    a()
    
def gift_message():
    print("All the best")

def gift_card():
    print("Merry Christmas")


num=int(input("1. Gift card 2. Gift message"))

if num==1:

    gift_wrapper(gift_card)

if num==2:

    gift_wrapper(gift_message)

