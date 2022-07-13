def main():
    print("hello world")

main()

def say_name(name):
    print(name)

say_name("eby")

def call_name(fname, lname):
    print(fname, lname)

call_name("ebere", "nwankwo")

def if_True_say(yes=False):
    print(yes)

if_True_say(True)

def drive(gear="p"):
    if gear == "d":
        print("moving")
    elif gear == "r":
        print("moving forward")
    else:
        print("stopped")

drive("r")

def cook_rice(rice, salt):
    if rice:
        if salt:
            print("cooking with salt")
        else:
            print("cooking without salt")
    else:
        print("get rice")

cook_rice(True, True)

