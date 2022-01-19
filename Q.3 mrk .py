print("____WELCOME IN LOGIN AND SIGNUP PAGE!____")
def signup(p):
    if len(p)>=6 and len(p)<=16:
        if p>="a" or p<="z":
            if "@" in p or "#" in p:
                if "1"in p or "2"in p or "3" in p or "4" in p or "5" in p or "6" in p or "7" in p or "8" in p or "9" in p or "0" in p:
                    print("strong passward")
                else:
                    print("week passward")
                    p=input("Enter your passward:")
                    signup(p)
            else:
                print("add special character.")
                p=input("Enter your paasward:")   
                signup(p)
        else:
            print("add alphabets")
            p=input("Enter your paasward:")
            signup(p)
    else:
        print("please check the lenght of passward, atleast 6 and maximum 16.")
p=input("ENter your passward:")
signup(p)