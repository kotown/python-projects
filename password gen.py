import string
import random

def passwordgen():
    #use the modules from string that contain all characters 
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    
    #GEt the desired length from user
    passlen = int(input("Enter thr desired password length: "))
    
    #append all characters to a list / array
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    #generate the passwrd 
    random.shuffle(s)    
    pas = ("".join(s[0:passlen]))
    print(pas)
    
passwordgen()
    