name=input("What is your name?")
if len(name) < 3:
    print("Name must be atleast 3 characters long")
elif len(name) > 10:
        print("name is too long")
else:
    print("name is good")