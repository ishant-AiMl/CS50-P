####### Code of Approach 1......

name = input("enter the name:-> ").lower().strip()

if name[0:5] == "hello":
    print("$0")
elif name[0] == "h":
    print("$20")
else:
    print("$100")



####### Code of Approach 2......
## another type of this code is 
name = input("enter the name with greeting them :-> ").lower().strip()
if name.startswith("hello"):
    print("$0")
elif name.startswith("h"):
    print("$20")
else:
    print("$100")    
