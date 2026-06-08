name, age = input("Enter your name and age: ").split()
age = int(age)
DOB = 2026 - age
print (f"Hello {name}, what is up? So you just reached {age} years old huh? Let me take a guess, you were born in the year {DOB}? Or am I wrong?")
reply = input("Your reply: ").lower()
if reply == "yes" or reply == "yea" or reply == "yeah":
    print ("Haha see, my calculations are flawless.")
    
if reply == "no" or reply == "nah" or reply == "nope":
    print ("I don't really care either way. So how old are you anyway?")
    next_reply = int(input("Your reply: "))
    if next_reply < 2010:
        print ("Wow, you're pretty old.")
    elif next_reply > 2010:
            print ("Grow up kid.")
    else:
                print ("Ah, so you were born exactly in 2010?")
   