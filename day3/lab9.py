#Take username and password from user and check it again for three times whether the user has entered the right 
#username and password.if yes then print a message "Logged in successfullu",if not then print invalid credentials 
#for consecutive 3 times AND IF THE LIMIT EXCEEDS than print "Attempt finished"
for i in  range(3):
    A = input("enter the user name ")
    if(A)=="Mukesh":
        B=input("enter thepassword ")
        if(B)==12345:
            print("Logged in")
            break
        else:
            print("invalid password")
    else:
            print("invalid username")
else:
        print("enter")



